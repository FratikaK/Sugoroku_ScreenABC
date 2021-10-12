import pygame
from pygame.locals import *

import Screen_abc as SC
from Screen_abc import Screen_abc
import sys

TEXT_SIZE = 25
TITLE_SIZE = 50

# 一人で遊ぶはTrue、みんなで遊ぶはFalseにする
SOLO = True

PLAYER = "プレイヤーの人数"
CPU = "CPUの人数"
TURN = "ターン数"
EXAMPLE1 = "EXAMPLE1"
EXAMPLE2 = "EXAMPLE2"
EXAMPLE3 = "EXAMPLE3"
EXAMPLE4 = "EXAMPLE4"

if SOLO:
    config = {CPU: 1, TURN: 10, EXAMPLE1: 1, EXAMPLE2: 1, EXAMPLE3: 1, EXAMPLE4: 1}
    select_position = {0: 100, 1: 130, 2: 160, 3: 190, 4: 220, 5: 250, 6: 280}
else:
    config = {PLAYER: 2, CPU: 1, TURN: 10, EXAMPLE1: 1, EXAMPLE2: 1, EXAMPLE3: 1, EXAMPLE4: 1}
    select_position = {0: 100, 1: 130, 2: 160, 3: 190, 4: 220, 5: 250, 6: 280, 7: 310}

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
    def __init__(self, player_num: int, cpu_num: int, turn: int, example1: int, example2: int, example3: int,
                 example4: int):
        self.player_num = player_num
        self.cpu_num = cpu_num
        self.turn = turn
        self.example1 = example1
        self.example2 = example2
        self.example3 = example3
        self.example4 = example4


class ConfigScreen(Screen_abc):
    def __init__(self):
        super(ConfigScreen, self).__init__()

    # Override
    def display(self):
        SC.screen.fill((0, 0, 0))
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
                        SC.ScreenNum = 0
                        c = config
                        # main.pyまたは、ゲームを動かすクラスにインスタンスを格納させる
                        if SOLO:
                            Config(1, c.get(CPU), c.get(TURN), c.get(EXAMPLE1), c.get(EXAMPLE2), c.get(EXAMPLE3),
                                   c.get(EXAMPLE4))
                        else:
                            Config(c.get(PLAYER), c.get(CPU), c.get(TURN), c.get(EXAMPLE1), c.get(EXAMPLE2),
                                   c.get(EXAMPLE3),
                                   c.get(EXAMPLE4))
                        # TODO 次の画面にすすむ処理、またはキャラクター選択画面？
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
