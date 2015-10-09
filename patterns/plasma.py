import Renderer

from Objects import *
from utils import *
from Constants import MADRIX_X, MADRIX_Y
from pygame.math import Vector2
import pygame
from math import pi,sin
import logging

log = logging.getLogger()
logging.basicConfig()
log.setLevel(logging.INFO)


class Plasma(Sprite):
    """
        fade up for 5 seconds
        swirly shit for 31s
        fade down 5s
    """
    def __init__(self, center):
        super().__init__(MADRIX_X, MADRIX_Y)

        self.image = pygame.Surface(MADRIX_SIZE, pygame.SRCALPHA)
        self.rect = self.image.get_rect()

        self.lamps = ceiling.lamps

        self.wormhole = Vector2(bubbleroof.center)

        self.wormhole_offset = Vector2(0, 1)

        self.duration = 50
        self.ticks = 0
        self.wofticks = 0
        self.wubticks = 0
        self.fade_ticks = 0
        self.time = 0.0
        self.log.debug('initing Plasma')
        self.alpha = 0


    def update(self):

        fade_in = get_fps() * 5
        fade_out = get_fps() * 5


        seconds = self.ticks / get_fps()

        wof = self.wormhole

        if self.ticks > (get_fps() * 5) and self.ticks < (get_fps() * 27) + 9:
            log.info('wot')
            self.alpha = 255
            self.wormhole_offset.rotate_ip(7 / 3)
            self.wofticks += 1
            wof = self.wormhole + (self.wormhole_offset * (20 * sin(self.wofticks * 2 * pi / 360 / 3)))
        elif seconds > 15:
            wub = sin(self.wubticks)
            self.wubticks += 1



        # update wormhole location
        # we are going to make a spiral for Tamaki's second birthday today!... happy birthday

        if self.ticks < fade_in:
            log.info(self.alpha)
            self.alpha = min(255, self.alpha + round(255.0 / (get_fps() * 5)))

        p = pygame.PixelArray(self.image)
        for l in self.lamps:
            l = Vector2(l.x, l.y)
            d = wof.distance_to(l)

            hue = 10 * (self.ticks + d + (8 * (sin(self.wubticks / 3.0)))) % 360

            if self.ticks < (get_fps() * 31) + 9:
                color = hlsa_to_rgba(hue, 50, 100, self.alpha)
            else:
                t = self.fade_ticks / 5 * 12
                y = (128 * sin(hue * 2 * pi / 360)) + 384 - t
                color = hlsa_to_rgba(10 * (self.ticks + d + (8 * (sin(self.wubticks / 3.0)))) % 360, 50, 100, max(0, min(255, y)))

            p[int(l.x), int(l.y)] = self.image.map_rgb(color)
        del p
        self.ticks += 1
        if self.ticks >= (get_fps() * 31) + 9:
            self.fade_ticks += 1


    def draw(self, surface):
        surface.blit(self.image, self.rect)


if __name__ == "__main__":
    import sys, platform, colorsys
    logging.getLogger().setLevel(logging.INFO)
    logging.basicConfig()

    args = Renderer.cmd_line_args()
    LN2015 = Renderer.Player('plasma', MADRIX_X, MADRIX_Y, fps=24,  args=args)

    LN2015.load_sprite("Plasma", 50, Plasma((65, 51)))

    alive = True
    while alive:
        alive = LN2015.run()

        if 'windows' in platform.platform().lower():
            ffmpeg_exe = 'C:\\Users\\admin\\Desktop\\ffmpeg-20150921-git-74e4948-win64-static\\bin\\ffmpeg.exe'
        else:
            ffmpeg_exe = 'ffmpeg'

    LN2015.export_video(ffmpeg_exe, '00:00:42.9')
    LN2015.end()
sys.exit()
 
