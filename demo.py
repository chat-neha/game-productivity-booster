import pygame
from sys import exit
from random import randint
import importlib
import coins as cn

pygame.init()

def game_main():
    
    def load_high_score():
        hs = open('highscores.txt','r')
        hs.seek(0)
        hiScore = hs.read()
        print(hiScore)

        if hiScore!='':
            hs.close()
            return int(hiScore)
        else:
            hs.close()
            return 0

    def save_high_score(score):
        hs = open('highscores.txt','w')
        hs.write(str(score))
        hs.close()

    def display_score():
        score_srfc = test_font.render(f'Score: {int(score/60)}',False,(64,64,64))
        score_rect = score_srfc.get_rect(center = (400,50))
        high_score_srfc = test_font.render(f'High Score: {high_score}',False,(64,64,64))
        high_score_srfc_rect = high_score_srfc.get_rect(center = (400,20))
        screen.blit(score_srfc,score_rect)
        screen.blit(high_score_srfc,high_score_srfc_rect)
        return score
       
    def obstacle_movement(li):
        if li:
            for rect in li:
                rect.x -= 6
                if int(score/60)>15:rect.x-=6.005
                if int(score/60)>30:rect.x-=6.05
                if rect.bottom == 300: 
                    screen.blit(snail_srfc,rect)
                if rect.bottom == 200: 
                    screen.blit(fly_srfc,rect)
            li = [rect for rect in li if rect.x>-100]
            return li
        else: return []

    def collisions(player,obstacles):
        if obstacles:
            for obstacle_rect in obstacles:
                if player.colliderect(obstacle_rect):
                    lost_sound.play()
                    return False
        return True   

    def player_animation(player_idx,player_srfc):
        
        #global player_idx 
        #global player_srfc
        
        if player_rect.bottom<300:
            player_srfc = player_jump
            return player_srfc

        else:
            player_idx += 0.1
            if player_idx >= len(player_walk):
                player_idx = 0

            player_srfc = player_walk [int(player_idx)]

            return player_srfc
       

    screen = pygame.display.set_mode((800,400))
    
    clock = pygame.time.Clock()
    pygame.display.set_caption("Productive Jump!")

    test_font = pygame.font.Font('Graphics/font/Pixeltype.ttf',40)

    
##    coin_srfc = test_font.render(f'Coins: {coins}',False,(64,64,64))
##    coin_rect = coin_srfc.get_rect(center = (800,50))
##    screen.blit(coin_srfc,coin_rect)
    
    game_active = True
    game_name = test_font.render("Productive Jump!",False,(111,196,169))
    game_name_rect = game_name.get_rect(center = (400,50))
    # start_time = 0
    score = 0
    hs = open('highscores.txt','r')
    hi = hs.read()
    if hi=='':
        high_score = 0
    else:
        high_score = hi


    sky_srfc = pygame.image.load('graphics/Sky.png').convert()
    ground_srfc = pygame.image.load('graphics/ground.png').convert()

    winter_sky_srfc = pygame.image.load('graphics/Sky.png').convert()
    winter_ground_srfc = pygame.image.load('graphics/ground.png').convert()

    # score_srfc = test_font.render("Game!", False , (64,64,64))
    # score_rect = score_srfc.get_rect(center = (400,50))

    snail_srfc1 = pygame.image.load('graphics/snail1.png').convert_alpha()
    snail_srfc2 = pygame.image.load('graphics/snail2.png').convert_alpha()
    snail_list = [snail_srfc1,snail_srfc2]
    snail_idx = 0
    snail_srfc = snail_list[snail_idx]

    fly_srfc1 = pygame.image.load('graphics/Fly1.png')
    fly_srfc2 = pygame.image.load('graphics/Fly2.png')
    fly_list = [fly_srfc1,fly_srfc2]
    fly_idx = 0 
    fly_srfc = fly_list[fly_idx]
    #obstacles
    obstacle_rect_list = []

    player_srfc1 = pygame.image.load('graphics/player_walk_1.png').convert_alpha()
    player_srfc2 = pygame.image.load('graphics/player_walk_2.png').convert_alpha()
    player_walk = [player_srfc1,player_srfc2]
    player_jump = pygame.image.load('graphics/jump.png').convert_alpha()

    player_idx = 0
    player_srfc = player_walk[player_idx]
    player_rect = player_srfc.get_rect(midbottom =(80,300))
    player_gravity = 0

    jump_sound = pygame.mixer.Sound('audio/jump.mp3')
    jump_sound.set_volume(0.5)
    player_stand = pygame.transform.rotozoom(pygame.image.load('graphics/player_stand.png').convert_alpha(),0,2)
    player_stand_rect = player_stand.get_rect(center = (400,200))
    lost_sound = pygame.mixer.Sound('audio/death.mp3')
    lost_sound.set_volume(0.5)

    gameover_srfc = test_font.render("GAMEOVER! Restart?",False,(111,196,169))
    gameover_rect = gameover_srfc.get_rect(center=(400,300))

    yes_srfc = test_font.render("Yes!",False,(111,196,169))
    yes_rect = yes_srfc.get_rect(center = (300,350))

    no_srfc = test_font.render("No!",False,(111,196,169))
    no_rect = no_srfc.get_rect(center = (500,350))

    #timer
    obstacle_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(obstacle_timer,1500)

    snail_ani_timer = pygame.USEREVENT + 2
    pygame.time.set_timer(snail_ani_timer,500)

    fly_ani_timer = pygame.USEREVENT + 3
    pygame.time.set_timer(fly_ani_timer,800)

