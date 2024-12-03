import pygame

class Cell:
    def __init__(self, value, row, col, screen, isOG = False):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketchedval = 0
        self.isOG = isOG
    def set_cell_value(self, value):
        self.value = value
    def set_sketched_value(self, value):
        self.sketchedval = value
    def draw(self):
        font = pygame.font.SysFont('Arial', 60)
        text = font.render(str(self.value), True, 'Black')
        self.screen.blit(text, (self.col * 70, self.row * 70))
        if self.sketchedval != 0:
            sketch = font.render(str(self.sketchedval), True, 'Grey', size=12)
            self.screen.blit(sketch, (self.col * 70, self.row * 70))

