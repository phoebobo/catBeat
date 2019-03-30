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

cat_beat = ['./cat_beat1.jpg','./cat_beat2.jpg','./cat_beat2.jpg']
beat_text = ['干死你！','草泥马！','用力一点！','甘霖娘！','塞林木!','MLGB!']

def startGame():  #去除开始的几个事件，
    textRectObj.top = -400
    cat_rect.top = -400
    startBtn.rect.top = -400
    # beat_rect.top = -500
    #猫图
    catBeatRect.top = 0
    global is_start
    is_start = 1

def gameOver(scorenum):
    screen.fill([0, 0, 0])
    my_font = pygame.font.SysFont('arial', 50)
    highscorestr = 'YOUR SCORE IS ' + str(scorenum)  # 显示得分
    over_screen = my_font.render(highscorestr, True, (255, 0, 0))
    over_rect = over_screen.get_rect()
    over_rect.center = screen.get_rect().center
    screen.blit(over_screen, over_rect)
    global score  # 分数是一个全局变量，在这里重置为0
    score = 0
    pygame.display.update()  # 刷新
    pygame.time.delay(10000)

def clickMouse():
    pass

if __name__ == '__main__':
    pygame.init()  #初始化
    pygame.mixer.init()

    global is_start  #判断开始没
    is_start = 0
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
    # 刚开始的下文字框
    beatObj = pygame.font.SysFont('方正兰亭超细黑简体', 20)
    beatObj.set_bold(True)
    beatText = beatObj.render('狂点鼠标！爆敲猫头！！！', True, blue)
    beat_rect = beatText.get_rect()
    beat_rect.centerx = cat_rect.centerx
    beat_rect.top = 500 - 60
    #开始隐藏的猫图
    catBeatImg = pygame.image.load(cat_beat[0])
    catBeatRect = catBeatImg.get_rect()
    catBeatRect.top = -500
    catBeatRect.left = 0
    #图片type
    cat_type = 0
    #帧率
    clock = pygame.time.Clock()
    #计算分数
    global score
    score = 0
    #用户自定义事件1分钟计时
    addEnemy = pygame.USEREVENT + 1
    pygame.time.set_timer(addEnemy,60000)
    pygame.display.flip()

    while True:
        screen.fill((72,0,0))  #背景色
        clock.tick(300)
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
            elif is_start and event.type == pygame.MOUSEBUTTONDOWN and 0 <= event.pos[0] <= 400 and \
                    0 <= event.pos[1] <= 413:
                catBeatImg = pygame.image.load(cat_beat[1])
                catBeatRect = catBeatImg.get_rect()
                catBeatRect.top = 0
                catBeatRect.left = 0
                cat_type = 1  # 图片变化
                score += 1  #分数
                # pygame.time.delay(100)
                # 下方文字
                beatObj = pygame.font.SysFont('方正兰亭超细黑简体', 50)
                beatObj.set_bold(True)
                beatText = beatObj.render(random.choice(beat_text), True, bright_green)
                beat_rect = beatText.get_rect()
                beat_rect.centerx = cat_rect.centerx
                beat_rect.top = 500 - 70
            if event.type == addEnemy and is_start:
                gameOver(score)

        screen.blit(textObj, textRectObj)
        screen.blit(cat_image, cat_rect)
        screen.blit(startBtn.image, startBtn.rect)
        screen.blit(beatText, beat_rect)
        screen.blit(catBeatImg,catBeatRect)
        pygame.display.flip()
        if cat_type == 1:
            catBeatImg = pygame.image.load(cat_beat[2])
            catBeatRect = catBeatImg.get_rect()
            catBeatRect.top = 0
            catBeatRect.left = 0
            screen.blit(catBeatImg, catBeatRect)
            pygame.time.delay(100)
            pygame.display.flip()
            cat_type = 2
        if cat_type == 2:
            catBeatImg = pygame.image.load(cat_beat[0])
            catBeatRect = catBeatImg.get_rect()
            catBeatRect.top = 0
            catBeatRect.left = 0
            screen.blit(catBeatImg, catBeatRect)
            pygame.display.flip()
            pygame.time.delay(100)
            cat_type = 0
