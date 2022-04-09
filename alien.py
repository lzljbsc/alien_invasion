import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """ 表示单个外星人的类 """
    
    def __init__(self, ai_game):
        """ 初始化外星人并设置其初始位置 """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.default_scale = self.settings.alien_scale
        self.scale = self.default_scale
        
        # 加载外星人图像并获取外接矩形
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # 获得外接矩形的宽高
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # 在外星人的属性x中存储小数值
        self.x = float(self.rect.x)
        
    def update(self):
        """ 向左右移动外星人 """
        self.scale -= 1
        if self.scale <= 0:
            self.x += (self.settings.alien_speed * self.settings.fleet_direction)
            self.rect.x = self.x
            self.scale = self.default_scale
        
    def check_edges(self):
        """ 如果外星人位于屏幕边缘，就返回True """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

