
def translateX(v):
    if v < 630 / 9 * 1:
        return 0
    elif v < 630 / 9 * 2:
        return 1
    elif v < 630 / 9 * 3:
        return 2
    elif v < 630 / 9 * 4:
        return 3
    elif v < 630 / 9 * 5:
        return 4
    elif v < 630 / 9 * 6:
        return 5
    elif v < 630 / 9 * 7:
        return 6
    elif v < 630 / 9 * 8:
        return 7
    elif v < 630 / 9 * 9:
        return 8



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
    x2new = 70
    y2new = 70
    rows = []
    cols = []
    for i in range(10):
        rows.append(i * (630 / 9))
    for i in range(10):
        cols.append(i * (630 / 9))
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        screen = pygame.display.set_mode((630, 700))
        clock = pygame.time.Clock()
        diff = 'easy'

        running = 'level'
        play = True
        while play:
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
                        if pygame.mouse.get_pos()[0] > 100 and pygame.mouse.get_pos()[0] < 200 and \
                                pygame.mouse.get_pos()[1] > 400 and pygame.mouse.get_pos()[1] < 450:
                            diff = 'easy'
                            running = 'game'
                        elif pygame.mouse.get_pos()[0] > 250 and pygame.mouse.get_pos()[0] < 400 and \
                                pygame.mouse.get_pos()[1] > 400 and pygame.mouse.get_pos()[0] < 450:
                            diff = 'medium'
                            running = 'game'
                        elif pygame.mouse.get_pos()[0] > 450 and pygame.mouse.get_pos()[0] < 550 and \
                                pygame.mouse.get_pos()[1] > 400 and pygame.mouse.get_pos()[1] < 450:
                            diff = 'hard'
                            running = 'game'
                    if event.type == pygame.QUIT:
                        pygame.quit()
            board = Board(630, 630, screen, diff)
            hold = True
            while running == 'game':

                if board.is_full():
                    win = board.check_board()
                    if win:
                        running = 'win'
                    else:
                        running = 'lose'

                if hold == False:
                    break

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pos()[0] > 100 and pygame.mouse.get_pos()[0] < 200 and \
                                pygame.mouse.get_pos()[1] > 640 and pygame.mouse.get_pos()[1] < 690:
                            board.reset_to_original()
                        elif pygame.mouse.get_pos()[0] > 250 and pygame.mouse.get_pos()[0] < 400 and \
                                pygame.mouse.get_pos()[1] > 640 and pygame.mouse.get_pos()[0] < 690:

                            hold = False
                        elif pygame.mouse.get_pos()[0] > 450 and pygame.mouse.get_pos()[0] < 550 and \
                                pygame.mouse.get_pos()[1] > 640 and pygame.mouse.get_pos()[1] < 690:
                            pygame.quit()
                        else:
                            eventpos = pygame.mouse.get_pos()
                            board.select(translateX(eventpos[1]), translateX(eventpos[0]))
                            x2og = x2new
                            y2og = y2new
                            x1og = x1new
                            y1og = y1new
                            for i in range(len(rows)):
                                if rows[i] > eventpos[0]:
                                    x1new = rows[i - 1]
                                    x2new = rows[i]
                                    break
                            for i in range(len(cols)):
                                if cols[i] > eventpos[1]:
                                    y1new = cols[i - 1]
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

                            board.currCell.value = board.currCell.sketchedval
                            board.currCell.sketchedval = 0

                        elif event.key == pygame.K_BACKSPACE:
                            if not board.currCell.isOG:
                                board.currCell.value = 0
                                board.currCell.sketchedval = 0
                        elif event.key == pygame.K_LEFT:
                            if  x1new != 0:
                                x1new = x1new-70
                                x2new = x2new-70
                                board.select(translateX(y1new), translateX(x1new))
                        elif event.key == pygame.K_RIGHT:
                            if x2new != 630:
                                x2new = x2new+70
                                x1new = x1new+70
                                board.select(translateX(y1new), translateX(x1new))
                        elif event.key == pygame.K_UP:
                            if y1new != 0:
                                y1new = y1new-70
                                y2new = y2new-70
                                board.select(translateX(y1new), translateX(x1new))
                        elif event.key == pygame.K_DOWN:
                            if y2new != 630:
                                y2new = y2new+70
                                y1new = y1new+70
                                board.select(translateX(y1new), translateX(x1new))



                        # x = pygame.mouse.get_pos()[0]
                        # y = pygame.mouse.get_pos()[1]

                # if selected:
                #     board.select(board.click(x, y)[0], board.click(x, y)[1])
                screen.fill("pink")
                board.draw()
                pygame.draw.line(screen, 'red', (x1new, y1new), (x1new, y2new), width=3)
                pygame.draw.line(screen, 'red', (x1new, y1new), (x2new, y1new), width=3)
                pygame.draw.line(screen, 'red', (x2new, y1new), (x2new, y2new), width=3)
                pygame.draw.line(screen, 'red', (x1new, y2new), (x2new, y2new), width=3)

                pygame.display.flip()
                clock.tick(60)
            while running == 'win':
                fontSmall = pygame.font.SysFont('Arial', 30)
                screen.fill("white")
                text1 = fontSmall.render('YOU WIN!', True, 'black')
                screen.blit(text1, (200, 300))

                pygame.draw.rect(screen, (173, 216, 230), (250, 400, 150, 50))

                t2 = fontSmall.render('Exit', True, 'black')
                screen.blit(t2, (250, 400))

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:

                        if pygame.mouse.get_pos()[0] > 250 and pygame.mouse.get_pos()[0] < 400 and \
                                pygame.mouse.get_pos()[1] > 400 and pygame.mouse.get_pos()[0] < 450:
                            pygame.quit()

                pygame.display.flip()
                clock.tick(60)

            while running == 'lose':
                fontSmall = pygame.font.SysFont('Arial', 30)
                screen.fill("white")
                text1 = fontSmall.render('YOU LOSE!', True, 'black')
                screen.blit(text1, (200, 300))
                pygame.draw.rect(screen, (173, 216, 230), (100, 400, 100, 50))

                pygame.draw.rect(screen, (173, 216, 230), (450, 400, 100, 50))
                text = fontSmall.render('Restart', True, 'black')
                screen.blit(text, (100, 400))

                t3 = fontSmall.render('Quit', True, 'black')
                screen.blit(t3, (450, 400))

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pos()[0] > 100 and pygame.mouse.get_pos()[0] < 200 and \
                                pygame.mouse.get_pos()[1] > 400 and pygame.mouse.get_pos()[1] < 450:
                            running = 'game'

                        elif pygame.mouse.get_pos()[0] > 450 and pygame.mouse.get_pos()[0] < 550 and \
                                pygame.mouse.get_pos()[1] > 400 and pygame.mouse.get_pos()[1] < 450:
                            pygame.quit()

                pygame.display.flip()
                clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
