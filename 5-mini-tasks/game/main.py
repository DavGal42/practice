"""
    Author: David Galstyan
    Description: This is a simple game created with the language python and module pygame
"""

import pygame
import random

pygame.init()

game_screen = pygame.display.set_mode((253, 450))
pygame.display.set_caption('Adventure Game')

icon = pygame.image.load('5-mini-tasks/game/imgs/joystick.png')
pygame.display.set_icon(icon)
background_image = pygame.image.load('5-mini-tasks/game/imgs/background.jpg')

basket = pygame.image.load('5-mini-tasks/game/imgs/basket.png')
basket_speed = 1
basket_x = 100
basket_y = 412

coin = pygame.image.load('5-mini-tasks/game/imgs/coin.png')
bomb = pygame.image.load('5-mini-tasks/game/imgs/bomb.png')
falling_speed = 0.5

label1 = pygame.font.Font('5-mini-tasks/game/fonts/Jersey15-Regular.ttf', 40)
label2 = pygame.font.Font('5-mini-tasks/game/fonts/Jersey15-Regular.ttf', 20)
lose_label = label1.render('You Lose!', False, 'White')
author = label2.render('Created by: David Galstyan', False, 'White')
restart_label = label1.render('Play Again', False, (115, 132, 148))
restart_label_rect = restart_label.get_rect(topleft=(50, 200))

sound = pygame.mixer.Sound('5-mini-tasks/game/sounds/bg-sound.mp3')
sound.play()

game_active = True
score = 0

class FallingObject:
    def __init__(self, image, x, y, speed):
        self.image = image
        self.x = x
        self.y = y
        self.speed = speed
        self.rect = self.image.get_rect(topleft=(x, y))
    
    def update(self):
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

falling_objects = []

def spawn_falling_object():
    if random.randint(0, 1) == 0:
        falling_objects.append(FallingObject(coin, random.randint(0, 253 - coin.get_width()), 0, falling_speed))
    else:
        falling_objects.append(FallingObject(bomb, random.randint(0, 253 - bomb.get_width()), 0, falling_speed))

spawn_event = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_event, 1500)

running = True

while running:
    game_screen.blit(background_image, (0, 0))

    if game_active:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            basket_x -= basket_speed
        if keys[pygame.K_RIGHT]:
            basket_x += basket_speed

        basket_x = max(0, min(basket_x, 253 - basket.get_width()))

        game_screen.blit(basket, (basket_x, basket_y))

        for obj in falling_objects[:]:
            obj.update()
            obj.draw(game_screen)

            if obj.rect.colliderect(basket.get_rect(topleft=(basket_x, basket_y))):
                falling_objects.remove(obj)
                if obj.image == bomb:
                    game_active = False
                elif obj.image == coin:
                    score += 1

            elif obj.y > 450:
                falling_objects.remove(obj)

        score_text = label2.render(f'Score: {score}', False, 'White')
        game_screen.blit(score_text, (10, 10))

    else:
        game_screen.fill((87, 88, 89))
        game_screen.blit(author, (20, 320))
        game_screen.blit(lose_label, (50, 100))
        game_screen.blit(restart_label, restart_label_rect)
        
        final_score_text = label2.render(f'Final Score: {score}', False, 'White')
        game_screen.blit(final_score_text, (60, 150))

        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            game_active = True
            falling_objects.clear()
            score = 0

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == spawn_event and game_active:
            spawn_falling_object()
