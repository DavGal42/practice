"""
    Author: David Galstyan
    Description: This is a simple game created with the language python and module pygame
"""

import pygame

pygame.init()

game_screen = pygame.display.set_mode((253, 450))

pygame.display.set_caption('Adventure Game')

icon = pygame.image.load('5-mini-tasks/game/imgs/joystick.png')
pygame.display.set_icon(icon)

background_image = pygame.image.load('5-mini-tasks/game/imgs/background.jpg')

label1 = pygame.font.Font('5-mini-tasks/game/fonts/Jersey15-Regular.ttf', 40)
label2 = pygame.font.Font('5-mini-tasks/game/fonts/Jersey15-Regular.ttf', 20)
lose_label1 = label1.render('You Lose!', False, 'White')
author = label2.render('Created by: David Galstyan', False, 'White')
restart_label1 = label1.render('Play Again', False, (115, 132, 148))
restart_label1_rect = restart_label1.get_rect(topleft=(150, 140))

sound = pygame.mixer.Sound('5-mini-tasks/game/sounds/bg-sound.mp3')
sound.play()

game_active = True

running = True

while running:
    game_screen.blit(background_image, (0, 0))

    if game_active:
        pass

    else:
        game_screen.fill((87, 88, 89))
        game_screen.blit(author, (20,320))
        game_screen.blit(lose_label1, (150, 100))
        game_screen.blit(restart_label1, restart_label1_rect)

        mouse = pygame.mouse.get_pos()
        if restart_label1_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()