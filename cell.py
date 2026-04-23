import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.sketched_value = 0
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False

    def draw(self,scale):
        font = pygame.font.Font(None, scale)
        x = self.col * scale
        y = self.row * scale
        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), (x, y, scale, scale), 3)
        if self.value != 0:
            text = font.render(str(self.value), True, (0, 0, 0))
            self.screen.blit(text, (x+(scale//3), y+(scale//3)))
        elif self.sketched_value != 0:
            sketch_font = pygame.font.Font(None, scale)
            text = sketch_font.render(str(self.sketched_value), True, (128, 128, 128))
            self.screen.blit(text, (x+scale//3, y+scale//3))
    
    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value
