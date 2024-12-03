from FINAL import SudokuGenerator
from Board import Board
from Cell import Cell
import pygame
import random

def translateX(v):
    if v < 630/9 * 1:
        return 0
    elif v < 630/9 * 2:
        return 1
    elif v < 630/9 * 3:
        return 2
    elif v < 630/9 * 4:
        return 3
    elif v < 630/9 * 5:
        return 4
    elif v < 630/9 * 6:
        return 5
    elif v < 630/9 * 7:
        return 6
    elif v < 630/9 * 8:
        return 7
    elif v < 630/9 *


def main():
    x1og = 0
    y1og = 0
    x2og = 0
    y2og = 0
    x1new = 0
    y1new = 0
    x2new = 0
    y2new = 0
    rows = []
    cols = []
    for i in range( 10):
        rows.append(i*(630/9))
    for i in range( 10):
        cols.append(i*(630/9))
    try:
       pygame.init()
       # You can draw the mole with this snippet:
       screen = pygame.display.set_mode((630, 630))
       clock = pygame.time.Clock()
       board = Board(630, 630, screen, 'easy')


       running = True
       selected = False
       while running:
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   running = False
               if event.type == pygame.MOUSEBUTTONDOWN:
                   eventpos = pygame.mouse.get_pos()
                   board.select(translateX(eventpos[0]), translateX(eventpos[1]))
                   x2og = x2new
                   y2og = y2new
                   x1og = x1new
                   y1og = y1new
                   for i in range(len(rows)):
                       if rows[i] > eventpos[0]:
                           x1new = rows[i-1]
                           x2new = rows[i]
                           break
                   for i in range(len(cols)):
                       if cols[i] > eventpos[1]:
                           y1new = cols[i-1]
                           y2new = cols[i]
                           break
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_1:
                       print('yep')
                       board.sketch(1)
                   elif event.key == pygame.K_2:
                       board.sketch(2)
                   elif event.key == pygame.K_3:
                       board.sketch(3)
                   elif event.key == pygame.K_4:
                       board.sketch(4)
                   elif event.key == pygame.K_5:
                       board.sketch(5)
                   elif event.key == pygame.K_6:
                       board.sketch(6)
                   elif event.key == pygame.K_7:
                       board.sketch(7)
                   elif event.key == pygame.K_8:
                       board.sketch(8)
                   elif event.key == pygame.K_9:
                       board.sketch(9)


                   # x = pygame.mouse.get_pos()[0]
                   # y = pygame.mouse.get_pos()[1]


      
           screen.fill("pink")
           board.draw()
           pygame.draw.line(screen, 'red', (x1new, y1new), (x1new, y2new), width=3)
           pygame.draw.line(screen, 'red', (x1new, y1new), (x2new, y1new), width = 3)
           pygame.draw.line(screen, 'red', (x2new, y1new), (x2new, y2new), width = 3)
           pygame.draw.line(screen, 'red', (x1new, y2new), (x2new, y2new), width = 3)


           pygame.display.flip()
           clock.tick(60)
    finally:
       pygame.quit()




if __name__ == "__main__":
   main()
