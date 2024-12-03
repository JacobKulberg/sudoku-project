import pygame
# import random
# from FINAL import SudokuGenerator
#
# def min_dif(list, num):
#     minitem = list[0]
#     for i in list:
#         if num > i:
#             if num - i < min:
#                 minitem = i
#     return minitem
# # board = [
# #                     [7, 8, 0, 4, 0, 0, 1, 2, 0],
# #                     [6, 0, 0, 0, 7, 5, 0, 0, 9],
# #                     [0, 0, 0, 6, 0, 1, 0, 7, 8],
# #                     [0, 0, 7, 0, 4, 0, 2, 6, 0],
# #                     [0, 0, 1, 0, 5, 0, 9, 3, 0],
# #                     [9, 0, 4, 0, 6, 0, 0, 0, 5],
# #                     [0, 7, 0, 3, 0, 0, 0, 1, 2],
# #                     [1, 2, 0, 0, 0, 7, 4, 0, 0],
# #                     [0, 4, 9, 2, 0, 6, 0, 0, 7]]
# board = SudokuGenerator(9, 30)
# board.fill_values()
# board.remove_cells()
# board.print_board()
#
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
    elif v < 630/9 * 9:
        return 8

#
# def main():
#     try:
#         pygame.init()
#
#         screen = pygame.display.set_mode((640, 512))
#         clock = pygame.time.Clock()
#         running = True
#         x1og = 0
#         y1og = 0
#         x2og = 0
#         y2og = 0
#         x1new = 0
#         y1new = 0
#         x2new = 0
#         y2new = 0
#         rows = []
#         cols = []
#         for i in range( 10):
#             rows.append(i*(640/9))
#         for i in range( 10):
#             cols.append(i*(512/9))
#         font = pygame.font.SysFont('Arial', 30)
#
#         while running:
#             color1 = "red"
#
#
#
#
#             screen.fill("White")
#             color = "black"
#
#
#             for i in range(9):
#                 if i == 3 or i == 6:
#                     pygame.draw.line(screen, color, (i*(640/9), 0), (i*(640/9), 512), width = 5)
#                 else:
#                     pygame.draw.line(screen, color, (i * (640 / 9), 0), (i * (640 / 9), 512))
#             for i in range(9):
#                 if i == 3 or i == 6:
#                     pygame.draw.line(screen, color, (0, i*(512/9)), (640, i*(512/9)), width = 5)
#                 else:
#                     pygame.draw.line(screen, color, (0, i * (512 / 9)), (640, i * (512 / 9)))
#             pygame.draw.line(screen, color1, (x1new, y1new), (x1new, y2new), width = 3)
#             pygame.draw.line(screen, color1, (x1new, y1new), (x2new, y1new), width = 3)
#             pygame.draw.line(screen, color1, (x2new, y1new), (x2new, y2new), width = 3)
#             pygame.draw.line(screen, color1, (x1new, y2new), (x2new, y2new), width = 3)
#             count = 0
#             for i in range(1, len(board.get_board())+1):
#                 for j in range(1, len(board.get_board()[0])+1):
#                     if board.get_board()[j-1][i-1] !=0:
#                         text = font.render(str(board.get_board()[j-1][i-1]), True, color1)
#                         screen.blit(text, (((rows[i-1])+35), ((cols[j-1])+28.44)))
#
#
#             pygame.display.flip()
#
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False
#                 elif event.type == pygame.MOUSEBUTTONDOWN:
#                     eventpos = pygame.mouse.get_pos()
#                     x2og = x2new
#                     y2og = y2new
#                     x1og = x1new
#                     y1og = y1new
#                     for i in range(len(rows)):
#                         if rows[i] > eventpos[0]:
#                             x1new = rows[i-1]
#                             x2new = rows[i]
#                             break
#                     for i in range(len(cols)):
#                         if cols[i] > eventpos[1]:
#                             y1new = cols[i-1]
#                             y2new = cols[i]
#                             break
#                 elif event.type == pygame.KEYDOWN:
#
#                     if board.get_board()[translateY(eventpos[1])][translateX(eventpos[0])] == 0:
#
#
                        # if event.key == pygame.K_1:
                        #     if board.is_valid( translateY(eventpos[1]),translateX(eventpos[0]), 1):
                        #         board.board[translateY(eventpos[1])][translateX(eventpos[0])] = 1
                        # elif event.key == pygame.K_2:
                        #     if board.is_valid(translateY(eventpos[1]),translateX(eventpos[0]), 2):
                        #         board.board[translateY(eventpos[1])][translateX(eventpos[0])] = 2
                        # elif event.key == pygame.K_3:
                        #     if board.is_valid(translateY(eventpos[1]),translateX(eventpos[0]), 3):
                        #         board.board[translateY(eventpos[1])][translateX(eventpos[0])] = 3
                        # elif event.key == pygame.K_4:
                        #     if board.is_valid(translateY(eventpos[1]),translateX(eventpos[0]), 4):
                        #         board.board[translateY(eventpos[1])][translateX(eventpos[0])] = 4
                        # elif event.key == pygame.K_5:
                        #     if board.is_valid(translateY(eventpos[1]),translateX(eventpos[0]), 5):
                        #         board.board[translateY(eventpos[1])][translateX(eventpos[0])] = 5
                        # elif event.key == pygame.K_6:
                        #     if board.is_valid(translateY(eventpos[1]),translateX(eventpos[0]), 6):
                        #         board.board[translateY(eventpos[1])][translateX(eventpos[0])] = 6
                        # elif event.key == pygame.K_7:
                        #     if board.is_valid(translateY(eventpos[1]),translateX(eventpos[0]), 7):
                        #         board.board[translateY(eventpos[1])][translateX(eventpos[0])] = 7
                        # elif event.key == pygame.K_8:
                        #     if board.is_valid(translateY(eventpos[1]),translateX(eventpos[0]), 8):
                        #         board.board[translateY(eventpos[1])][translateX(eventpos[0])] = 8
                        # elif event.key == pygame.K_9:
                        #     if board.is_valid(translateY(eventpos[1]),translateX(eventpos[0]), 9):
