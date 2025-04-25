import pygame, sys
from sudoku_generator import *
import copy

# width and height constants
WIDTH = 726
HEIGHT = 726
SIDE_WIDTH = 300
SCREEN_WIDTH = WIDTH + SIDE_WIDTH
SCREEN_HEIGHT = HEIGHT + 2

#some rgb colors
bg = (239, 235, 216)
bg_contrast = (31, 30, 28)

#initializing pygame window
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sudoku")
start = True

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
    screen.fill(bg)
    #light lines
    for i in range(1, 9):
        #horizontals
        pygame.draw.line(screen, bg_contrast, (0, i * WIDTH // 9), (WIDTH, i * WIDTH // 9))
        #verticals
        pygame.draw.line(screen, bg_contrast, (i * WIDTH // 9, 0), (i * WIDTH // 9, WIDTH))

    #heavy/box lines
    for i in range(4):
        pygame.draw.line(screen, bg_contrast, (0, i * WIDTH // 3), (WIDTH, i * WIDTH // 3), 3)
        pygame.draw.line(screen, bg_contrast, (i * WIDTH // 3, 0), (i * WIDTH // 3, WIDTH), 3)

    #menu options
    menu_font = pygame.font.SysFont("comicsans", 30)
    reset_text = menu_font.render("RESET", True, bg)
    menu_text = menu_font.render("MENU", True, bg)
    exit_text = menu_font.render("EXIT", True, bg)
    reset_surf = pygame.Surface((reset_text.get_size()[0] + 110, reset_text.get_size()[1] - 10))
    menu_surf = pygame.Surface((menu_text.get_size()[0] + 119, menu_text.get_size()[1] - 10))
    exit_surf = pygame.Surface((exit_text.get_size()[0] + 131, exit_text.get_size()[1] - 10))
    reset_surf.fill(bg_contrast)
    menu_surf.fill(bg_contrast)
    exit_surf.fill(bg_contrast)
    reset_surf.blit(reset_text, (55, -5))
    menu_surf.blit(menu_text, (59.5, -5))
    exit_surf.blit(exit_text, (65.5, -5))
    reset_rect = reset_surf.get_rect(center = (SCREEN_WIDTH - 150, SCREEN_HEIGHT// 2 - 100))
    menu_rect = menu_surf.get_rect(center = (SCREEN_WIDTH - 150, SCREEN_HEIGHT/2))
    exit_rect = exit_surf.get_rect(center = (SCREEN_WIDTH -150, SCREEN_HEIGHT//2 + 100))
    screen.blit(reset_surf, reset_rect)
    screen.blit(menu_surf, menu_rect)
    screen.blit(exit_surf, exit_rect)
    return reset_rect, menu_rect, exit_rect



#you get the idea
def start_screen():
    #creating font
    subtit_font = pygame.font.SysFont("comicsans", 25)
    tit_font = pygame.font.SysFont("comicsans", 95, True)
    button_font = pygame.font.SysFont("comicsans", 50)

    screen.fill(bg)

    #rendering the text
    subtit_text = subtit_font.render("WELCOME TO...", True, bg_contrast)
    tit_text = tit_font.render("SUDOKU!", True, bg_contrast)
    start_text = button_font.render("START", True, bg)
    exit_text = button_font.render("EXIT", True, bg)

    #creating buttons
    subtit_surf = subtit_text.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 200))
    tit_surf = tit_text.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 150))
    start_surface = pygame.Surface((start_text.get_size()[0] + 20, start_text.get_size()[1] + 10))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 63, exit_text.get_size()[1] + 10))

    #coloring buttons hehe
    start_surface.fill(bg_contrast)
    exit_surface.fill(bg_contrast)

    #blitting stuff
    screen.blit(subtit_text, subtit_surf)
    screen.blit(tit_text, tit_surf)
    start_surface.blit(start_text, (10, 5))
    exit_surface.blit(exit_text, (31.5, 5))

    #making surfaces for those buttons
    start_rect = start_surface.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30))
    exit_rect = exit_surface.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 170))
    screen.blit(start_surface, start_rect)
    screen.blit(exit_surface, exit_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(event.pos):
                    return select_difficulty()
                elif exit_rect.collidepoint(event.pos):
                    sys.exit()
        pygame.display.update()

def select_difficulty():
    # creating font
    tit_font = pygame.font.SysFont("comicsans", 60, True)
    button_font = pygame.font.SysFont("comicsans", 45)
    back_font = pygame.font.SysFont("comicsans", 30)

    screen.fill(bg)

    # rendering the text
    tit_text = tit_font.render("SELECT DIFFICULTY:", True, bg_contrast)
    easy_difficulty_text = button_font.render("EASY", True, bg)
    medium_difficulty_text = button_font.render("MEDIUM", True, bg)
    hard_difficulty_text = button_font.render("HARD", True, bg)
    back_text = back_font.render("BACK", True, bg)

    # creating buttons
    tit_surf = tit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 140))
    easy_difficulty_surface = pygame.Surface((easy_difficulty_text.get_size()[0] + 98, easy_difficulty_text.get_size()[1] + 10))
    medium_difficulty_surface = pygame.Surface((medium_difficulty_text.get_size()[0] + 20, medium_difficulty_text.get_size()[1] + 10))
    hard_difficulty_surface = pygame.Surface((hard_difficulty_text.get_size()[0] + 90, hard_difficulty_text.get_size()[1] + 10))
    back_surface = pygame.Surface((back_text.get_size()[0] + 10, back_text.get_size()[1] + 10))

    # coloring buttons
    easy_difficulty_surface.fill(bg_contrast)
    medium_difficulty_surface.fill(bg_contrast)
    hard_difficulty_surface.fill(bg_contrast)
    back_surface.fill(bg_contrast)

    # blitting stuff
    screen.blit(tit_text, tit_surf)
    easy_difficulty_surface.blit(easy_difficulty_text, (49, 5))
    medium_difficulty_surface.blit(medium_difficulty_text, (10, 5))
    hard_difficulty_surface.blit(hard_difficulty_text, (45, 5))
    back_surface.blit(back_text, (5, 5))

    # making surfaces for those buttons
    easy_difficulty_rect = easy_difficulty_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30))
    medium_difficulty_rect = medium_difficulty_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 140))
    hard_difficulty_rect = hard_difficulty_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 250))
    back_rect = back_surface.get_rect(center = (50, 33))
    screen.blit(easy_difficulty_surface, easy_difficulty_rect)
    screen.blit(medium_difficulty_surface, medium_difficulty_rect)
    screen.blit(hard_difficulty_surface, hard_difficulty_rect)
    screen.blit(back_surface, back_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_difficulty_rect.collidepoint(event.pos):
                    return "easy"
                elif medium_difficulty_rect.collidepoint(event.pos):
                    return "medium"
                elif hard_difficulty_rect.collidepoint(event.pos):
                    return "hard"
                elif back_rect.collidepoint(event.pos):
                    return start_screen()
        pygame.display.update()

# Mouse click selects tile
def get_tile_pos(mouse_pos):
        x, y = mouse_pos
        if x >= WIDTH:
            return None
        row = y // (WIDTH//9)
        col = x // (WIDTH//9)
        return row, col

# hype moments and aura
if __name__ == '__main__':

    # Main game loop
    while True:
        if start:
            # Show start screen and difficulty selection
            difficulty = start_screen()

            res, men, ex = grids()

            puzzle_board, solution = generate_puzzle(difficulty)

            number_font = get_number_font()

            selected_tile = None

            # Render puzzle numbers
            for r in range(9):
                for c in range(9):
                    value = puzzle_board[r][c]
                    if value != 0:
                        text_surf = number_font.render(str(value), True, bg_contrast)
                        text_rect = text_surf.get_rect(center=(c * WIDTH//9 + 40, r * WIDTH//9 + 40))
                        screen.blit(text_surf, text_rect)
            start = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if men.collidepoint(event.pos):
                    start = True
                elif ex.collidepoint(event.pos):
                    sys.exit()
                else:
                    pos = get_tile_pos(event.pos)
                    if pos:
                        selected_tile = pos
            if event.type == pygame.KEYDOWN:
                if selected_tile and event.unicode in '123456789':
                    r, c = selected_tile
                    if puzzle_board[r][c] == 0:
                        puzzle_board[r][c] = int(event.unicode)
                        
        #Updates board with user input
        grids()
        if selected_tile:
            r, c = selected_tile
            pygame.draw.rect(screen, (180, 180, 255),
                             pygame.Rect(c * WIDTH // 9, r * WIDTH // 9, WIDTH // 9, WIDTH // 9))
        for r in range(9):
            for c in range(9):
                value = puzzle_board[r][c]
                if value != 0:
                    text_surf = number_font.render(str(value), True, bg_contrast)
                    text_rect = text_surf.get_rect(center=(c * WIDTH // 9 + 40, r * WIDTH // 9 + 40))
                    screen.blit(text_surf, text_rect)

        pygame.display.update()
