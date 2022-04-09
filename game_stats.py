import json


class GameStats:
    """ 跟踪游戏的统计信息 """
    
    def __init__(self, ai_game):
        """ 初始化随游戏进行可能变化的统计信息 """
        self.settings = ai_game.settings
        self.reset_stats()
        
        # 让游戏一开始处于非活动状态
        self.game_active = False
        
        self.high_score = 0
        
    def reset_stats(self):
        """ 初始化在游戏运行期间可能变化的统计信息 """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
    
    
    