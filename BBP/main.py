import pygame
pygame.init() #initiate pygame and give permission to use pygame's functionality.

"""
python main.py

Responsible for:
- Starting Pygame
- Running the game loop 
- Handling input
- Updating state  #State = data that describes your world at this moment / describe the current situation.
- Collision detection/response
- Rendering the game #rendering = Take the current state and display it on the screen
- Display
"""

#Game configuration - describe the environment. CAPITALISED ∵ they're treated as fixed configuration.
(WIDTH, HEIGHT) =  300,500
BLUE = (0,0,255) 

#ball states - can change hence lower case.
x = 100
y = 100
vx = 2
vy = 5
radius = 20

#pygame setup
window = pygame.display.set_mode(size=(WIDTH,HEIGHT)) 
clock = pygame.time.Clock()
is_running = True

#function input:
def process_input(is_running):
    #Process input
    for event in pygame.event.get(): #event = user action such as closing window, key presses, mouse clicks # this is the PROCESS INPUT
        if event.type == pygame.QUIT:
            is_running = False
    return is_running


def update(x,y,vx,vy):
     #update state: new position = old position + velocity
        x = x + vx  #2 pixels horizontally per loop
        y = y + vy  #5 pixels vertically per loop
    
        #collision detection/response
        if x + radius >= WIDTH : 
            vx = -vx
    
        elif x - radius <= 0 : 
            vx = -vx #(- and - becomes + )
    
        if y + radius >= HEIGHT : 
            vy = -vy
        
        elif y - radius <= 0 :
            vy = -vy #(- and - becomes + )

        return x,y,vx,vy

def render(x,y):
     #Render
    window.fill((0,0,0))  #clears a graphical surface/screen by painting it entirely in black//black background, redrawn every frame / this is what i was MISSING. //why does the circle need to be drawn every frame? Part of the answer is: because you also need to erase the previous frame every time, otherwise old frames pile up visually. 
    pygame.draw.circle(window, BLUE, (x,y), radius) #center: (x, y). window - The target surface or screen where the circle appears.

def display():
    #Display
    pygame.display.update() # Draws the surface object to the screen.
    #control FPS - limit the game to 60 FPS
    clock.tick(60)



while is_running:

    is_running = process_input(is_running)
    x,y,vx,vy = update(x,y,vx,vy)
    render(x,y)
    display()
   

           
pygame.quit()
#pygame.event.get() = collecting everything the user has done since the last frame.






#new position = old position * velocity 
#rendering - showing the world
#state = changing the world
