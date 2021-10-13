import pygame
from pygame.locals import *

import Screen_abc as SC
from Screen_abc import Screen_abc
import sys

effect_instance = list()


def split_image(image, width: int, height: int, num: int):
    image_list = []
    for i in range(0, width, height):
        surface = pygame.Surface((int(width / num), height))
        surface.blit(image, (0, 0), (i, 0, int(width / num), height))
        surface.set_colorkey(surface.get_at((0, 0)), RLEACCEL)
        surface.convert()
        image_list.append(surface)
    return image_list


class EffectScreen(Screen_abc):
    def __init__(self):
        super().__init__()

    def display(self):
        for effect in effect_instance:
            effect.update()
            effect.draw(SC.screen)

        pygame.display.update()

    # 非同期で実行させるので何もしない
    def getEvent(self):
        pass


class SampleEffect(pygame.sprite.Sprite):
    frame = 0

    def __init__(self):
        super(SampleEffect, self).__init__()
        self.images = split_image("img/effect/sample_effect.png", 687, 24, 21)
