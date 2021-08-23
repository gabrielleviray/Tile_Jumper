# Import modules
import pygame

# Modules needed to start the game
from pygame.locals import *

# Initialize
pygame.init()

########################################
#                                      #
#          Create game window          #
#                                      #
########################################
window_width = 500
window_height = 500

# Create game window 
window = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption('Tile Jumper')

########################################
#                                      #
#              Game Loop               #
#                                      #
########################################
running = 1
while running:

    # Event handler: looks for events such as click, pressed keys, etc.
    # Cycle through all the events
    for event in pygame.event.get():

        # Look for when user clicks 'X' to close the game
        if event.type == pygame.QUIT:
            running = 0


pygame.quit()   # system exit
exit()  # closes window
