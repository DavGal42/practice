import pygame
import time


"""
    Author: David Galstyan
    Description: This is a simple game created with the language python and module pygame
                There is a person who wants to survive and his opponents are ghosts.He can
                go left,right and jump
"""


clock = pygame.time.Clock()

pygame.init()

screen = pygame.display.set_mode((600, 360))

pygame.display.set_caption('MyFirstGame')

icon = pygame.image.load('practice/5-mini-tasks/adventure-game/imgs/tree.png')
pygame.display.set_icon(icon)

bg = pygame.image.load('practice/5-mini-tasks/adventure-game/imgs/background.jpg').convert()
walk_left = [
    pygame.image.load('practice/5-mini-tasks/adventure-game/imgs/player-left/left1.png').convert_alpha(),
    pygame.image.load('practice/5-mini-tasks/adventure-game/imgs/player-left/left2.png').convert_alpha(),
    pygame.image.load('practice/5-mini-tasks/adventure-game/imgs/player-left/left3.png').convert_alpha(),
    pygame.image.load('practice/5-mini-tasks/adventure-game/imgs/player-left/left4.png').convert_alpha()
]
walk_right = [
    pygame.image.load('practice/5-mini-tasks/adventure-game/imgs/player-right/right1.png').convert_alpha(),
    pygame.image.load('practice/5-mini-tasks/adventure-game/imgs/player-right/right2.png').convert_alpha(),
    pygame.image.load('practice/5-mini-tasks/adventure-game/imgs/player-right/right3.png').convert_alpha(),
    pygame.image.load('practice/5-mini-tasks/adventure-game/imgs/player-right/right4.png').convert_alpha()
]


ghost = pygame.image.load('practice/5-mini-tasks/adventure-game/imgs/ghost.png').convert_alpha()
ghost_list_in_game = []

player_anim_count = 0
bg_x = 0

player_speed = 5
player_x = 150
player_y = 220

is_jump = False
jump_count = 8

bg_sound = pygame.mixer.Sound('practice/5-mini-tasks/adventure-game/sounds/bg-sound.mp3')
bg_sound.play()

ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 2500)

label1 = pygame.font.Font('practice/5-mini-tasks/adventure-game/fonts/Jersey15-Regular.ttf', 40)
label2 = pygame.font.Font('practice/5-mini-tasks/adventure-game/fonts/Jersey15-Regular.ttf', 20)
lose_label1 = label1.render('You Lose!', False, 'White')
author = label2.render('Created by: David Galstyan', False, 'White')
restart_label1 = label1.render('Play Again', False, (115, 132, 148))
restart_label1_rect = restart_label1.get_rect(topleft=(150, 140))

gameplay = True

running = True

def start_game():
    while running:
        screen.blit(bg, (bg_x, 0))
        screen.blit(bg, (bg_x + 600, 0))
        
        if gameplay:
            
            player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))    

            if ghost_list_in_game:
                for i, el in enumerate(ghost_list_in_game):
                    screen.blit(ghost, el)
                    el.x -= 10

                    if el.x < -10:
                        ghost_list_in_game.pop(i)

                    if player_rect.colliderect(el):
                        gameplay = False



            keys = pygame.key.get_pressed()


            if keys[pygame.K_LEFT]:
                screen.blit(walk_left[player_anim_count], (player_x,player_y))
            else:
                screen.blit(walk_right[player_anim_count], (player_x,player_y))



            if keys[pygame.K_LEFT] and player_x > 50:
                player_x -= player_speed
            elif keys[pygame.K_RIGHT] and player_x < 550:
                player_x += player_speed



            if not is_jump:
                if keys[pygame.K_SPACE]:
                    is_jump = True
            else:
                if jump_count >= -8:
                    if jump_count > 0:
                        player_y -= (jump_count ** 2) / 2
                    else:
                        player_y += (jump_count ** 2) / 2
                    jump_count -= 1
                else:
                    is_jump = False
                    jump_count = 8



            if player_anim_count == 3:
                player_anim_count = 0
            else:
                player_anim_count += 1



            bg_x -= 3
            if bg_x == -600:
                bg_x = 0
        else:
            screen.fill((87, 88, 89))
            screen.blit(author, (20,320))
            screen.blit(lose_label1, (150, 100))
            screen.blit(restart_label1, restart_label1_rect)

            mouse = pygame.mouse.get_pos()
            if restart_label1_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                gameplay = True
                player_x = 150
                ghost_list_in_game.clear()

        pygame.display.update()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == ghost_timer:
                ghost_list_in_game.append(ghost.get_rect(topleft=(600, 225)))


    clock.tick(10)

def main():
    start_game()

if __name__ == '__main__':
    main()