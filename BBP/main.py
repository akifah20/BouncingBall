#entry point

"""
Responsible for:

starting pygame
game loop
calling update/render methods

Think of this as the “controller” of the program.

 pip install pygame
"""


import pygame
pygame.init() #initiate pygame and give permission to use pygame's functionality.

blue = (0,0,255)
(width,height) =  300,500

window = pygame.display.set_mode(size=(width,height)) 

is_running = True
while is_running:
    pygame.draw.circle(window, blue, (150,150), 75)
    pygame.display.update()
    for event in pygame.event.get(): #event = user action such as closing window, key presses, mouse clicks
        if event.type == pygame.QUIT:
            is_running = False
pygame.quit()
#pygame.event.get() = collecting everything the user has done since the last frame.

#pygame.display.update() # Draws the surface object to the screen.