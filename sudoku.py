import pygame, sys
from sudoku_generator import *
import copy

# width and height constants
WIDTH = 720
HEIGHT = 720
CELL_LENGTH = WIDTH // 9
BOX_LENGTH = WIDTH // 3
SIDE_WIDTH = 300
SCREEN_WIDTH = WIDTH + SIDE_WIDTH
SCREEN_HEIGHT = HEIGHT + 2

#some rgb colors
bg = (239, 235, 216)
bg_contrast = (31, 30, 28)
baby_blue = (180, 180, 255)
big_blue = (51, 51, 153)
acid = (255, 245, 0)
pastl = (144, 238, 144)
soft_red = (255, 127, 127)

#initializing pygame window
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sudoku")
board_screen = pygame.Surface((WIDTH, HEIGHT))
screen.blit(board_screen, (0, 0))

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
    initial = copy.deepcopy(sudoku.get_board())
    return puzzle, solution, initial

# menu options
def menu():
    menu_font = pygame.font.SysFont("comicsans", 30)
    reset_text = menu_font.render("RESET", True, bg)
    restart_text = menu_font.render("RESTART", True, bg)
    exit_text = menu_font.render("EXIT", True, bg)
    reset_surf = pygame.Surface((reset_text.get_size()[0] + 110, reset_text.get_size()[1] - 10))
    restart_surf = pygame.Surface((restart_text.get_size()[0] + 68, restart_text.get_size()[1] - 10))
    exit_surf = pygame.Surface((exit_text.get_size()[0] + 131, exit_text.get_size()[1] - 10))
    reset_surf.fill(bg_contrast)
    restart_surf.fill(bg_contrast)
    exit_surf.fill(bg_contrast)
    reset_surf.blit(reset_text, (55, -5))
    restart_surf.blit(restart_text, (34, -5))
    exit_surf.blit(exit_text, (65.5, -5))
    reset_rect = reset_surf.get_rect(center=(SCREEN_WIDTH - 150, SCREEN_HEIGHT // 2))
    restart_rect = restart_surf.get_rect(center=(SCREEN_WIDTH - 150, SCREEN_HEIGHT / 2 + 100))
    exit_rect = exit_surf.get_rect(center=(SCREEN_WIDTH - 150, SCREEN_HEIGHT // 2 + 200))
    screen.blit(reset_surf, reset_rect)
    screen.blit(restart_surf, restart_rect)
    screen.blit(exit_surf, exit_rect)
    return reset_rect, restart_rect, exit_rect

#draw the grid lines
def grids():
    #light lines
    for i in range(1, 9):
        #horizontals
        pygame.draw.line(screen, bg_contrast, (0, i * CELL_LENGTH), (WIDTH, i * CELL_LENGTH))
        #verticals
        pygame.draw.line(screen, bg_contrast, (i * CELL_LENGTH, 0), (i * CELL_LENGTH, HEIGHT))

    # heavy/box lines
    for i in range(4):
        pygame.draw.line(screen, bg_contrast, (0, i * BOX_LENGTH), (WIDTH, i * BOX_LENGTH), 3)
        pygame.draw.line(screen, bg_contrast, (i * BOX_LENGTH, 0), (i * BOX_LENGTH, HEIGHT), 3)

# Draw numbers
def draw_numbers():
    for r in range(9):
        for c in range(9):
            val = puzzle_board[r][c]
            if val != 0:
                color = bg_contrast if initial[r][c] == val else big_blue
                surf = number_font.render(str(val), True, color)
                rect = surf.get_rect(
                    center=(c * CELL_LENGTH + CELL_LENGTH // 2, r * CELL_LENGTH + CELL_LENGTH // 2))
                screen.blit(surf, rect)

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
        if x >= WIDTH or y >= HEIGHT:
            return None
        row = y // (WIDTH//9)
        col = x // (WIDTH//9)
        return row, col

#checks if all cells on the board has been filled
def check_if_full(board):
    for i in board:
        for j in i:
            if j == 0:
                return False
    return True
#checks if the game has been won
def check_if_win(solution_board, played_board):
    for row in range(len(played_board)):
        for col in range(len(played_board)):
            if played_board[row][col] != solution_board[row][col]:
                return False
    return True
#draws game over thing
def draw_game_over(win):
    wl_font = pygame.font.SysFont("comicsans", 45)
    wl = "GAME WON!" if win else "GAME LOST."
    wlc = pastl if win else soft_red
    w_text = wl_font.render(wl, True, wlc)
    wl_surf = pygame.Surface((w_text.get_size()[0] + 10, w_text.get_size()[1] + 10))
    wl_surf.fill(bg_contrast)
    wl_surf.blit(w_text, (5, 5))
    wl_rect = wl_surf.get_rect(center=(SCREEN_WIDTH - 150, SCREEN_HEIGHT // 2 - 150))
    screen.blit(wl_surf, wl_rect)
#a little coloring animation that fills the board with green if you win and red if you lose
def color_animate(win):
    color = pastl if win else soft_red

    for i in range(1, 10, 2):
        coloring_surf = pygame.Surface((CELL_LENGTH * i, CELL_LENGTH * i))
        coloring_surf.fill(color)
        coloring_rect = coloring_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        board_screen.fill(bg)
        screen.blit(coloring_surf, coloring_rect)
        grids()
        draw_numbers()
        pygame.time.delay(200)
        pygame.display.update()



# hype moments and aura
if __name__ == '__main__':
    start = True

    while True:
        if start:
            game_over = False
            difficulty = start_screen()
            puzzle_board, solution, initial = generate_puzzle(difficulty)
            number_font = get_number_font()
            res, rst, ex = menu()
            selected_tile = (0, 0)
            temp_input = None  # stores number before ENTER
            start = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if res.collidepoint(event.pos):
                    puzzle_board = copy.deepcopy(initial)
                    temp_input = None
                    if game_over:
                        selected_tile = (0, 0)
                        game_over = False
                elif rst.collidepoint(event.pos):
                    start = True
                elif ex.collidepoint(event.pos):
                    sys.exit()
                elif not game_over:
                    pos = get_tile_pos(event.pos)
                    if pos:
                        selected_tile = pos
                        temp_input = None
            if event.type == pygame.KEYDOWN and not game_over:
                if selected_tile:
                    r, c = selected_tile
                    if event.key == pygame.K_UP:
                        selected_tile = ((r - 1) % 9, c)
                        temp_input = None
                    elif event.key == pygame.K_DOWN:
                        selected_tile = ((r + 1) % 9, c)
                        temp_input = None
                    elif event.key == pygame.K_LEFT:
                        selected_tile = (r, (c - 1) % 9)
                        temp_input = None
                    elif event.key == pygame.K_RIGHT:
                        selected_tile = (r, (c + 1) % 9)
                        temp_input = None
                    elif event.unicode != '' and event.unicode in '123456789' and initial[r][c] == 0:
                        temp_input = int(event.unicode)
                    elif event.key == pygame.K_RETURN and temp_input is not None:
                        if initial[r][c] == 0:
                            puzzle_board[r][c] = temp_input
                            if check_if_full(puzzle_board):
                                game_over = True
                                selected_tile = None
                                win_state = check_if_win(solution, puzzle_board)
                                wl_color = pastl if game_over else soft_red
                                draw_game_over(win_state)
                                color_animate(win_state)
                        temp_input = None

        # Rendering
        if not game_over:
            screen.fill(bg)
            grids()
            menu()

        # Highlight selected cell
        if selected_tile:
            r, c = selected_tile
            highlight = pygame.Surface((CELL_LENGTH - 1, CELL_LENGTH - 1))
            highlight.fill(baby_blue)
            screen.blit(highlight, (c * CELL_LENGTH + 1, r * CELL_LENGTH + 1))
            grids()

        if not game_over:
            draw_numbers()

        # Draw temp input
        if selected_tile and temp_input and not game_over:
            r, c = selected_tile
            surf = number_font.render(str(temp_input), True, acid)
            rect = surf.get_rect(center=(c * CELL_LENGTH + CELL_LENGTH // 2, r * CELL_LENGTH + CELL_LENGTH // 2))
            screen.blit(surf, rect)

        pygame.display.update()