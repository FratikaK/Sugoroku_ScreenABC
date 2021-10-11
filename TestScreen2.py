import pygame
from pygame.locals import *

import Screen_abc as SC
from Screen_abc import Screen_abc
import sys

class TestScreen2(Screen_abc):

    def display(self):
        super().update()

        SC.screen.fill(SC.Olive)

        super().setText_L('遷移先の画面', self.grid[9][9], 25, SC.Red)


    def getEvent(self):
        for event in pygame.event.get():
            # 終了用のイベント処理
            if event.type == QUIT:  # 閉じるボタンが押されたとき
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # キーを押したとき
                if event.key == K_ESCAPE:  # Escキーが押されたとき
                    pygame.quit()
                    sys.exit()
                if event.key == K_SPACE:
                    SC.ScreenNum = 0


