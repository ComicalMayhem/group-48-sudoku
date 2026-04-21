import pygame

# where main function shall be run
# and create the different screens

import pygame
from sudoku_generator import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400), pygame.RESIZABLE)
pygame.display.set_caption('Sudoku')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

bg = pygame.image.load('Graphics/bg.jpg')
text = test_font.render('Sudoku', True, 'Black')

easy = test_font.render('Easy',True,'Black')
medium = test_font.render('Medium',True,'Black')
hard = test_font.render('Hard',True,'Black')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.VIDEORESIZE:
            screen.blit(pygame.transform.scale(bg, event.dict['size']), (0, 0))
            pygame.display.update()
            x,y = screen.get_size()[0],screen.get_size()[1]
        elif event.type == pygame.VIDEOEXPOSE:
            screen.fill((0, 0, 0))
            screen.blit(pygame.transform.scale(bg, screen.get_size()), (0, 0))
            x, y = screen.get_size()[0], screen.get_size()[1]
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if easy_rect.collidepoint(pos):
                board = generate_sudoku(9, 30)
            elif medium_rect.collidepoint(pos):
                board = generate_sudoku(9, 40)
            elif hard_rect.collidepoint(pos):
                board = generate_sudoku(9, 50)


    text_rect = text.get_rect(center=(x // 2, y // 4))
    screen.blit(pygame.transform.scale(text, text.get_size()), text_rect)

    easy_rect = easy.get_rect(center=(x * 0.25, y * 0.75))
    pygame.draw.rect(screen, 'white', easy_rect, 10,10)
    pygame.draw.rect(screen, 'white', easy_rect,border_radius = 10)

    medium_rect = medium.get_rect(center=(x * 0.5, y * 0.75))
    pygame.draw.rect(screen, 'white', medium_rect, 10, 10)
    pygame.draw.rect(screen, 'white', medium_rect, border_radius=10)

    hard_rect = hard.get_rect(center=(x * 0.75, y * 0.75))
    pygame.draw.rect(screen, 'white', hard_rect, 10, 10)
    pygame.draw.rect(screen, 'white', hard_rect, border_radius=10)

    screen.blit(easy,easy_rect)
    screen.blit(medium,medium_rect)
    screen.blit(hard,hard_rect)


    pygame.display.update()
    clock.tick(60)

