import pygame

pygame.init()

screen_size = (800, 800) 
screen = pygame.display.set_mode(screen_size) # create screen

pygame.display.set_caption("Breakout") # title

# ball
ball_size = 15
ball = pygame.Rect(385, 500, ball_size, ball_size) # init position ball

# player
width_player = 100
player = pygame.Rect(350, 750, width_player, 15)

# Number of blocks
number_blocks_line = 8
number_lines = 8
all_blocks = number_blocks_line * number_lines

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
# init
def draw_init_game():
    screen.fill(colors['black']) # bg-color screen

    pygame.draw.rect(screen, colors['blue'], player)
    pygame.draw.rect(screen, colors['white'], ball)

# blocks
def create_blocks(number_blocks_line, number_lines):
    width_screen = screen_size[0]
    height_screen = screen_size[1]

    block_distance = 5
    width_block = (width_screen / 8) - block_distance

    height_block = 15
    line_distance = height_block + 10


    blocks = []

    for j in range(number_lines):
        for i in range(number_blocks_line):
            # create block in screen
            block = pygame.Rect(i * (width_block + 5) + 2.5, (j * line_distance) + 40, width_block, height_block)
            # add block
            blocks.append(block)
    
    return blocks

def draw_blocks(blocks):
    for block in blocks:
        pygame.draw.rect(screen, colors['green'], block)

# move elements
def move_player(event):
    if (event.type == pygame.KEYDOWN): # 'KEYDOWN' = PRESS

        if (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
            player.x = player.x + 10 # position x-axis

        if (event.key == pygame.K_LEFT or event.key == pygame.K_a):
            player.x = player.x - 10

    pass

# initializing game
blocks = create_blocks(number_blocks_line, number_lines)

# loop game
end_game = False
while not end_game:
    draw_init_game()  
    draw_blocks(blocks)

    for event in pygame.event.get(): # event of the player
        if (event.type == pygame.QUIT):
            end_game = True 
        move_player(event)

    # update screen
    pygame.time.wait(1) 
    pygame.display.flip()

pygame.quit() # end pygame instance
