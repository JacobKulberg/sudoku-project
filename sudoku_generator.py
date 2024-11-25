import math, random
import pygame
import random
import os
from sudoku import *

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""


class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''

    def __init__(self):
        '''
        Returns a 2D python list of numbers which represents the board

        Parameters: None
        Return: list[list]
        '''
        self.row_length = 9
        self.box_length = self.row_length // 3
        self.board = self.get_board()
        self.fullboard = self.get_board()
        self.baseboard = self.board

    def get_board(self):
        board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        return board

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''

    def print_board(self):
        print(self.board)

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row

	Return: boolean
    '''

    def valid_in_row(self, row, num):
        self.row = row
        self.num = num
        if num in row:
            return False
        else:
            return True

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column

	Return: boolean
    '''

    def valid_in_col(self, col, num):

        column_values = [self.board[row][col] for row in range(len(self.board))]
        return num not in column_values

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''

    def valid_in_box(self, row_start, col_start, num, board):

        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                if board[row][col] == num:
                    return False
        return True

    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''

    def is_valid(self, row, col, num):
        # Row Check
        if num in self.board[row]:
            return False

        # Column Check
        if num in [self.board[i][col] for i in range(9)]:
            return False

        # 3 by 3 Grid Check
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for r in range(row_start, row_start + 3):
            for c in range(col_start, col_start + 3):
                if self.board[r][c] == num:
                    return False

        return True

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''

    def fill_box(self, row_start, col_start):
        for r in range(row_start, row_start + 3):
            for c in range(col_start, col_start + 3):
                num = random.randint(1,9)
                if self.valid_in_box(row_start, col_start, num, self.board):
                    self.board[r][c] = num
                else:
                    while True:
                        num = random.randint(1,9)
                        if self.valid_in_box(row_start, col_start, num, self.board):
                            self.board[r][c] = num
                            break
        return self.board

    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''

    def fill_diagonal(self):
        for i in range(0, self.row_length, 3):
            self.fill_box(i, i)

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled

	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called

    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''

    def remove_cells(self, difficulty):
        difficulty_levels = {
            "Easy": 30,
            "Medium": 40,
            "Hard": 50
        }
        amtRemoved = difficulty_levels.get(self.remove_cells, difficulty_levels[difficulty])
        
        cells = [(row, col) for row in range(9) for col in range(9)]
        cells_to_remove = random.sample(cells, amtRemoved)

        for row, col in cells_to_remove:
            self.board[row][col] = 0

    def check_win(self):
        for i in range(self.row_length):
            nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            for j in range(self.row_length):
                if self.board[i][j] in nums:
                    nums.remove(self.board[i][j])
            if len(nums) != 0:
                return False

        for j in range(self.row_length):
            nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            for i in range(self.row_length):
                if self.board[i][j] in nums:
                    nums.remove(self.board[i][j])
            if len(nums) != 0:
                return False

        for i in range(0, self.row_length, 3):
            for j in range(0, self.row_length, 3):
                nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        if self.board[r][c] in nums:
                            nums.remove(self.board[r][c])
                if len(nums) != 0:
                    return False

        return True


'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board


