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

log = logging.getLogger()
logging.basicConfig()
log.setLevel(logging.INFO)

Thread = namedtuple('Thread', ('start', 'direction', 'hue', 'width', 'age'))


class Whizz():
    def __init__(self, threadcount):
        self.rect = pygame.Rect((0, 0), MADRIX_SIZE)
        self.threadcount = 20
        self.threadrate_init = 5
        self.threadrate = 0
        self.image = pygame.Surface(MADRIX_SIZE, pygame.SRCALPHA)
        self.ticks = 0
        self.max_age = 50
        self.speed = self.max_age/200
        self.threads = []

    def draw(self, s):
        s.blit(self.image, (0, 0))

    def update(self):
        self.ticks += 1
        if len(self.threads) < self.threadcount:
            if self.threadrate > 0:
                self.threadrate = self.threadrate - 1
            else:
                self.threadrate = self.threadrate_init
                # find a vector not in the roof
                start = Vector2(65, 51)

                offset = Vector2(0, 0)
                offset.from_polar((MADRIX_X/2, random.randrange(360)))
                start = start + offset
                offset.scale_to_length(random.randint(3, 9))
                direction = offset.rotate(random.randrange(-5, 5))

                width = random.random() * 3
                hue = (random.randrange(30) + self.ticks) % 360
                t = Thread(start, direction, hue, width, 0)
                log.debug(('add', t))
                self.threads.append(t)


        self.image.fill((0, 0, 0, 0))
        px = pygame.PixelArray(self.image)

        new_threads = []
        for threadi in self.threads:

            # update location
            new_start = threadi.start - threadi.direction
            new_age = threadi.age + 1
            new_direction = threadi.direction.rotate(0)
            if new_age > self.max_age:
                log.debug(('del', threadi, new_start))
                continue

            thread = Thread(new_start, new_direction, threadi.hue, threadi.width, new_age)
            new_threads.append(thread)

            # draw onto surface
            for i in range(-int(2*thread.width), round(abs(thread.direction.x)+2*thread.width)):
                if new_start.x + i > self.rect.width + self.rect.left \
                        or new_start.x + i < 0:
                        continue
                for j in range(-int(2*thread.width), round(abs(thread.direction.y)+2*thread.width)):
                    if new_start.y + j > self.rect.height + self.rect.top \
                            or new_start.y + j < 0:
                        continue

                    p = Vector2(i, j)
                    d = dist_Point_to_Segment(p, (Vector2(0, 0), thread.direction))
                    dp = thread.direction.dot(p)
                    a = thread.direction.angle_to(p)
                    point_to_direction = (thread.direction - p).length()


                    if d < thread.width:
                        alpha = 255

                        alpha = alpha * (1-(Vector2(i, j).length_squared()/thread.direction.length_squared()))
                        if abs(a) > 90:
                            if thread.width > point_to_direction:
                                alpha = 0.3/(thread.width-point_to_direction)
                            else:
                                alpha = 0
                        #alpha = alpha * a
                        alpha = alpha * (1-(d / thread.width))

                        # bound alpha to valid values
                        alpha = max(0, min(255, alpha))

                        lightness = min(50*(thread.width/(1+p.distance_to(thread.direction))), 50)
                        log.info(lightness)
                        color = hlsa_to_rgba(threadi.hue, 50 + lightness, 100, alpha)
                        try:
                            px[int(i + new_start.x), int(j + new_start.y)] = self.image.map_rgb(color)
                        except:
                            log.error(thread, color)
                            raise


        self.threads = new_threads
        del px

if __name__ == "__main__":

    logging.getLogger().setLevel(logging.INFO)
    logging.basicConfig()

    args = Renderer.cmd_line_args()

    LN2015 = Renderer.Player('objects', MADRIX_X, MADRIX_Y, fps=24, args=args)

    LN2015.load_sprite("whizz", 50, Whizz(5))

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

