import pygame, sys
from button import Button
#import importlib
#import tkinter as tk
import coins as cn
import demo
#import doing as dn

pygame.init()

SCREEN=pygame.display.set_mode((800,400))
pygame.display.set_caption("Menu")

SCREEN.fill((94,129,162))

#game=importlib.import_module('demo')
#doing = importlib.import_module('doing')

def get_font(size):
    return pygame.font.Font('Graphics/font/Pixeltype.ttf',size)

def play(): 
        if(cn.coin_decrease(100)):
            demo.game_main()



def Tasks():
    import doing as dn
    dn.doing_main()
    pygame.display.update()

def main_menu():
    while True:
        SCREEN.fill((94,129,162))
        
        MENU_MOUSE_POS=pygame.mouse.get_pos()
        MENU_TEXT=get_font(80).render("PRODUCTIVE JUMP!",True,"#b68f40")
        MENU_RECT=MENU_TEXT.get_rect(center=(400, 80))

##        coins=cn.coin_decrease(100)
##        coin_srfc = test_font.render(f'Coins: {coins}',False,(64,64,64))
##        coin_rect = coin_srfc.get_rect(center = (700,50))
##        screen.blit(coin_srfc,coin_rect)
        
        PLAY_BUTTON = Button(image=None, pos=(400, 180), 
                                text_input="PLAY", font=get_font(55), base_colour="#d7fcd4", hovering_colour="White")
        TASKS_BUTTON = Button(image=None, pos=(400, 250), 
                                text_input="TASKS", font=get_font(55), base_colour="#d7fcd4", hovering_colour="White")
        QUIT_BUTTON = Button(image=None, pos=(400, 320), 
                                text_input="QUIT", font=get_font(55), base_colour="#d7fcd4", hovering_colour="White")          
                
        SCREEN.blit(MENU_TEXT,MENU_RECT)

        for button in [PLAY_BUTTON,TASKS_BUTTON,QUIT_BUTTON]:
                                               button.changeColour(MENU_MOUSE_POS)
                                               button.update(SCREEN)
                            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if TASKS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Tasks()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
            
        
            pygame.display.update()

main_menu()
