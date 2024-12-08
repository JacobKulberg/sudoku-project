import pygame, sys
from board import Board

WIDTH = 540
HEIGHT = 600
BG_COLOR = (255, 255, 245)
NUM_COLOR = (171, 176, 172)
PINK = (255, 192, 203)
GRAY = (168, 168, 168)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_PINK= (227, 115, 131)
BUTTON_WIDTH = 120


def draw_buttons(screen, font):
    modes = ["EASY", "MEDIUM", "HARD"]
    box_spacing = (WIDTH - (BUTTON_WIDTH * len(modes))) / (len(modes) + 1)
    button_positions = []

    for index, mode in enumerate(modes):
        position = (box_spacing * (index + 1)) + (BUTTON_WIDTH * index)
        pygame.draw.rect(screen, WHITE, (position, 400, BUTTON_WIDTH, 40))
        pygame.draw.rect(screen, DARK_PINK, (position, 400, BUTTON_WIDTH, 40), 4)
        surface = font.render(mode, 0, BLACK)
        screen.blit(surface, surface.get_rect(center=(position + BUTTON_WIDTH / 2, 420)))

        button_positions.append([position, 400])
    return button_positions


def draw_game_buttons(screen, font):
    buttons = ["RESET", "RESTART", "EXIT"]
    box_spacing = (WIDTH - (BUTTON_WIDTH * len(buttons))) / (len(buttons) + 1)
    button_positions = []

    for index, label in enumerate(buttons):
        position = (box_spacing * (index + 1)) + (BUTTON_WIDTH * index)
        pygame.draw.rect(screen, WHITE, (position, 550, BUTTON_WIDTH, 40), 0)  # Button background
        pygame.draw.rect(screen, DARK_PINK, (position, 550, BUTTON_WIDTH, 40), 2)  # Button border
        surface = font.render(label, 0, BLACK)
        screen.blit(surface, surface.get_rect(center=(position + BUTTON_WIDTH / 2, 570)))

        button_positions.append((position, 550, BUTTON_WIDTH, 40))  # Store button position as a tuple

    return button_positions

def start_screen(screen):
    """Displays the start screen where the user selects difficulty."""
    screen.fill(PINK)
    font = pygame.font.Font(None, 50)
    text = font.render("Welcome to Sudoku", 0, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(text, text_rect)
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

                if button_positions[0][0] <= x <= button_positions[0][0] + BUTTON_WIDTH and 400 <= y <= 440:
                    return 1  # Easy
                elif button_positions[1][0] <= x <= button_positions[1][0] + BUTTON_WIDTH and 400 <= y <= 440:
                    return 2  # Medium
                elif button_positions[2][0] <= x <= button_positions[2][0] + BUTTON_WIDTH and 400 <= y <= 440:
                    return 3  # Hard


def game_over_screen(screen, win):
    """Displays the game over screen with success or failure message."""
    screen.fill(PINK)
    font = pygame.font.Font(None, 50)

    if win:
        message = font.render("Game Won!", 0, BLACK)
    else:
        message = font.render("Game Over :(", 0, BLACK)

    message_rect = message.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(message, message_rect)

    font = pygame.font.Font(None, 30)
    button_x = WIDTH // 2 - BUTTON_WIDTH // 2
    pygame.draw.rect(screen, WHITE, (button_x, 400, BUTTON_WIDTH, 40))
    pygame.draw.rect(screen, DARK_PINK, (button_x, 400, BUTTON_WIDTH, 40), 4)

    if win:
        text = "EXIT"
    else:
        text = "RESTART"

    surface = font.render(text, 0, BLACK)
    screen.blit(surface, surface.get_rect(center=(button_x + BUTTON_WIDTH//2, 420)))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if button_x <= x <= button_x + BUTTON_WIDTH and 400 <= y <= 440:
                    if win:
                        pygame.quit()
                        sys.exit()
                    return 1  #So the loop will end and game will restart

def sudoku_screen(screen, board):
    board.draw()


def main():
    """Main function to run the game."""
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    font = pygame.font.Font(None, 30)

    difficulty = start_screen(screen)
    board = Board(WIDTH, HEIGHT, screen, difficulty)
    screen.fill(BG_COLOR)

    while True:

        board.draw()
        button_positions = draw_game_buttons(screen, font)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                #Game button functionality
                for index, (bx, by, bwidth, bheight) in enumerate(button_positions):
                    if bx <= x <= bx + bwidth and by <= y <= by + bheight:
                        if index == 0:  # RESET
                            board.reset_to_original()
                        elif index == 1:  # RESTART
                            difficulty = start_screen(screen)
                            board = Board(WIDTH, WIDTH, screen, difficulty)
                        elif index == 2:  # EXIT
                            pygame.quit()
                            sys.exit()

                #Cell selection functionality
                clicked_cell = board.click(x, y)
                if clicked_cell:
                    board.select(clicked_cell[0], clicked_cell[1])
            elif event.type == pygame.KEYDOWN:
                #Key events
                if event.key == pygame.K_RETURN:
                    #Finalizing values
                    if board.selected:
                        row, col = board.selected
                        board.cells[row][col].finalize_value()

                    #Ends game and checks if all values are correct
                    if board.is_full():
                        win = board.check_board()
                        game_over_screen(screen, win)
                        difficulty = start_screen(screen)
                        board = Board(WIDTH, WIDTH, screen, difficulty)
                elif pygame.K_1 <= event.key <= pygame.K_9:
                    value = event.key - pygame.K_0
                    board.sketch(value)
                elif event.key == pygame.K_BACKSPACE:
                    board.clear()
                elif event.key == pygame.K_UP:
                    board.move_selection("UP")
                elif event.key == pygame.K_DOWN:
                    board.move_selection("DOWN")
                elif event.key == pygame.K_LEFT:
                    board.move_selection("LEFT")
                elif event.key == pygame.K_RIGHT:
                    board.move_selection("RIGHT")

        pygame.display.update()


if __name__ == "__main__":
    main()