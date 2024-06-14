import pygame 
from sys import exit
from random import randint
import importlib
import time
#global start_time 
pygame.init()

def game_main():

    def display_score():
        #current_time = int (pygame.time.get_ticks()/1000) - start_time
        score_surface = test_font.render(('Score: '+ str(int(score/60))), False, (64,64,64))
        score_rect = score_surface.get_rect (center = (400,50))
        screen.blit(score_surface, score_rect)
        return score

    def obstacle_movement(obstacle_list):
        if obstacle_list: #if there is something in the list
            for i in obstacle_list:
                if i.bottom==300:
                    screen.blit (snail_surface, i)
                else:
                    screen.blit (fly_surface, i)
                    
                i.x -=5

            obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

            return obstacle_list
        
        else:
            return []

    def collisions (player, obstacles):
        if obstacles:
            for i in obstacles:
                if player.colliderect(i):
                    return False

        return True
                    
        
    screen = pygame.display.set_mode((800,400))
    pygame.display.set_caption ("Runner")
    clock = pygame.time.Clock()
    test_font = pygame.font.Font('font/Pixeltype.ttf',50)
    game_active = True
    score = 0

    sky_surface = pygame.image.load ('graphics/Sky.png').convert()
    ground_surface = pygame.image.load ('graphics/ground.png').convert()

    #Obstacles 
    snail_surface = pygame.image.load ('graphics/snail/snail1.png').convert_alpha()

    fly_surface = pygame.image.load('graphics/fly/fly1.png').convert_alpha()

    obstacle_rect_list = []

    player_surface = pygame.image.load ('graphics/player/player_walk_1.png').convert_alpha()
    player_rect = player_surface.get_rect(midbottom= (80,300))
    player_gravity = 0

    #Game Over screen
    player_stand = pygame.image.load ('graphics/player/player_stand.png').convert_alpha()
    player_stand= pygame.transform.rotozoom(player_stand,0,2) #width and height of surface
    player_stand_rect = player_stand.get_rect(center = (400,200))

    game_name = test_font.render ('Pixel Runner', False, (111,196,169))
    game_name_rect = player_stand.get_rect(center = (380,150))

    game_message = test_font.render ('Press space to run', False, (111,196,169))
    game_message_rect = game_message.get_rect(center = (400,320))

    menu_message = test_font.render ('Return to Menu', False, (111,196,169))
    menu_message_rect = menu_message.get_rect(center = (400, 370))

    #Timer
    obstacle_timer = pygame.USEREVENT + 1 # to avoid clash with existing in-built events
    pygame.time.set_timer (obstacle_timer, 1500)


    while True:
        #score+=1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if game_active == True:
##                if event.type == pygame.MOUSEMOTION:
##                    if player_rect.collidepoint (event.pos) :
##                        player_gravity = -20

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and player_rect.bottom>=300: #spacebar
                        player_gravity = -20
                        #score+=1

            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    score = 0
                    
                else:
                    mouse_pos = pygame.mouse.get_pos()
                    #if event.type == pygame.MOUSEMOTION:
                    if menu_message_rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
    ##                        from menu import main_menu
    ##                        menu.main_menu()
    ##                        menu.close()
                        
                        menu=importlib.import_module('menu')
                       #current_time-=current_time
                       # start_time = int(pygame.time.get_ticks()/1000)
                        menu.main_menu()
                        
                    
                    
            if event.type == obstacle_timer and game_active:
                if randint(0,2):
                    obstacle_rect_list.append(snail_surface.get_rect(bottomright = (randint(900,1100),300)))
                else:
                    obstacle_rect_list.append(fly_surface.get_rect(bottomright = (randint(900,1100),210)))
                    

        if game_active == True:
            score += 1
            screen.blit(sky_surface, (0,0)) 
            screen.blit(ground_surface, (0,300))

            score = display_score()
            

    ##        if snail_rect.right<=0:
    ##            snail_rect.left = 800
    ##        screen.blit(snail_surface, snail_rect) --> not needed as imporved enemy spawn logic used


            player_gravity+=0.8
            player_rect.y += player_gravity
            if player_rect.bottom>=300:
                player_rect.bottom=300
            screen.blit(player_surface, player_rect)

            #obstacle movement
            obstacle_rect_list = obstacle_movement(obstacle_rect_list)

            game_active = collisions(player_rect,obstacle_rect_list)

        else:
            screen.fill((94,129,162))
            screen.blit(player_stand, player_stand_rect)
            obstacle_rect_list.clear()
            player_rect.midbottom = (80,300) #in case we crash into a fly, reset player to ground
            player_gravity = 0

            score_message = test_font.render(('Score: '+ str(int(score/60))), False, (111,196,169))
            score_rect = score_message.get_rect (center = (400,50))
            screen.blit(score_message, score_rect)
            screen.blit(game_message,game_message_rect)
            screen.blit(game_name, game_name_rect)
            screen.blit(menu_message, menu_message_rect)
        
            
        pygame.display.update()
        clock.tick(60)