import pygame, sys
from sudoku_generator import *
import copy

#some rgb colors
bg = (239, 235, 216)
bg_contrast = (31, 30, 28)

#initializing pygame window
pygame.init()
screen = pygame.display.set_mode((720, 790))
pygame.display.set_caption("Sudoku")

# Difficulty settings: number of cells to remove per level
DIFFICULTY_LEVELS = {
    'easy': 30,
    'medium': 40,
    'hard': 50
}

# Font for rendering numbers on the grid
def get_number_font():
    return pygame.font.SysFont("comicsans", 40)

def generate_puzzle(difficulty):
    """
    Generates a Sudoku puzzle and its solution based on difficulty.

    Parameters:
        difficulty (str): 'easy', 'medium', or 'hard'

    Returns:
        tuple: (puzzle_board, solution_board) as 2D lists
    """
    removed = DIFFICULTY_LEVELS.get(difficulty, DIFFICULTY_LEVELS['easy'])
    sudoku = SudokuGenerator(9, removed)
    sudoku.fill_values()
    solution = copy.deepcopy(sudoku.get_board())
    sudoku.remove_cells()
    puzzle = sudoku.get_board()
    return puzzle, solution

#draw the grid lines
def grids():
    #light lines
    for i in range(1, 9):
        #horizontals
        pygame.draw.line(screen, bg_contrast, (0, i * 80), (720, i * 80))
        #verticals
        pygame.draw.line(screen, bg_contrast, (i * 80, 0), (i * 80, 720))
    #heavy/box lines
    for i in range(1, 3):
        pygame.draw.line(screen, bg_contrast, (0, i * 240), (720, i * 240), 3)
        pygame.draw.line(screen, bg_contrast, (i * 240, 0), (i * 240, 720), 3)

#initializing a sudoku board and saving the solution
sudoku = SudokuGenerator(9, 0)
sudoku.fill_values()
solution = sudoku.get_board()

#you get the idea
def start_screen():
    #creating font
    tit_font = pygame.font.SysFont("comicsans", 120, True)
    button_font = pygame.font.SysFont("comicsans", 70)

    screen.fill(bg)

    #rendering the text onto surfaces
    tit_text = tit_font.render("Sudoku", False, bg_contrast)
    start_text = button_font.render("Start", False, bg)
    exit_text = button_font.render(" Exit ", False, bg)

    #creating surfaces
    tit_surf = tit_text.get_rect(center = (720//2, 790//2 - 150))
    start_surface = pygame.Surface((start_text.get_size()[0] + 20, start_text.get_size()[1] + 20))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 25, exit_text.get_size()[1] + 20))

    #coloring buttons hehe
    start_surface.fill(bg_contrast)
    exit_surface.fill(bg_contrast)

    #blitting stuff
    screen.blit(tit_text, tit_surf)
    start_surface.blit(start_text, (10, 10))
    exit_surface.blit(exit_text, (10,10))

    #making those buttons
    start_rect = start_surface.get_rect(center = (720//2, 790//2 + 30))
    exit_rect = exit_surface.get_rect(center = (720//2, 790//2 + 170))
    screen.blit(start_surface, start_rect)
    screen.blit(exit_surface, exit_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(event.pos):
                    return
                elif exit_rect.collidepoint(event.pos):
                    sys.exit()
        pygame.display.update()





# hype moments and aura
if __name__ == '__main__':
    # Prompt for difficulty level
    difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
    puzzle_board, solution = generate_puzzle(difficulty)

    # Show start screen
    start_screen()

    number_font = get_number_font()

    # Main game loop
    while True:
        screen.fill(bg)
        grids()

        # Render puzzle numbers
        for r in range(9):
            for c in range(9):
                value = puzzle_board[r][c]
                if value != 0:
                    text_surf = number_font.render(str(value), True, bg_contrast)
                    text_rect = text_surf.get_rect(center=(c * 80 + 40, r * 80 + 40))
                    screen.blit(text_surf, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # TODO: handle user input for selecting and filling cells

        pygame.display.update()