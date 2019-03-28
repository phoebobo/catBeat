import pygame

class Button(pygame.sprite.Sprite):

    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
    # msg为要在按钮中显示的文本
        """初始化按钮的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # 按钮
        self.image = pygame.image.load('./btn1.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx  # 创建按钮的rect对象
        self.rect.centery = 500-72-36

        self.screen.blit(self.image, self.rect)  #绘制上去
