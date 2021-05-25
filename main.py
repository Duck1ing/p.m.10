import pygame
import sys
import PickBanTool
import searchByName
import Timer
import ChampionClass

SCREEN_WIDTH = 1366  #화면 가로
SCREEN_HEIGHT = 768  #화면 세로

pygame.init()  #파이게임 초기화
pygame.display.set_caption("PickBan")
pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

while True:  #메인
    clock.tick(60)  #최대 프레임 = 60
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  #종료시 시스템 완전히 종료

    pygame.display.update()  #창 띄우기
