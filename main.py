import pygame

#Initialize pygame
pygame.init()

#Screen Size
class Screen():
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
    def make(self):
        pygame.display.set_mode((self.width, self.height))

#Screen
screen = Screen()
screen.make()

#Caption
pygame.display.set_caption("Snake Game")


#Run loop
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False