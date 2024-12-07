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

BUTTON_WIDTH = 120

def draw_buttons(screen, font):
    modes = ["EASY", "MEDIUM", "HARD"]
    box_spacing = (WIDTH-(BUTTON_WIDTH*len(modes))) / (len(modes)+1)
    button_positions = []

    for index, mode in enumerate(modes):
        position = (box_spacing*(index+1)) + (BUTTON_WIDTH*index)
        pygame.draw.rect(screen, (100, 0, 0), (position, 400,BUTTON_WIDTH , 40), 4)
        surface = font.render(mode, 0, BLACK)
        screen.blit(surface, surface.get_rect(center=(position+BUTTON_WIDTH/2, 420)))

        button_positions.append([position, 400])

    return button_positions

def start_screen(screen):
    """Displays the start screen where the user selects difficulty."""
    screen.fill(BG_COLOR)
    font = pygame.font.Font(None, 50)
    text = font.render("Welcome to Sudoku", 0, BLACK)

    font = pygame.font.Font(None, 40)
    game_mode_text = font.render("Select Game Mode:", 0, BLACK)
    game_mode_text_rect = game_mode_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(game_mode_text, game_mode_text_rect)

    button_positions = draw_buttons(screen, font)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if button_positions[0][0] <= x <= button_positions[0][0]+BUTTON_WIDTH and 400 <= y <= 440:
                    return 1  # Easy
                elif button_positions[1][0] <= x <= button_positions[1][0]+BUTTON_WIDTH and 400 <= y <= 440:
                    return 2  # Medium
                elif button_positions[2][0] <= x <= button_positions[2][0]+BUTTON_WIDTH and 400 <= y <= 440:
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
