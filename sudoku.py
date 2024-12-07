import pygame, sys
from board import Board
from sudoku_generator import SudokuGenerator

WIDTH = 540
HEIGHT = 600
BG_COLOR = (255, 255, 245)
NUM_COLOR = (171, 176, 172)
PINK = (255, 192, 203)
GRAY = (168, 168, 168)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def draw_buttons(screen, font):
    pygame.draw.rect(screen, (100, 0, 0), (80, 400, 120, 40), 4)
    surface = font.render("EASY", 0, BLACK)
    screen.blit(surface, surface.get_rect(center=(140, 420)))

    pygame.draw.rect(screen, (100, 0, 0), (260, 400, 120, 40), 4)
    surface = font.render("MEDIUM", 0, BLACK)
    screen.blit(surface, surface.get_rect(center=(320, 420)))

    pygame.draw.rect(screen, (100, 0, 0), (440, 400, 120, 40), 4)
    surface = font.render("HARD", 0, BLACK)
    screen.blit(surface, surface.get_rect(center=(500, 420)))

def start_screen(screen):
    """Displays the start screen where the user selects difficulty."""
    screen.fill(BG_COLOR)
    font = pygame.font.Font(None, 50)
    text = font.render("Welcome to Sudoku", 0, BLACK)
    font = pygame.font.Font(None, 40)

    game_mode_text = font.render("Select Game Mode:", 0, BLACK)
    game_mode_text_rect = game_mode_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(game_mode_text, game_mode_text_rect)

    draw_buttons(screen, font)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 80 <= x <= 200 and 400 <= y <= 440:
                    return 1  # Easy
                elif 260 <= x <= 380 and 400 <= y <= 440:
                    return 2  # Medium
                elif 440 <= x <= 560 and 400 <= y <= 440:
                    return 3  # Hard

def game_over_screen(screen, win):
    """Displays the game over screen with success or failure message."""
    screen.fill(BG_COLOR)
    font = pygame.font.Font(None, 50)

    if win:
        message = font.render("Game Won!", 0, BLACK)
    else:
        message = font.render("Game Over :(", 0, BLACK)

    message_rect = message.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(message, message_rect)
    pygame.display.flip()


def main():
    """Main function to run the game."""
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    difficulty = start_screen(screen)

    board = Board(WIDTH, WIDTH, screen, difficulty)

    running = True
    while running:
        screen.fill(BG_COLOR)
        board.draw()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                clicked_cell = board.click(x, y)
                if clicked_cell:
                    board.select(clicked_cell[0], clicked_cell[1])
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if board.is_full():
                        win = board.check_board()
                        game_over_screen(screen, win)
                        running = False
                elif pygame.K_1 <= event.key <= pygame.K_9:
                    value = event.key - pygame.K_0
                    board.sketch(value)
                elif event.key == pygame.K_BACKSPACE:
                    board.clear()

        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
