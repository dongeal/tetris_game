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
FPSCLOCK =  pygame.time.Clock()


def main():
    sysfont = pygame.font.SysFont(None, 36)
    counter = 0

    while True:
        SURFACE.fill(WHITE) #바탕 흰색

        for event in pygame.event.get(): # Get events
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        counter += 1
        counter_text = sysfont.render(f'count is {counter}',
                                      True ,
                                      GREY)
        SURFACE.blit(counter_text, (50,50))

        pygame.display.update()
        FPSCLOCK.tick(10) #FPS 10


if __name__ == '__main__':
    main()


