import pygame
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.sketched_value = 0
        self.row = row
        self.col = col
        self.screen = screen
        self.size = size
        self.selected = False
        """
        Initializes a Cell object
        Parameters: value (the value in the cell), row (row index of the cell), col (column index of the cell), screen (pygame screen where the cell is drawn)
        """
    def set_cell_value(self, value):
        self.value = value
        """
        sets the value of the cell
        """
    def set_sketched_value(self, value):
        self.sketched_value = value
        """
        sets the sketched value of the cell
        """

    def draw(self):
        cell_size = 50
        x = self.col * cell_size
        y = self.row * cell_size

        #draws cell border
        pygame.draw.rect(self.screen, (0, 0, 0), (x, y, cell_size, cell_size), 1)
    # if cell is selected, it will be highlighted red
    if self.selected:
            pygame.draw.rect(self.screen, (100, 0, 0), (x, y, cell_size, cell_size), 5)
    font = pygame.font.Font(None, 40)
    #draws the value (non-user input) if it exists
    if self.value != 0:
        num = font.render(str(self.value), 0, (0, 0, 0))
        self.screen.blit(num, num.get_rect(center=(x, y, cell_size, cell_size).center))
    #draws sketched value (user input) if it exists
    elif self.sketched_value != 0:
        sketch_num = font.render(str(self.sketched_value), 0, (50, 50, 50))
        self.screen.blit(sketch_text, sketch_text.get_rect(topleft=(x, y)))


