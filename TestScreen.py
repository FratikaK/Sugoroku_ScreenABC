import pygame
from pygame.locals import *

import Screen_abc as SC
from Screen_abc import Screen_abc
import sys

class TestScreen(Screen_abc):

    def display(self):
        super().update()

        super().setBackground(SC.backImg,(0,128,32,32))

        super().setText_L('大きいサイズ', self.grid[1][1], 25, SC.Yellow)
        super().setText_M('中くらいサイズ', self.grid[0][9], 25, SC.Purple)
        super().setText_S('小さいサイズ', self.grid[19][9], 25, SC.Fuchsia)

        super().setBox(SC.Navy_Blue,self.grid[19][9],32*10,32*5)

        text = ['これはsetTextBox_Sによる文章です。','２段落目はこんな感じ','ここは３段落目']

        super().setTextBox_S(text, SC.White, SC.White, self.grid[1][14], 32*30, 32*5,1,25,10,10)

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
                    SC.ScreenNum = 1


