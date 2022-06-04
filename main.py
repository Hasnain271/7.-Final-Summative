import pygame

#Initialize pygame
pygame.init()

#Screen Size


#Screen
screen = pygame.display.set_mode((800, 600))

#Caption
pygame.display.set_caption("Snake Game")

#Snake
snake_img = pygame.image.load("snake.png")
snake_x = 416
snake_y = 300

def snake(x, y):
    screen.blit(snake_img, (x, y))

#Run loop
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    snake(snake_x, snake_y)
    pygame.display.update()
        

