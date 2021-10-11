import pygame
from pygame.locals import *
#from Screen_abc import Screen
from TestScreen import TestScreen
from TestScreen2 import TestScreen2
import Screen_abc as SC



screen = [TestScreen(),TestScreen2()]

if __name__ == '__main__':
    while True:
        screen[SC.ScreenNum].display()
        screen[SC.ScreenNum].getEvent()


