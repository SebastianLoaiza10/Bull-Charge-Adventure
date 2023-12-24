import pygame
import sys
from config import config

# Initialize Pygame
pygame.init()

# Setting up game window
screen = pygame.display.set_mode((config.WIDTH,config.HEIGHT))
pygame.display.set_caption('Bull Charge Adventure')

# Loading game assests
icon_img = pygame.image.load('assets/bull_game_icon.jpg')
#bull_img = pygame.image.load('')
snowy_rock_img = pygame.image.load('assets/rock.png')
small_tree_img = pygame.image.load('assets/small_tree.png')
#present_img = pygame.image.load('')
background_img = pygame.image.load('assets/background.png')

# Create's game icon on window
pygame.display.set_icon(icon_img)


clock = pygame.time.Clock()
while True:
    # event handling
    for event in pygame.event.get():
        # Handles if the users closes the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background_img,(0,0))
    screen.blit(small_tree_img,(100,100))  
    screen.blit(snowy_rock_img,(500,500))

    # updates display and caps FPS based on config
    pygame.display.update()
    clock.tick(config.FPS)