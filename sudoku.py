import pygame
import board

# where main function shall be run
# and create the different screens

import pygame
from sudoku_generator import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,800), pygame.RESIZABLE)
screen_rect = screen.get_rect()
pygame.display.set_caption('Sudoku')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

bg = pygame.image.load('Graphics/bg.jpg')
paper = pygame.image.load('Graphics/paper.jpg')
paper = pygame.transform.scale(paper,(497,497))
paper2 = pygame.image.load('Graphics/paper.jpg')
paper2 = pygame.transform.scale(paper,(497,497))
paper2_rect = paper2.get_rect()
text = test_font.render('Sudoku', True, 'Black')

easy = test_font.render('Easy',True,'Black')
medium = test_font.render('Medium',True,'Black')
hard = test_font.render('Hard',True,'Black')
submit = test_font.render('Submit',True,'Black')
clear = test_font.render('Clear',True,'Black')

confirm = False
valid_nums = [pygame.K_KP1, pygame.K_1, pygame.K_KP2, pygame.K_2,
              pygame.K_KP3, pygame.K_3, pygame.K_KP4, pygame.K_4,
              pygame.K_KP5, pygame.K_5, pygame.K_KP6, pygame.K_6,
              pygame.K_KP7, pygame.K_7, pygame.K_KP8, pygame.K_8,
              pygame.K_KP9, pygame.K_9]

game_start = True
game_play = False
game_end = False
x,y = screen.get_size()[0],screen.get_size()[1]

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

        if game_start:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if easy_rect.collidepoint(pos):
                    apples = board.Board(500, 500, paper, 'easy')
                    game_play,game_start = True, False
                elif medium_rect.collidepoint(pos):
                    apples = board.Board(500, 500, paper, 'medium')
                    game_play, game_start = True, False
                elif hard_rect.collidepoint(pos):
                    apples = board.Board(500, 500, paper, 'hard')
                    game_play, game_start = True, False
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
        if game_play:
            screen.blit(pygame.transform.scale(bg, screen.get_size()), (0, 0))
            paper_rect = paper.get_rect(center=(screen.get_size()[0] // 2, screen.get_size()[1] // 2))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                paper.blit(paper2,paper2_rect)
                pos = list(pygame.mouse.get_pos())
                if ((screen_rect.width/2)-250) < pos[0] < ((screen_rect.width/2)+250) and ((screen_rect.height/2)-250) < pos[1] < ((screen_rect.height/2)+250):
                    pos[0] = pos[0]-((screen_rect.width//2)-250)
                    pos[1] = pos[1]-(screen_rect.height//2)+250
                    item = apples.click(pos[0],pos[1])
                else:
                    item = None
                if item is not None:
                    apples.select(item[0],item[1])
                apples.draw()
            if event.type == pygame.KEYDOWN:
                for index, value in enumerate(valid_nums):
                    if event.key == value:
                        apples.sketch((index//2)+1)
                        confirm = (index//2)+1
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    apples.place_number(confirm)
            screen.blit(paper, paper_rect)
            apples.draw()

    pygame.display.update()
    clock.tick(60)

