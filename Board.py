import pygame

from Cell import Cell

from Sudoku import SudokuGenerator


class Board:

    def __init__(self, width=630, height=700, screen=None, difficulty='easy'):

        self.screen = screen
        self.width = width
        self.height = height
        if difficulty == 'easy':
            self.difficulty = 1
        elif difficulty == 'medium':
            self.difficulty = 40
        elif difficulty == 'hard':
            self.difficulty = 50
        self.currCell = None
        self.board = SudokuGenerator(9, self.difficulty)
        self.board.fill_values()
        self.board.remove_cells()
        self.lst = []
        for i in range(9):
            self.lst.append([])
            for j in range(9):
                if self.board.get_board()[i][j] == 0:
                    self.lst[i].append(Cell(self.board.get_board()[i][j], i, j, self.screen, False))
                else:
                    self.lst[i].append(Cell(self.board.get_board()[i][j], i, j, self.screen, True))


    def draw(self):

        for i in range(9):
            if i == 3 or i == 6:
                pygame.draw.line(self.screen, 'black', (i * (630 / 9), 0), (i * (630 / 9), 630), width=5)
            else:
                pygame.draw.line(self.screen, 'black', (i * (630 / 9), 0), (i * (630 / 9), 630))
        for i in range(9):
            if i == 3 or i == 6:
                pygame.draw.line(self.screen, 'black', (0, i * (630 / 9)), (630, i * (630 / 9)), width=5)
            else:
                pygame.draw.line(self.screen, 'black', (0, i * (630 / 9)), (630, i * (630 / 9)))
        pygame.draw.line(self.screen, 'black', (0, 630), (630, 630), width=5)
        for i in range(9):
            for j in range(9):
                self.lst[j][i].draw()
        fontSmall = pygame.font.SysFont('Arial', 30)
        pygame.draw.rect(self.screen, (173, 216, 230), (100, 640, 100, 50))
        pygame.draw.rect(self.screen, (173, 216, 230), (250, 640, 150, 50))
        pygame.draw.rect(self.screen, (173, 216, 230), (450, 640, 100, 50))
        text = fontSmall.render('RESET', True, 'black')
        self.screen.blit(text, (100, 640))
        t2 = fontSmall.render('RESTART', True, 'black')
        self.screen.blit(t2, (250, 640))
        t3 = fontSmall.render('EXIT', True, 'black')
        self.screen.blit(t3, (450, 640))

    def click(self, x, y):

        if x < 630 / 9 * 1:
            v1 = 0
        elif x < 630 / 9 * 2:
            v1 = 1
        elif x < 630 / 9 * 3:
            v1 = 2
        elif x < 630 / 9 * 4:
            v1 = 3
        elif x < 630 / 9 * 5:
            v1 = 4
        elif x < 630 / 9 * 6:
            v1 = 5
        elif x < 630 / 9 * 7:
            v1 = 6
        elif x < 630 / 9 * 8:
            v1 = 7
        elif x < 730 / 9 * 9:
            v1 = 8
        else:
            return None

        if y < 630 / 9 * 1:
            v2 = 0
        elif y < 630 / 9 * 2:
            v2 = 1
        elif y < 630 / 9 * 3:
            v2 = 2
        elif y < 630 / 9 * 4:
            v2 = 3
        elif y < 630 / 9 * 5:
            v2 = 4
        elif y < 630 / 9 * 6:
            v2 = 5
        elif y < 630 / 9 * 7:
            v2 = 6
        elif y < 630 / 9 * 8:
            v2 = 7
        elif y < 730 / 9 * 9:
            v2 = 8
        else:
            return None

        return v1, v2

    def select(self, x, y):

        self.currCell = self.lst[x][y]
        x1 = x * 70
        x2 = (x+1)*70
        y1 = y * 7
        y2 = (y+1)*70
        pygame.draw.line(self.screen, 'red', (x1, y1), (x, y2), width=3)
        pygame.draw.line(self.screen, 'red', (x1, y1), (x2, y1), width=3)
        pygame.draw.line(self.screen, 'red', (x2, y1), (x2, y2), width=3)
        pygame.draw.line(self.screen, 'red', (x1, y2), (x2, y2), width=3)

    def clear(self):
        if not self.currCell.isOG:
            self.currCell.set_cell_value(0)
            self.board.board()[self.currCell.x][self.currCell.y] = 0

    def sketch(self, value):
        if not self.currCell.isOG:
            self.currCell.set_sketched_value(value)

    def place_number(self, value):
        if not self.currCell.isOG:
            self.currCell.set_cell_value(value)
            self.board.get_board()[self.currCell.x][self.currCell.y] = value

    def reset_to_original(self):
        for i in range(9):
            for j in range(9):
                if not self.lst[i][j].isOG:
                    self.lst[i][j].set_cell_value(0)
                    self.board.board[i][j] = 0

    def is_full(self):
        for i in range(9):
            for j in range(9):
                if self.lst[i][j].value == 0:
                    return False
        return True

    def check_board(self):
        for i in range(9):
            for j in range(9):
                self.board.board[i][j] = self.lst[i][j].value
        Hold = True


        for i in range(9):
            row = set()
            for j in range(9):
                if self.board.board[i][j] not in row:
                    row.add(self.board.board[i][j])
            if len(row) != 9:
                return False


        for i in range(9):
            col = set()
            for j in range(9):
                if self.board.board[j][i] not in col:
                    col.add(self.board.board[j][i])
            if len(col) != 9:
                return False

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = set()
                for i in range(3):
                    for j in range(3):
                        value = self.board.board[box_row + i][box_col + j]
                        if value not in box:
                            box.add(value)
                if len(box) != 9:
                    return False
        return True



