import pygame
from pygame.locals import *

from Screen_abc import Screen_abc
import Screen_abc as SC
import sys

from effect import *


class TestEffectScreen(Screen_abc):
    def __init__(self):
        super(TestEffectScreen, self).__init__()
        self.x_location = 100
        self.y_location = 100

    def display(self):
        SC.screen.fill((0, 0, 0))
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

                if event.key == K_SPACE:
                    effect_group.add(UmaEffect())
                if event.key == K_RIGHT:
                    self.x_location += 20
                    effect_group.add(IceEffect(self.x_location, self.y_location))
                if event.key == K_DOWN:
                    self.y_location += 10
                    effect_group.add(CircleEffect(self.x_location,self.y_location))
                if event.key == K_1:
                    effect_group.add(ScreenLineEffect("Test Effect"))