#                                 board.board[translateY(eventpos[1])][translateX(eventpos[0])] = 9
#
#
#
#
#             pygame.display.flip()
#
#
#
#             clock.tick(60)
#
#     finally:
#         pygame.quit()
#
#
# if __name__ == "__main__":
#     main()

from Sudoku import SudokuGenerator
from Board import Board
from Cell import Cell
import pygame
import random


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
       diff = 'easy'



       running = 'level'
       while running == 'level':
           fontSmall = pygame.font.SysFont('Arial', 30)
           screen.fill("white")
           pygame.draw.rect(screen, (173, 216, 230), (100, 400, 100, 50))
           pygame.draw.rect(screen, (173, 216, 230), (250, 400, 150, 50))
           pygame.draw.rect(screen, (173, 216, 230), (450, 400, 100, 50))
           text = fontSmall.render('EASY', True, 'black')
           screen.blit(text, (100, 400))
           t2 = fontSmall.render('MEDIUM', True, 'black')
           screen.blit(t2, (250, 400))
           t3 = fontSmall.render('HARD', True, 'black')
           screen.blit(t3, (450, 400))
           pygame.display.flip()
           clock.tick(60)

           for event in pygame.event.get():
               if event.type == pygame.MOUSEBUTTONDOWN:
                   if pygame.mouse.get_pos()[0] > 123 and pygame.mouse.get_pos()[0] < 223 and pygame.mouse.get_pos()[1] > 400 and pygame.mouse.get_pos()[1] < 450:
                       diff = 'easy'
                       running = 'game'
                   elif pygame.mouse.get_pos()[0] > 250 and pygame.mouse.get_pos()[0] < 350 and pygame.mouse.get_pos()[1] > 400 and pygame.mouse.get_pos()[0] < 450:
                       diff = 'medium'
                       running = 'game'
                   elif pygame.mouse.get_pos()[0] > 375 and pygame.mouse.get_pos()[0] < 475 and pygame.mouse.get_pos()[1] > 400 and pygame.mouse.get_pos()[1] < 450:
                       diff = 'hard'
                       running = 'game'
               if event.type == pygame.QUIT:
                   pygame.quit()
       board = Board(630, 630, screen, diff)
       while running == 'game':
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   running = False
               if event.type == pygame.MOUSEBUTTONDOWN:
                   eventpos = pygame.mouse.get_pos()
                   board.select(translateX(eventpos[1]), translateX(eventpos[0]))
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
                   elif event.key == pygame.K_RETURN:
                       print('enter')
                       board.currCell.value = board.currCell.sketchedval
                       board.currCell.sketchedval = 0
                   elif event.key == pygame.K_BACKSPACE:
                       if not board.currCell.isOG:
                           board.currCell.value = 0
                           board.currCell.sketchedval = 0


                   # x = pygame.mouse.get_pos()[0]
                   # y = pygame.mouse.get_pos()[1]


           # if selected:
           #     board.select(board.click(x, y)[0], board.click(x, y)[1])
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
