import pygame
import random

#Initialize pygame
pygame.init()


# Screen
screen = pygame.display.set_mode((800, 600))

# Caption
pygame.display.set_caption("Snake Game")

# Snake
snake_x = 408
snake_y = 300
snake_x_change = 0
snake_y_change = 0 

def snake(x, y):
    '''(int, int) -> None
    Draws a rectangle (the snake) on the screen'''
    pygame.draw.rect(screen, (128, 128, 128), (x, y, 16, 16))

def snake_movement(direction):
    '''(str) -> float, float
    Moves snake according to the direction'''
    global snake_x_change
    global snake_y_change
    if direction == "North":
        snake_y_change = -0.3
        snake_x_change = 0
    elif direction == "South":
        snake_y_change = 0.3
        snake_x_change = 0
    elif direction == "East":
        snake_x_change = 0.3
        snake_y_change = 0
    elif direction == "West":
        snake_x_change = -0.3
        snake_y_change = 0

    return snake_x_change, snake_y_change



# Apple
apple_x = random.randint(0, 800)
apple_y = random.randint(0, 600)
def apple(x, y):
    '''(int, int) -> None
    Randomizes x and y coordinates and draws apple randomly on the screen'''
    apple = pygame.image.load("apple.png")
    screen.blit(apple, (x, y))



# Run loop
running = True

while running:

    # BG Colour
    screen.fill((127, 255, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Movement keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change, snake_y_change = snake_movement("West")
            elif event.key == pygame.K_RIGHT:
                snake_x_change, snake_y_change = snake_movement("East")
            elif event.key == pygame.K_UP:
                snake_x_change, snake_y_change = snake_movement("North")
            elif event.key == pygame.K_DOWN:
                snake_x_change, snake_y_change = snake_movement("South")
            # Quit key (Escape)
            elif event.key == pygame.K_ESCAPE:
                running = False
            else:
                snake_x_change, snake_y_change = snake_movement("North")

    # Boundaries
    snake_x += snake_x_change
    if snake_x < 0:
        running = False
    elif snake_x > 784:
        running = False
    snake_y += snake_y_change
    if snake_y < 0:
        running = False
    elif snake_y > 584:
        running = False
    
    snake_x += snake_x_change
    snake_y += snake_y_change

    snake(snake_x, snake_y)
    apple(apple_x, apple_y)
    pygame.display.update()

                


    
    
        

