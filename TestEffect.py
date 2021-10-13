import sys

import pygame
from pygame.locals import *

import EffectScreen
import Screen_abc as SC
from Screen_abc import Screen_abc


class TestDisplay(Screen_abc):

    def __init__(self):
        super(TestDisplay, self).__init__()
        self.x_location = 100
        self.y_location = 100

    def display(self):
        SC.screen.fill((0, 0, 0))
        super().update(5)

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
                    EffectScreen.effect_instance.add(EffectScreen.SampleEffect(self.x_location, self.y_location))

                if event.key == K_UP:
                    self.y_location -= 30
                if event.key == K_DOWN:
                    self.y_location += 30
                if event.key == K_LEFT:
                    self.x_location -= 30
                if event.key == K_RIGHT:
                    self.x_location += 30
