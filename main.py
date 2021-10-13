import pygame
from pygame.locals import *
# from Screen_abc import Screen
from ConfigScreen import ConfigScreen
from EffectScreen import EffectScreen
from LoadingScreen import NowLoading
from TestScreen import TestScreen
from TestScreen2 import TestScreen2
import Screen_abc as SC

screen = [TestScreen(), TestScreen2(), ConfigScreen(), NowLoading()]
effect_screen = EffectScreen()

if __name__ == '__main__':
    while True:
        screen[SC.ScreenNum].display()
        screen[SC.ScreenNum].getEvent()
        effect_screen.display()
