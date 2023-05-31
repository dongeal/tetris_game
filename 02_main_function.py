import sys #프로그램 종료 함수 호출용

import pygame
from pygame.locals import QUIT

WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (128,128,128)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pygame.init()
pygame.display.set_caption('Tetris')

SURFACE = pygame.display.set_mode([400, 300])


def main():
    while True:
        SURFACE.fill(WHITE) #바탕 흰색

        for event in pygame.event.get(): # Get events
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()


if __name__ == '__main__':
    main()