##    player_ani_timer = pygame.USEREVENT + 4
##    pygame.time.set_timer(player_ani_timer,1000)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if game_active: 
                if event.type == obstacle_timer:
                    if randint(0,2):
                        obstacle_rect_list.append(snail_srfc.get_rect(bottomright = (randint(900,1100),300)))
                    else:
                        obstacle_rect_list.append(fly_srfc.get_rect(bottomright = (randint(900,1500),200)))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if player_rect.collidepoint(event.pos):
                        player_gravity = -20
                if event.type == pygame.KEYDOWN and (player_rect.bottom == 300 or player_rect.bottom == 320):
                    if event.key == pygame.K_SPACE:
                        player_gravity = -20
                        jump_sound.play()
                if event.type == snail_ani_timer:
                    if snail_idx == 0: snail_idx = 1
                    else:snail_idx = 0
                    snail_srfc = snail_list[snail_idx]
                if event.type == fly_ani_timer:
                    if fly_idx == 0: fly_idx = 1
                    else:fly_idx = 0
                    fly_srfc = fly_list[fly_idx]
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if yes_rect.collidepoint(event.pos):
                        if(cn.coin_decrease(100)):
                            game_active = True
                            score = 0   
                        else:
                            break                         
                        
                        # start_time = pygame.time.get_ticks()
                    elif no_rect.collidepoint(event.pos):
                        menu=importlib.import_module('menu')
                        importlib.import_module('doing') 
                        menu.main_menu()
                
        

        if game_active:
            score += 1
            screen.blit(winter_sky_srfc,(0,0))
            screen.blit(winter_ground_srfc,(0,300))
            # pygame.draw.rect(screen,'Lavender',score_rect)
            # pygame.draw.rect(screen,'Lavender',score_rect,10)
            # screen.blit(score_srfc,score_rect)
            score = display_score()   
            # snail_rect.x -= 6
            # if snail_rect.right<=0:
            #     snail_rect.left = 800
            # screen.blit(snail_srfc,snail_rect)
            
            player_gravity += 0.88
            player_rect.y += player_gravity 
            if player_rect.bottom >= 300: player_rect.bottom = 300
            if player_rect.top <= 0 : player_rect.top = 0
            screen.blit(player_srfc,player_rect)
            player_idx = 0
            player_srfc=player_animation(player_idx,player_srfc)

            #obstacle movement
            obstacle_rect_list = obstacle_movement(obstacle_rect_list)

            #collisions
            game_active = collisions(player_rect,obstacle_rect_list)
            if not(game_active):
                game_score = int(score/60)
                last_high_score = load_high_score()
                high_score = max(last_high_score,game_score)
                
                save_high_score(high_score)
                obstacle_rect_list = []
        
        else:
            
            score_msg = test_font.render(f'Your Score: {int(score/60)}',False,(111,196,169))
            score_msg_rect = score_msg.get_rect(center = (400,20))
            screen.fill((94,129,162))
            screen.blit(player_stand,player_stand_rect)
            screen.blit(gameover_srfc,gameover_rect)
            screen.blit(yes_srfc,yes_rect)
            screen.blit(no_srfc,no_rect)
            screen.blit(game_name,game_name_rect)
            screen.blit(score_msg,score_msg_rect)
            player_rect.midbottom = ((80,300))
            

        pygame.display.update()
        clock.tick(60)

    #surface-display surface-only 1-window
    #regular surface can be only placed on display surface

