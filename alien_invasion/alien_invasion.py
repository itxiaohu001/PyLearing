import sys

import pygame

from settings import Settings


class AlienInvasion:
    def _init_(self):
        self.settings = Settings()
        # 初始化pygame
        pygame.init()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_wigth, self.settings.screen_heigth)
        )
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        # 开始游戏的主循环
        while True:
            # 监视键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # 每次循环时都重绘屏幕
            self.screen.fill(self.settings.bg_color)
            # 让最近绘制的屏幕可见
            pygame.display.flip()


if __name__ == "_main_":
    # 创建示例运行游戏
    ai = AlienInvasion()
    ai.run_game()
