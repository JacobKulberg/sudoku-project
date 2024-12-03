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
        fontBig = pygame.font.SysFont('Arial', 60)
        fontSmall = pygame.font.SysFont('Arial', 30)
        if self.value != 0:
            text = fontBig.render(str(self.value), True, 'Black')
            self.screen.blit(text, (self.col * 70, self.row * 70))
        if self.sketchedval != 0:
            sketch = fontSmall.render(str(self.sketchedval), True, 'Grey')
            self.screen.blit(sketch, (self.col * 70+5, self.row * 70+5))

