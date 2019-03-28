import pygame
import random
from pygame.locals import *
from random import randrange
from button import Button
#颜色
white = (255,255,255)
black = (0,0,0)
gray = (128,128,128)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
blue = (0,0,255)

def startGame():
    textRectObj.top = -400
    cat_rect.top = -400
    startBtn.rect.top = -400

if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((400,500))
    pygame.display.set_caption('爆敲猫头')
    window_image = pygame.image.load('./cat_head.png')
    pygame.display.set_icon(window_image)
    #写两个开始的介绍
    titleObj = pygame.font.SysFont('方正兰亭超细黑简体', 50)
    titleObj.set_bold(True)  # 加粗
    textObj = titleObj.render('爆敲猫头', True, bright_green)
    textRectObj = textObj.get_rect()
    textRectObj.center = (200,100)
    startBtn = Button(screen)  #开始按钮
    #文本框

    #开始时中间图片
    cat_image = pygame.image.load('./cat_head.png')
    cat_rect = cat_image.get_rect()
    cat_rect.center = screen.get_rect().center

    pygame.display.flip()

    while True:
        screen.fill((72,0,0))  #背景色
        screen.blit(textObj,textRectObj)
        screen.blit(cat_image,cat_rect)
        screen.blit(startBtn.image, startBtn.rect)
        #关闭游戏
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEMOTION:
                pass
            elif event.type == pygame.MOUSEBUTTONDOWN and 121 <= event.pos[0] <= 279 and \
                    356 <= event.pos[1] <= 428:  # 判断鼠标位置以及是否摁了下去。
                # 做需要做的事情，如开始游戏。
                startGame()


        pygame.display.flip()