import pygame
from pygame.locals import *
# from Screen_abc import Screen
import TestEffect
from ConfigScreen import ConfigScreen
from EffectScreen import EffectScreen
from LoadingScreen import NowLoading
from TestScreen import TestScreen
from TestScreen2 import TestScreen2
import Screen_abc as SC

screen = [TestScreen(), TestScreen2(), ConfigScreen(), NowLoading(), TestEffect.TestDisplay()]
effect_screen = EffectScreen()

if __name__ == '__main__':
    while True:
        screen[SC.ScreenNum].display()
        effect_screen.display()
        screen[SC.ScreenNum].getEvent()
