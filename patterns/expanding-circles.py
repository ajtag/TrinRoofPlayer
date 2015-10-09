__author__ = 'ultrafez'

import random
from collections import namedtuple
import logging

import pygame

from Constants import *
from utils import *
from Objects import *
import sys
import platform
import Renderer
from Renderer import get_fps

log = logging.getLogger()
logging.basicConfig()
log.setLevel(logging.INFO)

Thread = namedtuple('Thread', ('start', 'direction', 'hue', 'width', 'age'))

transparent = 255, 255, 255, 0


class Circle(Sprite):
    def __init__(self, pos, color):
        super().__init__()
        self.pos = pos
        self.color = color
        self.radius = 0
        self.thickness = 10
        self.s = pygame.Surface(MADRIX_SIZE, flags=pygame.SRCALPHA)

    def update(self):
        self.radius += 1
        if self.radius > (MADRIX_X*1.5 + self.thickness*2):
            # it'll definitely be off-screen at this point
            self.kill()

    def draw(self, surface):
        self.s.fill(transparent)
        pygame.draw.circle(self.s, self.color, self.pos, int(self.radius))
        if self.radius > self.thickness:
            pass
            pygame.draw.circle(self.s, transparent, self.pos, int(self.radius - self.thickness))

        surface.blit(self.s, (0, 0))


class CircleGen(Group):
    def __init__(self):
        super().__init__()
        self.rand.seed(1516)
        self.time = 0
        self.addBlob()
        
    def update(self):
        super().update()

        if self.time % 15 == 0:
            self.addBlob()

        self.time += 1

    def addBlob(self):
        pos = self.rand.choice(ceiling.lamps)
        col = hls_to_rgb(self.rand.randint(0, 360), 50, 100)
        self.add(Circle(pos, col))

    def draw(self, surface):
        # surface.fill(black)
        for blob in self:
            blob.draw(surface)

    def end(self):
        pass


if __name__ == "__main__":

    logging.getLogger().setLevel(logging.INFO)
    logging.basicConfig()

    args = Renderer.cmd_line_args()

    LN2015 = Renderer.Player('CircleGen', MADRIX_X, MADRIX_Y, fps=24, args=args)

    LN2015.load_sprite("CIRCLEGEN", 50, CircleGen())

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

