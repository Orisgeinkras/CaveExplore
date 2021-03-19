##################
# necessary bits #
##################
import pygame
import sys
import os
import pickle

#############################
# the room where it happens #
#############################
def main():
    ###################################################################
    # initializing pygame module to use some funky commands.          #
    # dont really know what happens without this so... leaving it in. #
    # not like this is code golf lol                                  #
    # in fact, this is anti-code golf, look at these comments!        #
    ###################################################################
    pygame.init()
    
    ###########################
    # dont kill your cpu kids #
    # kek 30 fps              #
    ###########################
    pygame.time.Clock().tick(30)
    
    #############
    # load time #
    #############
    icon = pygame.image.load(os.path.join("assets", "images", "icon.png"))
    bg = pygame.image.load(os.path.join("assets", "images", "bg.png"))
    joystix = pygame.font.Font(os.path.join("assets", "fonts", "joystix.ttf"), 30)
    
    ##############################
    # game logo and window title #
    ##############################
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Game Title Placeholder Text")
    
    ####################################################
    # and the programmer said let there be game window #
    # and the game existed                             #
    ####################################################
    screen = pygame.display.set_mode((800,600))
    
    ###################################################################
    # graphic design is my passion                                    #
    # pretend that's in like comic sans or something with a shitty bg #
    ###################################################################
    screen.blit(bg, (0, 0))
    textBox = pygame.draw.rect(screen, (30,30,30), (0, 400, 800, 50))
    
    ###############################
    # initializing some variables #
    ###############################
    global location
    global hp
    global level
    global lhl
    location = 1
    hp = 20
    level = 1
    lhl = [location, hp, level]
    
    #####################
    # loading save data #
    #####################
    try:
        with open(os.path.join("data", "save.txt"), "rb") as save:
            lhl = pickle.load(save)
            location = lhl[0]
            hp = lhl[1]
            level = lhl[2]
    except(ValueError, SyntaxError, MemoryError, pickle.UnpicklingError):
        screen.blit(joystix.render(">Save data was corrupted.", True, (255,255,255)), (0,400))
        

    #########################
    # is your code running? #
    #########################
    running = True
    #####################################
    # then you better go catch it. heh. #
    #####################################
    
    while running:
        
        
        for event in pygame.event.get():
            
            ##################################
            # welcome to event handler hell. #
            ##################################
            
            ########################################################
            # thank god this makes me not have to use task manager #
            # dont fucking edit this or i will die.                #
            # i really dont understand any of this wizardry        #
            ########################################################
            if(event.type == pygame.QUIT):
                lhl = [location, hp, level]
                with open(os.path.join("data", "save.txt"), "wb") as save:
                    pickle.dump(lhl, save)
                running = False
                pygame.quit()
                sys.exit()
                ################
                # bye felicia. #
                ################
                

        pygame.display.update()

###############################################
# this makes the thing do the existing thing. #
###############################################
main()
