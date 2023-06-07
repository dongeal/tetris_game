import sys #프로그램 종료 함수 호출용
from math import sqrt
import random

import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

from material import *


class Block:
    def __init__(self, name):
        self.turn = 0
        self.type = BLOCKS[name]
        self.data = self.type[self.turn]
        self.size = int(sqrt(len(self.data)))
        self.xpos = (WIDTH-self.size)//2
        self.ypos = 0
    
    def draw(self):
        for index in range(len(self.data)):
            xpos = index % self.size   # 0,1,2,3 x 좌표
            ypos = index // self.size  # 0,1,2,3 y 좌표
            val = self.data[index]     # B,B,J,B,B....material.py에 정의 
            if (( 0 <= ypos + self.ypos <HEIGHT) and
                ( 0 <= xpos + self.xpos <WIDTH) and
                (val != 'B')):
                x_pos = 25 + (xpos + self.xpos) * 25
                y_pos = 25 + (ypos + self.ypos) * 25
                pygame.draw.rect(SURFACE,COLORS[val],
                                 (x_pos,y_pos, 24, 24))


def get_block(): # 무작위로 블록 반환
    name = random.choice(list(BLOCKS.keys())) #J,L,S...
    block = Block(name)
    return block




#전역 변수
pygame.init()
SURFACE = pygame.display.set_mode([600,600])
FPSCLOCK =  pygame.time.Clock()
WIDTH = 10 + 2
HEIGHT = 20 + 1
FIELD =[[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
BLOCK = None
FPS = 15

def main():
    global BLOCK
    score = 0
    if BLOCK is None:
        BLOCK = get_block()  # 랜덤 블럭 선택

    smallfont = pygame.font.SysFont(None, 36)

    # 게임필드 박스 그리기
    for ypos in range(HEIGHT):
        for xpos in range(WIDTH):
            FIELD[ypos][xpos] ='W' if xpos ==0 or xpos == WIDTH -1 else 'B'
    for index in range(WIDTH):
        FIELD[HEIGHT-1][index] = 'W'
    
    # 게임 무한루프 수행
    while True:
        # 이벤트 루프를  확인
        key = None
        for event in pygame.event.get(): # Get events
            if event.type == QUIT: # 종료 이벤트
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                key = event.key
                if key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()       

        # Draw FIELD
        SURFACE.fill((100,100,100))
        for ypos in range(HEIGHT):
            for xpos in range(WIDTH):
                value = FIELD[ypos][xpos]
                pygame.draw.rect(SURFACE, COLORS[value],
                                (xpos*25 +25, ypos*25 +25,24,24))

        BLOCK.draw() # 위에 랜덤으로 가져온 블럭 그리기

        # 점수 나타내기
        score_str = str(score).zfill(6)
        score_image = smallfont.render(score_str, True, (180,180,180))
        SURFACE.blit(score_image,(500,30))
        
        
        
        # 언제나 화면을 업데이트
        pygame.display.update()
        FPSCLOCK.tick(FPS) #FPS 



if __name__ == '__main__':
    main()


