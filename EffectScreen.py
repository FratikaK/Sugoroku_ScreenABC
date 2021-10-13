import pygame
from pygame.locals import *

import Screen_abc as SC
from Screen_abc import Screen_abc
import sys

effect_instance = pygame.sprite.Group()


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
        effect_instance.update()
        effect_instance.draw(SC.screen)

    # 非同期で実行させるので何もしない
    def getEvent(self):
        pass


class SampleEffect(pygame.sprite.Sprite):
    frame = 0

    def __init__(self, x_location, y_location):
        super(SampleEffect, self).__init__()
        self.images = [pygame.image.load("./img/uma/uma01.png"),
                       pygame.image.load("./img/uma/uma02.png"),
                       pygame.image.load("./img/uma/uma03.png"),
                       pygame.image.load("./img/uma/uma04.png"),
                       pygame.image.load("./img/uma/uma05.png"),
                       pygame.image.load("./img/uma/uma06.png")]
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x_location
        self.rect.y = y_location

    def update(self):
        if self.frame > len(self.images) - 1:
            self.frame = 0
        self.image = self.images[self.frame]
        self.frame += 1
