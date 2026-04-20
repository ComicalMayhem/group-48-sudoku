import pygame


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.sketched_value = 0
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False

    def draw(self):
        font = pygame.font.Font(None, 40)
        x = self.col * 60
        y = self.row * 60

        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), (x, y, 60, 60), 3)

        if self.value != 0:
            text = font.render(str(self.value), True, (0, 0, 0))
            self.screen.blit(text, (x + 20, y + 15))
        elif self.sketched_value != 0:
            sketch_font = pygame.font.Font(None, 25)
            text = sketch_font.render(str(self.sketched_value), True, (128, 128, 128))
            self.screen.blit(text, (x + 5, y + 5))