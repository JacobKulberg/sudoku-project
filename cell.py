import pygame
class Cell():
    def __init__(self, value, row, col, screen):
        self.value = value
        self.sketched_value = 0
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.is_finalized = False  # Flag to check if the value was finalized by the user

    def set_cell_value(self, value):
        self.value = value
        self.is_finalized = False  # Reset finalized flag when value is set

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self, width, height):
        cell_size_x = width / 9
        cell_size_y = height / 9
        x = self.col * cell_size_x
        y = self.row * cell_size_y

        # Highlight the cell if selected
        if self.selected:
            pygame.draw.rect(self.screen, (100, 0, 0), (x, y, cell_size_x, cell_size_y), 5)

        font = pygame.font.Font(None, 40)

        # Draw the value (non-user input) if it exists
        if self.value != 0:
            if not self.is_finalized:
                color = (0, 0, 0)
            else:
                color = (129, 133, 137)
            num = font.render(str(self.value), 0, color)
            self.screen.blit(num, num.get_rect(center=((self.col * cell_size_x + cell_size_x / 2),
                                                       (self.row * cell_size_y + cell_size_y / 2))))
        # Draw sketched value (user input) if it exists
        elif self.sketched_value != 0:
            sketch_num = font.render(str(self.sketched_value), 0, (230, 230, 230))
            self.screen.blit(sketch_num, sketch_num.get_rect(topleft=(x + 10, y + 10)))

    def finalize_value(self):
        if self.sketched_value != 0:
            self.value = self.sketched_value
            self.sketched_value = 0
            self.is_finalized = True