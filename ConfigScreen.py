import pygame
from pygame.locals import *

import Screen_abc as SC
from Screen_abc import Screen_abc
from effect import *
import sys

TEXT_SIZE = 25
TITLE_SIZE = 50

# 一人で遊ぶはTrue、みんなで遊ぶはFalseにする
SOLO = False

PLAYER = "プレイヤーの人数"
CPU = "CPUの人数"
TURN = "ターン数"

if SOLO:
    config = {CPU: 1, TURN: 10}
    select_position = {0: 100, 1: 130, 2: 160}
else:
    config = {PLAYER: 2, CPU: 1, TURN: 10}
    select_position = {0: 100, 1: 130, 2: 160, 3: 190}

now_select = 0
limit = len(select_position) - 1
config_iterator = {}
i = 0
for cf in config.keys():
    config_iterator[i] = cf
    i += 1


# データクラスとして利用する
# 設定が終わった後の数値はここに格納する
class Config:
    def __init__(self, player_num: int, cpu_num: int, turn: int):
        self.player_num = player_num
        self.cpu_num = cpu_num
        self.turn = turn


class ConfigScreen(Screen_abc):
    def __init__(self):
        super(ConfigScreen, self).__init__()

    # Override
    def display(self):
        SC.screen.fill((0, 120, 0))
        text_width = 400
        num_width = 800
        height = 100
        # タイトル表示
        super().setText_L("Game Setting", (500, 30), TITLE_SIZE)
        # 各設定の項目表示
        for conf in config.keys():
            super().setText_M(conf, (text_width, height), TEXT_SIZE)
            super().setText_M(str(config.get(conf)), (num_width, height), TEXT_SIZE)
            height += 30
        super().setText_M("次へ", (num_width, height), TEXT_SIZE)

        # 選択の表示
        super().setText_M("<         >", (770, select_position.get(now_select)), TEXT_SIZE)

        # 操作の仕方表示
        super().setText_M(
            "←　→で数値変更、設定が大丈夫ならスペースキーで次へを押してね", (30, 600), TEXT_SIZE)
        draw_effect()
        super().update(60)

    # Override
    def getEvent(self):
        global now_select
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == K_UP:
                    now_select = now_select - 1
                    if now_select < 0:
                        now_select = limit
                elif event.key == K_DOWN:
                    now_select = now_select + 1
                    if now_select > limit:
                        now_select = 0
                elif event.key == K_SPACE:
                    if now_select == limit:
                        # SC.ScreenNum = 0
                        c = config
                        # main.pyまたは、ゲームを動かすクラスにインスタンスを格納させる
                        if SOLO:
                            Config(1, c.get(CPU), c.get(TURN))
                        else:
                            Config(c.get(PLAYER), c.get(CPU), c.get(TURN))
                        effect_group.add(ScreenChangeEffect(4))
                        return

                if now_select < limit:
                    if event.key == K_LEFT:
                        conf_str = config_iterator.get(now_select)
                        config[conf_str] -= 1
                        if config[conf_str] < 1:
                            config[conf_str] = 1
                    elif event.key == K_RIGHT:
                        conf_str = config_iterator.get(now_select)
                        config[conf_str] += 1
