__author__ = 'ajtag'

import random
from collections import namedtuple
import logging

import pygame
from pygame.math import Vector2

from Constants import *
from utils import *
import sys
import platform
import Renderer
import math
from Renderer import get_fps

log = logging.getLogger()
logging.basicConfig()
log.setLevel(logging.INFO)

Thread = namedtuple('Thread', ('start', 'direction', 'hue', 'width', 'age'))

FONT = pygame.font.Font(None, 24)


class Lamps():
    def __init__(self):
        self.rect = pygame.Rect((0, 0), MADRIX_SIZE)
        self.image = pygame.Surface(MADRIX_SIZE, pygame.SRCALPHA)
        self.ticks = 0
        self.solid = 0


        self.lamps = ceiling.lamps
        self.lamps.sort(key=lambda l: l.y*132 + l.x)
        self.lampid = 0


    def draw(self, s):
        s.blit(self.image, (0, 0))

    def update(self):

        if self.ticks % 6 == 0:
            self.image.fill(black)
            lamp = self.lamps[self.lampid]
            self.image.set_at((lamp.x, lamp.y), white)
            self.lampid = (self.lampid + 1) % len(self.lamps)
            self.image.blit(FONT.render('{}x{}'.format(lamp.x, lamp.y),  False, (255, 0, 0),), (2,5))

        self.ticks += 1


if __name__ == "__main__":

    logging.getLogger().setLevel(logging.INFO)
    logging.basicConfig()

    args = Renderer.cmd_line_args()

    LN2015 = Renderer.Player('lamps', MADRIX_X, MADRIX_Y, fps=24, args=args)

    LN2015.load_sprite("Lamps", 50, Lamps())

    alive = True
    while alive:
        alive = LN2015.run()

        if 'windows' in platform.platform().lower():
            ffmpeg_exe = 'C:\\Users\\admin\\Desktop\\ffmpeg-20150921-git-74e4948-win64-static\\bin\\ffmpeg.exe'
        else:
            ffmpeg_exe = 'ffmpeg'

    LN2015.export_video(ffmpeg_exe)
    LN2015.end()
sys.exit()

