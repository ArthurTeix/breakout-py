import pygame

pygame.init()

screen_size = (800, 800) 
screen = pygame.display.set_mode(screen_size) # create screen

pygame.display.set_caption("Breakout") # title

# ball
ball_size = 15
ball = pygame.Rect(100, 500, ball_size, ball_size) # init position ball

# player
width_player = 100
player = pygame.Rect(0, 750, width_player, 15)

# Number of blocks
number_blocks_line = 8
number_lines = 5
all_blocks = number_blocks_line * number_lines

def create_blocks(number_blocks_line, number_lines):
    blocks = []
    return blocks

# pygame colors (RGB)
colors = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'yellow': (255, 255, 0),
    'blue': (0, 0, 255),
    'green': (0, 255, 0)
}

# score
points = 0

#       x-axis and y-axis
ball_speed = [1, 1]

# show screen
screen.fill(colors['black']) # bg-color screen

# loop game
end_game = False   
while not end_game:

    for event in pygame.event.get(): # event of the player
        if (event.type == pygame.QUIT):
            end_game = True 

    # update screen
    pygame.time.wait(1) 
    pygame.display.flip()