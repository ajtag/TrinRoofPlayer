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
import random

log = logging.getLogger()
logging.basicConfig()
log.setLevel(logging.INFO)

FONT = pygame.font.Font(None, 24)

neighbours = []
for i in (-1, 0, 1):
    for j in (-1, 0, 1):
        if i==0 and j ==0:
            pass
        else:
            neighbours.append ((i, j))

class GOL():
    def __init__(self):
        self.rect = pygame.Rect((0, 0), MADRIX_SIZE)
        self.image = pygame.Surface(MADRIX_SIZE)
        self.tomorrow = pygame.Surface(MADRIX_SIZE)
        self.ticks = 0

        self.alive = 0
        for lamp in ceiling.lamps:
            if random.randint(0, 100) < (300 / 8):
                self.image.set_at((lamp.x, lamp.y), white)
                self.alive += 1
        log.info(self.alive)

    def draw(self, s):
        s.blit(self.image, (0, 0))

    def update(self):
        self.tomorrow.fill(black)
        im = pygame.PixelArray(self.image)
        t = pygame.PixelArray(self.tomorrow)

        for lamp in ceiling.lamps:
            if random.randint(0, 100) < 0.1 * (300 / 8):
                    self.image.set_at((lamp.x, lamp.y), white)
                    self.alive += 1


        self.alive = 0

        for lamp in ceiling.lamps:
            live = False
            next_to = 0

            for neighbour in neighbours:
                try:
                    if im[lamp.x, lamp.y] > 0x80:
                        live = True
                    if im[lamp.x + neighbour[0], lamp.y + neighbour[1]] > 0x808080:
                        next_to += 1
                except IndexError:
                    log.error(('error', (lamp.x, lamp.y)))
                    if lamp.x * lamp.y >= 0:
                        raise


            if next_to > 3:
                # kill
                t[lamp.x, lamp.y] = black
            elif next_to == 3:
                # stay or birth
                t[lamp.x, lamp.y] = white
                self.alive += 1
            elif next_to == 2 and live:
                # stay
                t[lamp.x, lamp.y] = white
                self.alive += 1
            else:
                t[lamp.x, lamp.y] = black
        #    log.info((next_to, live))

        del im
        del t

        t = self.image
        self.image = self.tomorrow
        self.tomorrow = t

        self.ticks += 1


if __name__ == "__main__":

    logging.getLogger().setLevel(logging.INFO)
    logging.basicConfig()

    args = Renderer.cmd_line_args()

    LN2015 = Renderer.Player('gameoflife', MADRIX_X, MADRIX_Y, fps=24, args=args)

    LN2015.load_sprite("gameoflife", 50, GOL())

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

