import pygame
import random
import math

#Initialize pygame
pygame.init()

# Screen
screen = pygame.display.set_mode((800, 600))

# Caption
pygame.display.set_caption("Snake Game")

# Direction
direction = ""

# Snake
snake_head = [400, 300]
snake_pos = []
snake_size = 16
snake_change = []
snake_length = 1


# Score Text
score = 0
score_font = pygame.font.Font('KdamThmorPro-Regular.ttf', 32)

def snake(pos):
    '''(int, int) -> None
    Draws a rectangle (the snake) on the screen'''
    for i in pos:
        pygame.draw.rect(screen, (128, 128, 128), (i[0], i[1], 16, 16))
    

def snake_movement(direction, snake):
    '''(str) -> str
    Moves snake according to the direction'''
    global snake_change
    for i in range(len(snake)):
        if direction == "North":
            snake_change[i][1] = -snake_size
            snake_change[i][0] = 0
        elif direction == "South":
            snake_change[i][1] = snake_size
            snake_change[i][0] = 0
        elif direction == "East":
            snake_change[i][0] = snake_size
            snake_change[i][1] = 0
        elif direction == "West":
            snake_change[i][0] = -snake_size
            snake_change[i][1] = 0

    return direction

def snakebody_movement(direction):

    global snake_pos
    global snake_change
    new_snake_x, new_snake_y = 0, 0
    for i in range(len(snake_pos)):
        if direction == "North":
            new_snake_x, new_snake_y = snake_pos[i][0], snake_pos[i][1] - 16
        elif direction == "South":
            new_snake_x, new_snake_y = snake_pos[i][0], snake_pos[i][1] + 16
        elif direction == "East":
            new_snake_x, new_snake_y = snake_pos[i][0] + 16, snake_pos[i][1]
        elif direction == "West":
            new_snake_x, new_snake_y = snake_pos[i][0] - 16, snake_pos[i][1]
        snake_pos.append([new_snake_x, new_snake_y])
        snake_change.append([0, 0])
        del snake_pos[i]
        del snake_change[i]

def apple_position():
    '''() -> int, int
    Gives a random coordinate for the apple spawn'''
    return random.randint(0, 800), random.randint(0, 600)

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
fps = 15
clock = pygame.time.Clock()

# Run loop
running = True
snake_pos.insert(0, snake_head)
snake_change.insert(0, [0, 0])

while running:

    # BG Colour
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Movement keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = snake_movement("West", snake_pos)
            elif event.key == pygame.K_RIGHT:
                direction = snake_movement("East", snake_pos)
            elif event.key == pygame.K_UP:
                direction = snake_movement("North", snake_pos)
            elif event.key == pygame.K_DOWN:
                direction = snake_movement("South", snake_pos)
            # Quit key (Escape)
            elif event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                direction = snake_movement("North", snake_pos)
        
    for i in range(snake_length):
        snake_pos[i][0] += snake_change[i][0]
        snake_pos[i][1] += snake_change[i][1]

        if len(snake_pos) > snake_length:
            del snake_pos[0]
            del snake_change[0]
        # Boundaries
        if snake_pos[i][0] <= 0:
            running = False
        elif snake_pos[i][0] >= 800:
            running = False
        if snake_pos[i][1] <= 0:
            running = False
        elif snake_pos[i][1] >= 600:
            running = False

        collision = isCollision(snake_pos[i][0], snake_pos[i][1], apple_x, apple_y)
        if collision:
            new_snake_x, new_snake_y = 0, 0
            apple_y = 2000
            apple_x, apple_y = apple_position()
            score += 1
            snake_length += 1
            if direction == "North":
                new_snake_x, new_snake_y = snake_pos[i][0], snake_pos[i][1] - 16
            elif direction == "South":
                new_snake_x, new_snake_y = snake_pos[i][0], snake_pos[i][1] + 16
            elif direction == "East":
                new_snake_x, new_snake_y = snake_pos[i][0] + 16, snake_pos[i][1]
            elif direction == "West":
                new_snake_x, new_snake_y = snake_pos[i][0] - 16, snake_pos[i][1]
            snake_pos.append([new_snake_x, new_snake_y])
            snake_change.append([0, 0])
            snake_movement(direction, snake_pos)
            snake(snake_pos)
            

    snake(snake_pos)
    apple(apple_x, apple_y)
    score_text()
    pygame.display.update()
    clock.tick(fps)

                


    
    
        

