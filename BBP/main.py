#entry point

"""
Responsible for:

starting pygame
game loop
calling update/render methods

Think of this as the “controller” of the program.

 pip install pygame
 python main.py

"""
import pygame
pygame.init() #initiate pygame and give permission to use pygame's functionality.

blue = (0,0,255)
(width,height) =  300,500

x = 1
y = 100
vx = 2 #horizontal velocity
vy = 0 #vertical velocity 
radius = 65

window = pygame.display.set_mode(size=(width,height)) 
is_running = True
while is_running:
    window.fill((0,0,0))  #clears a graphical surface/screen by painting it entirely in black//black background, redrawn every frame / this is what i was MISSING. //why does the circle need to be drawn every frame? Part of the answer is: because you also need to erase the previous frame every time, otherwise old frames pile up visually.
    #if x + radius < width and width > 0 : 
    x = x + vx  # new position = old position + velocity 
    pygame.draw.circle(window, blue, (x,y), radius) 
    pygame.display.update() # Draws the surface object to the screen.
        
    if x + radius >= width and width > 0 : 
        vx = -2 #this causes negative velocity. so now we use this value instead.

    elif x - radius == 0 : 
        vx = 2
        
    for event in pygame.event.get(): #event = user action such as closing window, key presses, mouse clicks
        if event.type == pygame.QUIT:
            is_running = False
pygame.quit()
#pygame.event.get() = collecting everything the user has done since the last frame.






# position = previous position * velocity 
