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
    joystix = pygame.font.Font(os.path.join("assets", "fonts", "joystix.ttf"), 15)
    
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
    def redrawBg():
        screen.blit(bg, (0, 0))
    redrawBg()
    def redrawTextBox():
        pygame.draw.rect(screen, (30,30,30), (0, 400, 800, 50))
    redrawTextBox()
    def redrawSpriteBox():
        pygame.draw.rect(screen, (0,0,0), (300, 200, 200, 200))
    redrawSpriteBox()
    
    ###############################
    # initializing some variables #
    ###############################
    global location
    global hp
    global maxHp
    global level
    global lhml
    location = 0
    hp = 20
    maxHp = 20
    level = 1
    lhml = [location, hp, maxHp, level]
    
    #####################
    # loading save data #
    #####################
    try:
        with open(os.path.join("data", "save.txt"), "rb") as save:
            lhml = pickle.load(save)
            location = lhml[0]
            hp = lhml[1]
            maxHp = lhml[2]
            level = lhml[3]
    except(ValueError, SyntaxError, MemoryError, pickle.UnpicklingError):
        screen.blit(joystix.render(">Save data was corrupted. Please restart.", True, (255,255,255)), (0,400))

    #########################
    # is your code running? #
    #########################
    running = True
    #####################################
    # then you better go catch it. heh. #
    #####################################
    
    while running:
        
        for event in pygame.event.get():
            ########################################################
            # thank god this makes me not have to use task manager #
            # dont fucking edit this or i will die.                #
            # i really dont understand any of this wizardry        #
            ########################################################
            if(event.type == pygame.QUIT):
                lhml = [location, hp, maxHp, level]
                with open(os.path.join("data", "save.txt"), "wb") as save:
                    pickle.dump(lhml, save)
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
