import pygame
from pygame.locals import *

import Screen_abc as SC
from Screen_abc import Screen_abc
import sys

images = [pygame.image.load("img/uma/uma01.png"),
          pygame.image.load("img/uma/uma02.png"),
          pygame.image.load("img/uma/uma03.png"),
          pygame.image.load("img/uma/uma04.png"),
          pygame.image.load("img/uma/uma05.png"),
          pygame.image.load("img/uma/uma06.png")]

index = 0


class NowLoading(Screen_abc):
    def __init__(self):
        super().__init__()

    def display(self):
        SC.screen.fill((0, 0, 0))
        SC.screen.blit(images[index])

    def getEvent(self):
        pass
