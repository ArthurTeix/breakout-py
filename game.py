import pygame

pygame.init()

screen_size = (800, 800) 
screen = pygame.display.set_mode(screen_size) # create screen

pygame.display.set_caption("Breakout") # title

ball_size = 15
ball = pygame.Rect(100, 500, ball_size, ball_size) # init position ball

width_player = 100
player = pygame.Rect(0, 750, width_player, 15)

# Number of blocks
number_blocks_line = 8
number_lines = 5
all_blocks = number_blocks_line * number_lines
