class GameStats():
    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True
        self.game_pause = False
        self.new_high = False
        self.alien_bot = 0
        self.boss = False
        self.count = 0
        self.boss_bullet_time_count = 20
        self.boss_bullets_limit = 3
        self.boss_shot = False
        with open('high_score.txt') as hs:
            high_score =int( hs.read())
        self.high_score = high_score
    def reset_stats(self):
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
    def reset_boss_bulet(self):
        self.boss_bullet_time_count = 20
    def reset_count(self):
        self.count = 0
