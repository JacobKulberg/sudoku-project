from copy import deepcopy
import pygame

import sudoku_generator
from cell import Cell
from sudoku_generator import SudokuGenerator
class Board:
    #difficulty is gonna be a number, easy = 1, med = 2, hard = 3
    def __init__(self, width, height, screen, difficulty):
        sudoku = SudokuGenerator(9, 20+(difficulty*10))
        sudoku.fill_values()
        self.key = deepcopy(sudoku.get_board())
        sudoku.remove_cells()
        self.vals = sudoku.get_board()

        self.width = width
        self.height = height
        pygame.init()
        # Leave extra room for buttons display below ~ 60
        self.screen = pygame.display.set_mode((width, height+60))
        self.cells = []
        cell_row = []
        for i in range(0,9):
            for j in range(0,9):
                cell_row.append(Cell(self.vals[i][j], i, j, self.screen))
            self.cells.append(cell_row)
            cell_row = []
        self.selected = [0,0]


    def draw(self):
        self.screen.fill((154, 206, 235))
        for i in range(1,10):
            if (i%3) == 0:
                pygame.draw.line(self.screen, (0, 0, 0), (0, i * (self.height / 9)),(self.width, i * (self.height / 9)), 3)
                pygame.draw.line(self.screen, (0, 0, 0), (i * (self.width / 9), 0),(i * (self.width / 9), self.height), 3)
            pygame.draw.line(self.screen, (0, 0, 0), (0, i*(self.height/9)), (self.width, i*(self.height/9)))
            pygame.draw.line(self.screen, (0,0,0), (i*(self.width/9), 0), (i*(self.width/9), self.height))
        for row in self.cells:
            for cell in row:
                cell.draw(self.width, self.height)

        pygame.display.update()

    def select(self, row, col):
        """Marks the cell at (row, col) as selected and deselects others."""
        for r in self.cells:
            for cell in r:
                cell.selected = False
        self.cells[row][col].selected = True
        self.selected = (row, col)

    def click(self, x, y):
        size_x = self.width / 9
        size_y = self.height / 9
        if (x <= self.width) and (y <= self.height):
            for i in range(0, 9):
                if (x <= (i + 1) * size_x) and (x >= i * size_x):
                    col = i
                if (y <= (i + 1) * size_y) and (y >= i * size_y):
                    row = i
            return (row, col)
        return None

    def clear(self):
        #sets cell value of selected cell to 0
        if self.vals[self.selected[0]][self.selected[1]] == 0:
            self.cells[self.selected[0]][self.selected[1]].set_cell_value(0)

    def sketch(self, value):
        # sets sketch value of selected cell to value
        self.cells[self.selected[0]][self.selected[1]].set_sketched_value(value)
        self.cells[self.selected[0]][self.selected[1]].draw(self.width, self.height)
    def place_number(self, value):
        # sets cell value of selected cell to value
        self.cells[self.selected[0]][self.selected[1]].set_cell_value(value)
    def reset_to_original(self):
        for i in range(0, 9):
            for j in range(0, 9):
                self.cells[i][j].set_cell_value(self.key[i][j])
        self.selected = None
    def is_full(self):
        for row in self.cells:
            for cell in row:
                if cell.value == 0 and cell.sketched_value == 0:
                    return False
        return True
    def update_board(self):
        while True:
            for row in self.cells:
                for cell in row:
                    cell.draw(self.width, self.height)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            pygame.display.update()

    def find_empty(self):
        for i in range(0,9):
            for j in range(0,9):
                if self.cells[i][j].value == 0:
                    return (i,j)
    def check_board(self):
        #check if board is solved correctly
        for i in range(0,9):
            for j in range(0,9):
                if self.cells[i][j].sketched_value != 0 and self.cells[i][j].sketched_value != self.key[i][j]:
                    return False
        return True
    def move_selection(self, direction):
        row, col = self.selected

        if direction == "UP" and row > 0:
            row -= 1
        elif direction == "DOWN" and row < 8:
            row += 1
        elif direction == "LEFT" and col > 0:
            col -= 1
        elif direction == "RIGHT" and col < 8:
            col += 1

        # Update the selection
        self.select(row, col)