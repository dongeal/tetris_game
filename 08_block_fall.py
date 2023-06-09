import sys #프로그램 종료 함수 호출용
from math import sqrt
import random

import pygame
from pygame.locals import QUIT, KEYDOWN, K_UP, K_LEFT, K_RIGHT, K_DOWN, K_SPACE, K_ESCAPE

from material import *


class Block:
    def __init__(self, name):
        self.turn = 0
        self.type = BLOCKS[name]
        self.data = self.type[self.turn]
        self.size = int(sqrt(len(self.data)))
        self.xpos = (WIDTH-self.size)//2
        self.ypos = 0
        self.stop = 0

    def update(self):
        global BLOCK
        if is_overlapped(self.xpos,self.ypos+1, self.turn):
            for y_offset in range(self.size):
                for x_offset in range(self.size):
                    if (( 0 <= self.xpos + x_offset < WIDTH) and 
                        ( 0 <= self.ypos + y_offset <HEIGHT)): 
                         val =self.data[y_offset*self.size +x_offset]
                         if val !='B':
                            FIELD[self.ypos + y_offset][self.xpos + x_offset] = val
            BLOCK = get_block()         
    
        else:
            self.stop = self.stop +1
            if self.stop > FPS *1:
                self.stop = 0
                self.ypos =self.ypos+1


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
    
    def left(self): 
        if not is_overlapped(self.xpos-1, self.ypos, self.turn):
            self.xpos = self.xpos-1  # 충돌아니면 키 반응

    def right(self):
        if not is_overlapped(self.xpos+1, self.ypos, self.turn):       
            self.xpos = self.xpos+1    

    def down(self):
        if not is_overlapped(self.xpos, self.ypos+1, self.turn):
            self.ypos = self.ypos+1
    
    def up(self):
        if not is_overlapped(self.xpos-1, self.ypos, (self.turn+1)%4):
            self.turn =(self.turn+1)%4
            self.data =self.type[self.turn]

def get_block(): # 무작위로 블록 반환
    name = random.choice(list(BLOCKS.keys())) #J,L,S...
    block = Block(name)
    return block

def is_overlapped(xpos, ypos, turn): # 블록 충돌 판정
    data = BLOCK.type[turn]
    for y_offset in range(BLOCK.size):
        for x_offset in range(BLOCK.size): # 블록전체데이타를 순환
            if (( 0 <= xpos + x_offset < WIDTH) and 
                ( 0 <= ypos + y_offset <HEIGHT)):  # 블록이 필드안에 있는디
                if ((data[y_offset*BLOCK.size + x_offset] != 'B') and
                    (FIELD[ypos + y_offset][xpos + x_offset] != 'B')): #빈칸아니면
                     return True  # 충돌
    return False # 충돌아님

def is_game_over():
    filled = 0
    for cell in FIELD[0]:
        if cell != 'B':
            filled += 1
    return filled >2

#전역 변수
pygame.init()
pygame.key.set_repeat(150,30) #delay 30, interval 30
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
    
    # 메세지
    smallfont = pygame.font.SysFont(None, 36)
    largefont = pygame.font.SysFont(None, 72)
    message_over = largefont.render("Game Over!!", True, (255,255,255))
    message_rect = message_over.get_rect()
    message_rect.center = (300,300)


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
        # 게임 오버 확인
        if is_game_over():
            SURFACE.blit(message_over, message_rect)
        else: # 게임 오버 아니면
        # 움직임 처리    
            if key == K_UP or key == K_SPACE:
                BLOCK.up()
            elif key == K_RIGHT:
                BLOCK.right()
            elif key == K_LEFT:
                BLOCK.left()
            elif key == K_DOWN:
                BLOCK.down() 

<<<<<<< HEAD
        if key == K_UP or key == K_SPACE:
            BLOCK.up()
        elif key == K_RIGHT:
            BLOCK.right()
        elif key == K_LEFT:
            BLOCK.left()
        elif key == K_DOWN:
            BLOCK.down() 

        # Draw FIELD
        SURFACE.fill((0,0,0))
        for ypos in range(HEIGHT):
            for xpos in range(WIDTH):
                value = FIELD[ypos][xpos]
                pygame.draw.rect(SURFACE, COLORS[value],
                                (xpos*25 +25, ypos*25 +25,24,24))
=======
            # Draw FIELD
            SURFACE.fill((0,0,0))
            for ypos in range(HEIGHT):
                for xpos in range(WIDTH):
                    value = FIELD[ypos][xpos]
                    pygame.draw.rect(SURFACE, COLORS[value],
                                    (xpos*25 +25, ypos*25 +25,24,24))

            BLOCK.update()
            BLOCK.draw() # 위에 랜덤으로 가져온 블럭 그리기
>>>>>>> 7afd7de4b8dafad01ee7c31db3db0a09ad8f73d9

            # 점수 나타내기
            score_str = str(score).zfill(6)
            score_image = smallfont.render(score_str, True, (180,180,180))
            SURFACE.blit(score_image,(500,30))
        
        
        
         # 언제나 화면을 업데이트
        pygame.display.update()
        FPSCLOCK.tick(FPS) #FPS 



if __name__ == '__main__':
    main()


