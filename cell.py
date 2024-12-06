class Cell():
    def init(self, value, row, col, screen):
        self.value = value
        self.sketched_value = 0
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False

        # Initializes a Cell object
        # Parameters: value (the value in the cell), row (row index of the cell), col (column index of the cell), screen (pygame screen where the cell is drawn)

    def set_cell_value(self, value):
        self.value = value
        #sets the value of the cell

    def set_sketched_value(self, value):
        self.sketched_value = value
        # """
        # sets the sketched value of the cell
        # """

    def draw(self, width, height):
        cell_size_x = width/9
        cell_size_y = height/9
        x = self.col * cell_size_x
        y = self.row * cell_size_y


        # if cell is selected, it will be highlighted red
        if self.selected:
                pygame.draw.rect(self.screen, (100, 0, 0), (x, y, cell_size_x, cell_size_y), 5)
        font = pygame.font.Font(None, 40)
        #draws the value (non-user input) if it exists
        if self.value != 0:
            num = font.render(str(self.value), 0, (0, 0, 0))
            self.screen.blit(num, num.get_rect(center=((self.col* cell_size_x + cell_size_x/2), (self.row*cell_size_y + cell_size_y/2))))
        #draws sketched value (user input) if it exists
        elif self.sketched_value != 0:
            sketch_num = font.render(str(self.sketched_value), 0, (50, 50, 50))
            self.screen.blit(sketch_num, sketch_num.get_rect(topleft=(x, y)))