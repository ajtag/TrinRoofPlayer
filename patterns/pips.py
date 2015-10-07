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

SHORTPIP = 0.1
LONGPIP = 0.5

class Pips():
    def __init__(self):
        self.rect = pygame.Rect((0, 0), MADRIX_SIZE)
        self.pip_count = 0
        self.image = pygame.Surface(MADRIX_SIZE, pygame.SRCALPHA)
        self.ticks = 0

        self.solid = 0

        self.brightness = 0

        self.pips = {
            5*get_fps(): int(get_fps()*SHORTPIP),
            6*get_fps(): int(get_fps()*SHORTPIP),
            7*get_fps(): int(get_fps()*SHORTPIP),
            8*get_fps(): int(get_fps()*SHORTPIP),
            9*get_fps(): int(get_fps()*SHORTPIP),
            10*get_fps(): int(get_fps()*LONGPIP)
        }

    def draw(self, s):
        s.blit(self.image, (0, 0))

    def update(self):
        if self.ticks in self.pips:
            self.solid = self.pips.get(self.ticks)
            log.info(self.solid)
            self.brightness = 255

        if self.solid > 0:
            self.solid -= 1
        else:
            if self.brightness > 20:
                self.brightness = int(self.brightness * 0.7)
            else:
                self.brightness = 0

        log.info(self.brightness)
        self.image.fill((self.brightness, self.brightness, self.brightness))

        if self.ticks == get_fps() * 12:
            raise StopIteration
        self.ticks += 1




if __name__ == "__main__":

    logging.getLogger().setLevel(logging.INFO)
    logging.basicConfig()

    args = Renderer.cmd_line_args()

    LN2015 = Renderer.Player('objects', MADRIX_X, MADRIX_Y, fps=24, args=args)

    LN2015.load_sprite("Pips", 50, Pips())

    alive = True
    while alive:
        alive = LN2015.run()

        if 'windows' in platform.platform().lower():
            ffmpeg_exe = 'C:\\Users\\admin\\Desktop\\ffmpeg-20150921-git-74e4948-win64-static\\bin\\ffmpeg.exe'
        else:
            ffmpeg_exe = 'ffmpeg'

    LN2015.export_video(ffmpeg_exe, 12)
    LN2015.end()
sys.exit()