def display_start(screen):
    width = 64 * 9
    height = 64 * 10

    current_dir = os.path.dirname(__file__)
    image_path = os.path.join(current_dir, "assets","Sodoku_Start_Screen.png")
    
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found at {image_path}")
    # screen.fill((255, 255, 245))
    background_image = pygame.image.load(image_path)
    background_image = pygame.transform.scale(background_image, (width, height))
    screen.blit(background_image, (0, 0))

    big_font = pygame.font.Font(None, 80)
    small_font = pygame.font.Font(None, 50)

    start_surf = big_font.render("Welcome to Sodoku", 0, (128,0,0))
    start_rect = start_surf.get_rect(center=(width // 2, height // 2 - 175))
    screen.blit(start_surf, start_rect)

    select_surf = small_font.render("Select Game Mode:", 0, "black")
    select_rect = select_surf.get_rect(center=(width // 2, height // 2 - 40))
    screen.blit(select_surf, select_rect)

    button_width = 120
    button_height = 50
    gap = 20
    button_x_start = (width - (3* button_width + 2 * gap)) // 2
    button_y = height // 2 + 50

    button_colors = {"easy": (200,255,200), "medium": (255,255,200), "hard": (255,200,200)}
    button_texts = ["Easy", "Medium", "Hard"]
    buttons = []

    for i, text in enumerate(button_texts):
        x = button_x_start + i * (button_width + gap)
        button_rect = pygame.Rect(x, button_y, button_width, button_height)
        buttons.append((button_rect, text))
        pygame.draw.rect(screen, button_colors[text.lower()], button_rect)
        button_surf = small_font.render(text, True, "black")
        button_rect_text = button_surf.get_rect(center=button_rect.center)
        screen.blit(button_surf, button_rect_text)
    return buttons



def game_over(screen):
    width = 64 * 9
    height = 64 * 10

    button_width = 120
    button_height = 50
    gap = 20
    button_x_start = (width - (3* button_width + 2 * gap)) // 2
    button_y = height // 2 + 50

    current_dir = os.path.dirname(__file__)
    image_path = os.path.join(current_dir, "assets","Sodoku_Start_Screen.png")
    
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found at {image_path}")
    # screen.fill((255, 255, 245))
    background_image = pygame.image.load(image_path)
    background_image = pygame.transform.scale(background_image, (width, height))
    screen.blit(background_image, (0, 0))

    big_font = pygame.font.Font(None, 80)
    small_font = pygame.font.Font(None, 50)

    start_surf = big_font.render("Game Over :(", 0, (128,0,0))
    start_rect = start_surf.get_rect(center=(width // 2, height // 2 - 175))
    screen.blit(start_surf, start_rect)

    button_color = (153,101,21)
    button_text = "Restart"
    

   
    x = (width - button_width) // 2
    y = (height - button_height) // 2

    button_rect = pygame.Rect(x, y, button_width, button_height)

    pygame.draw.rect(screen, button_color, button_rect)

    pygame.draw.rect(screen, button_color, button_rect)
    button_surf = small_font.render(button_text, True, "White")
    button_rect_text = button_surf.get_rect(center=button_rect.center)
    screen.blit(button_surf, button_rect_text)

    return button_rect


def game_win(screen):
    width = 64 * 9
    height = 64 * 10

    button_width = 120
    button_height = 50
    gap = 20
    button_x_start = (width - (3 * button_width + 2 * gap)) // 2
    button_y = height // 2 + 50

    current_dir = os.path.dirname(__file__)
    image_path = os.path.join(current_dir, "assets", "Sodoku_Start_Screen.png")

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found at {image_path}")
    # screen.fill((255, 255, 245))
    background_image = pygame.image.load(image_path)
    background_image = pygame.transform.scale(background_image, (width, height))
    screen.blit(background_image, (0, 0))

    big_font = pygame.font.Font(None, 80)
    small_font = pygame.font.Font(None, 50)

    start_surf = big_font.render("Game Won!", 0, (128, 0, 0))
    start_rect = start_surf.get_rect(center=(width // 2, height // 2 - 175))
    screen.blit(start_surf, start_rect)

    button_color = (153, 101, 21)
    button_text = "Exit"

    x = (width - button_width) // 2
    y = (height - button_height) // 2

    button_rect = pygame.Rect(x, y, button_width, button_height)

    pygame.draw.rect(screen, button_color, button_rect)

    pygame.draw.rect(screen, button_color, button_rect)
    button_surf = small_font.render(button_text, True, "White")
    button_rect_text = button_surf.get_rect(center=button_rect.center)
    screen.blit(button_surf, button_rect_text)

    return button_rect

def game_in_progress(screen):
    width = 64 * 9
    height = 64 * 10

    small_font = pygame.font.Font(None, 50)

    button_width = 120
    button_height = 50
    gap = 20
    button_x_start = (width - (3 * button_width + 2 * gap)) // 2
    button_y =  584

    button_color = (153, 101, 21)
    button_texts = ["Reset", "Restart", "Exit"]
    buttons = []

    for i, text in enumerate(button_texts):
        x = button_x_start + i * (button_width + gap)
        button_rect = pygame.Rect(x, button_y, button_width, button_height)
        buttons.append((button_rect, text))
        pygame.draw.rect(screen, button_color, button_rect)
        button_surf = small_font.render(text, True, "white")
        button_rect_text = button_surf.get_rect(center=button_rect.center)
        screen.blit(button_surf, button_rect_text)
    return buttons
