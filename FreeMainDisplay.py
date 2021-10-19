import random

import pygame
from pygame.locals import *

from Screen_abc import Screen_abc
import Screen_abc as SC
import sys

from effect import *
from player_sample.player import Player, Object

back_ground_image = pygame.image.load("img/background/river2.png")
player1_window = pygame.image.load("img/window/player1_window.png")
player2_window = pygame.image.load("img/window/player2_window.png")
player3_window = pygame.image.load("img/window/player3_window.png")
player4_window = pygame.image.load("img/window/player4_window.png")
string_window = pygame.image.load("img/window/string_window.png")
end_window = pygame.image.load("img/window/end_window.png")
turn_window = pygame.image.load("img/window/turn_window.png")
item_title_window = pygame.image.load("img/window/item_title.png")
item_window = pygame.image.load("img/window/item_window.png")
square_image = [pygame.image.load("img/square/square_plus.png"),
                pygame.image.load("img/square/square_sub.png"),
                pygame.image.load("img/square/square_object.png"),
                pygame.image.load("img/square/square_bonus.png"),
                pygame.image.load("img/square/square_sub_extra.png")]
masu = [(256, 160), (320, 160), (384, 160), (448, 160), (512, 160), (576, 160), (640, 160), (704, 160), (768, 160),
        (832, 160), (896, 160), (960, 160),
        # 上ライン
        (960, 224), (960, 288), (960, 352), (960, 416),  # 右ライン
        (896, 416), (832, 416), (768, 416), (704, 416), (640, 416), (576, 416), (512, 416), (448, 416), (384, 416),
        (320, 416), (256, 416),
        # 下ライン
        (256, 352), (256, 288), (256, 224)]  # 左ライン

player_array = [Player("First"), Player("Second"), Player("Third"), Player("Forth")]

object_array = [Object("うどん"), Object("そば")]


class FreeMainDisplay(Screen_abc):
    def __init__(self):
        super(FreeMainDisplay, self).__init__()
        self.now_select = 0
        self.player_turn = 1

    def display(self):
        SC.screen.blit(back_ground_image, back_ground_image.get_rect())
        SC.screen.blit(player1_window, (0, 0))
        SC.screen.blit(player2_window, (320, 0))
        SC.screen.blit(player3_window, (640, 0))
        SC.screen.blit(player4_window, (960, 0))
        SC.screen.blit(string_window, (256, 480))
        SC.screen.blit(turn_window, (32, 160))
        SC.screen.blit(end_window, (32, 512))
        SC.screen.blit(item_title_window, (1120, 320))
        SC.screen.blit(item_window, (1088, 352))

        for sq in masu:
            SC.screen.blit(square_image[self.now_select], sq)

        draw_effect()
        super().update(10)

    def getEvent(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == K_RIGHT:
                    self.now_select += 1
                    if self.now_select > len(square_image) - 1:
                        self.now_select = 0
                if event.key == K_LEFT:
                    self.now_select -= 1
                    if self.now_select < 0:
                        self.now_select = len(square_image) - 1
                if event.key == K_UP:
                    self.player_turn += 1
                    if self.player_turn > 4:
                        self.player_turn = 1
                    effect_group.add(ScreenLineFontEffect("プレイヤー" + str(self.player_turn) + "のターン"))

                if event.key == K_1:
                    money = random.randint(0, 100)
                    player_array[self.player_turn - 1].set_money(money)
                if event.key == K_2:
                    rand = random.randint(0, len(object_array) - 1)
                    player_array[self.player_turn - 1].add_object(object_array[rand])
