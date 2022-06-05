import pygame
import random
import math

#Initialize pygame
pygame.init()

# Screen
screen = pygame.display.set_mode((800, 600))

# Caption
pygame.display.set_caption("Snake Game")

# Snake
snake_head = [408, 300]
snake_x = []
snake_y = []
snake_x_change = 0
snake_y_change = 0
snake_length = 1


for i in range(snake_length):
    snake_x.append(408)
    snake_y.append(300)

# Score Text
score = 0
score_font = pygame.font.Font('KdamThmorPro-Regular.ttf', 32)

def snake(x, y):
    '''(int, int) -> None
    Draws a rectangle (the snake) on the screen'''
    pygame.draw.rect(screen, (128, 128, 128), (x, y, 16, 16))
    

def snake_movement(direction):
    '''(str) -> str
    Moves snake according to the direction'''
    global snake_x_change
    global snake_y_change
    if direction == "North":
        snake_y_change = -3
        snake_x_change = 0
    elif direction == "South":
        snake_y_change = 3
        snake_x_change = 0
    elif direction == "East":
        snake_x_change = 3
        snake_y_change = 0
    elif direction == "West":
        snake_x_change = -3
        snake_y_change = 0

    return direction

def apple_position():
    '''() -> int, int
    Gives a random coordinate for the apple spawn'''
    return random.randint(0, 784), random.randint(0, 584)

def apple(x, y):
    '''(int, int) -> None
    Randomizes x and y coordinates and draws apple randomly on the screen'''
    apple = pygame.image.load("apple.png")
    screen.blit(apple, (x, y))

def isCollision(snakeX, snakeY, appleX, appleY):
    '''(int, int, int, int) -> bool
    Takes in coordinates of the snake and the apple and uses distance formula to calculate distance between the two then returns True if within 16 pixels'''
    distance = math.sqrt((math.pow(snakeX - appleX, 2)) + (math.pow(snakeY - appleY, 2)))
    if distance < 16:
        return True
    return False

def score_text(x = 10, y = 10):
    '''(int, int) -> None
    Renders the text for the score'''
    text = score_font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (x, y))



#Apple Position
apple_x, apple_y = apple_position()

# FPS
fps = 60
clock = pygame.time.Clock()

# Run loop
running = True

while running:

    # BG Colour
    screen.fill((127, 255, 0))

    # Score Text

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Movement keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = snake_movement("West")
            elif event.key == pygame.K_RIGHT:
                direction = snake_movement("East")
            elif event.key == pygame.K_UP:
                direction = snake_movement("North")
            elif event.key == pygame.K_DOWN:
                direction = snake_movement("South")
            # Quit key (Escape)
            elif event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                direction = snake_movement("North")

    # Boundaries
    for i in range(snake_length):
        snake_x[i] += snake_x_change
        for j in range(1):
            snake_x.append(snake_x[i])
        if snake_x[i] < 0:
            running = False
        elif snake_x[i] > 784:
            running = False
        snake_y[i] += snake_y_change
        for j in range(1):
            snake_y.append(snake_y[i])
        if snake_y[i] < 0:
            running = False
        elif snake_y[i] > 584:
             running = False


        snake(snake_x[i], snake_y[i])


        collision = isCollision(snake_x[i], snake_y[i], apple_x, apple_y)
        if collision == True:
            apple_y = 2000
            apple_x, apple_y = apple_position()
            score += 1
            snake_length += 1
        
        
    apple(apple_x, apple_y)
    score_text()
    pygame.display.update()
    clock.tick(fps)

                


    
    
        

