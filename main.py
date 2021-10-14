# from Screen_abc import Screen
from ConfigScreen import ConfigScreen
from LoadingScreen import NowLoading
from TestScreen import TestScreen
from TestScreen2 import TestScreen2
import Screen_abc as SC
from TestEffectScreen import TestEffectScreen
from effect import effect_group


screen = [TestScreen(), TestScreen2(), ConfigScreen(), NowLoading(), TestEffectScreen()]

if __name__ == '__main__':
    while True:
        screen[SC.ScreenNum].display()
        screen[SC.ScreenNum].getEvent()

