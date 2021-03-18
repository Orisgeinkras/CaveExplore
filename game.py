##################
# necessary bits #
##################
import pygame
import sys
import os

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
    # load time #d
    #############
    icon = pygame.image.load(os.path.join("assets", "images", "icon.png"))
    bg = pygame.image.load(os.path.join("assets", "images", "bg.png"))
    font = pygame.font.SysFont(os.path.join("assets", "fonts", "joystix monospace.ttf"), 12)
    
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
    
    #########################
    # is your code running? #
    #########################
    running = True
    #####################################
    # then you better go catch it. heh. #
    #####################################
    
    while running:
        
        screen.blit(bg, (0, 0))   
        
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
