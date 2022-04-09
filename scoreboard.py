import pygame.font
from pygame.sprite import Group
import json
from ship import Ship


class Scoreboard:
    """ 显示得分信息的类 """
    
    def __init__(self, ai_game):
        """ 初始化记录得分的属性 """
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        # 显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        # 读取最高得分，准备包含最高得分和当前得分的图像
        self.read_high_score()
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
    
    def prep_score(self):
        """ 将得分转换为渲染的图像 """
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        
        # 屏幕右上角显示得分
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_high_score(self):
        """ 将最高得分转换为渲染的图像 """
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)
        
        # 最高分放到屏幕上方中央位置
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    
    def prep_level(self):
        """ 将等级转换为渲染的图像 """
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        
        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    
    def prep_ships(self):
        """ 显示剩余的飞船数 """
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
    
    def show_score(self):
        """ 在屏幕上绘制得分、等级和余下的飞船数 """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
    
    def read_high_score(self):
        """ 从文件中读入最高得分，无该文件则设置为0 """
        try:
            with open(self.settings.socre_filename) as f:
                score = json.load(f)
        except FileNotFoundError:
            self.stats.high_score = 0
        else:
            self.stats.high_score = score[0]

    def store_high_score(self):
        """ 存储最高得分到文件中 """
        with open(self.settings.socre_filename, 'w') as f:
            high_score_list = [self.stats.high_score]
            json.dump(high_score_list, f)

    def check_high_score(self):
        """ 检查是否诞生了新的最高得分 """
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
            self.store_high_score()

    
    