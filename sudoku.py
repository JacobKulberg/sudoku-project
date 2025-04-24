import pygame, sys
from sudoku_generator import *
#background rgb
bg = (239, 235, 216)
bg_contrast = (31, 30, 28)
#initializing pygame window
pygame.init()
screen = pygame.display.set_mode((720, 790))
pygame.display.set_caption("Sudoku")

#initializing a sudoku board and saving the solution
sudoku = SudokuGenerator(9, 0)
sudoku.fill_values()
solution = sudoku.get_board()

#you get the idea
def start_screen():
    #creating font
    tit_font = pygame.font.SysFont("comicsans", 120, True)
    button_font = pygame.font.SysFont("comicsans", 90)

    screen.fill(bg)

    #rendering the text onto surfaces
    tit_text = tit_font.render("Sudoku", True, bg_contrast)
    start_text = button_font.render("Start", True, (255, 255, 255))
    exit_text = button_font.render("Exit", True, (255, 255, 255))

    #creating surfaces
    tit_surf = tit_text.get_rect(center = (720//2, 790//2 - 150))
    start_surface = pygame.Surface((start_text.get_size()[0] + 20, start_text.get_size()[1] + 20))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))

    #coloring buttons hehe
    start_surface.fill(bg_contrast)
    exit_surface.fill(bg_contrast)

    #blitting stuff
    screen.blit(tit_text, tit_surf)
    start_surface.blit(start_text, (10, 10))
    exit_surface.blit(exit_text, (10,10))

    #making those buttons
    start_rect = start_surface.get_rect(center = (720//2, 790//2 + 50))
    exit_rect = exit_surface.get_rect(center = (720//2, 790//2 + 120))
    screen.blit(start_surface, start_rect)
    screen.blit(exit_surface, exit_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:



def grids():
    #light lines
    for i in range(1, 9):
        #horizontals
        pygame.draw.line(screen, "black", (0, i * 80), (720, i * 80))
        #verticals
        pygame.draw.line(screen, "black", (i * 80, 0), (i * 80, 720))
    #heavy/box lines
    for i in range(1, 3):
        pygame.draw.line(screen, "black", (0, i * 240), (720, i * 240), 3)
        pygame.draw.line(screen, "black", (i * 240, 0), (i * 240, 720), 3)

#hype moments and aura
if __name__ == '__main__':
    screen.fill(bg)
    grids()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()