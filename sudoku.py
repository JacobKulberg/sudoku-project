import pygame, sys
from sudoku_generator import *

pygame.init()
screen = pygame.display.set_mode((720, 790))
pygame.display.set_caption("Sudoku")
screen.fill((239, 235, 216))
def grids():
    #light lines
    for i in range(1, 9):
        #horizontals
        pygame.draw.line(screen, "black", (0, i * 80), (720, i * 80))
        #verticals
        pygame.draw.line(screen, "black", (i * 80, 0), (i * 80, 720))
    #heavy/box lines
    for i in range(1, 3):
        pygame.draw.line(screen, "black", (0, i * 240), (720, i * 240), 3)
        pygame.draw.line(screen, "black", (i * 240, 0), (i * 240, 720), 3)
grids()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()