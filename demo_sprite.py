import logging
import Renderer

from Constants import MADRIX_X, MADRIX_Y, white, Lamp
from random import randint

import pygame
import math


class Sprite(pygame.sprite.Sprite):
    def __init__(self, x=None, y=None):
        self.log = logging.getLogger(self.__class__.__name__)
        pygame.sprite.Sprite.__init__(self)
        if x is not None:
            self.image = pygame.Surface((x, y))
            self.image.set_colorkey(white)
            self.image.fill(white)
        self.log.debug('##init##')


def hls_to_rgb(hue, lightness, saturation):
    """
    :param hue: 0-360
    :param lightness:  0-100
    :param saturation:  0-100
    :return: list
    """
    return [int(i * 255) for i in colorsys.hls_to_rgb(hue / 360.0, lightness / 100.0, saturation / 100.0)]


class RisingSun(Sprite):
    def __init__(self, start, end, size, duration, fade):
        super().__init__(size * 2, size * 2)

        self.start = start
        self.move_x = end[0] - start[0]
        self.move_y = end[1] - start[1]
        self.size = size
        self.rect = self.image.get_rect()
        self.duration = duration
        self.fade = 1.0 / fade

        self.ticks = 0
        self.time = 0.0
        self.alpha = 1.0
        self.log.debug('initing sun')


    def update(self):
        p = pygame.PixelArray(self.image)
        d2 = self.size
        for x in range(p.shape[0]):
            for y in range(p.shape[1]):
                dx = self.size - x
                dy = self.size - y
                dist = math.sqrt(dx * dx + dy * dy)
                if dist < d2:
                    color = hls_to_rgb( 10* (self.ticks + dist) % 360, 50, 100)
                    p[x, y] = self.image.map_rgb(color)
        del p

        self.ticks += 1
        if self.time < 1.0:
            self.time += 1.0 / self.duration
            x = self.start[0] + self.time * self.move_x
            y = self.start[1] + self.time * self.move_y
            self.rect.center = (x, y)
        else:
            self.time = 1.0
            self.alpha -= self.fade
            if self.alpha < 0.0:
                raise StopIteration
            self.image.set_alpha(255 * self.alpha)

    def draw(self, surface):
        surface.blit(self.image, self.rect)




if __name__ == "__main__":
    import sys, platform, colorsys
    logging.getLogger().setLevel(logging.INFO)
    logging.basicConfig()

    args = Renderer.cmd_line_args()


    LN2015 = Renderer.Player('objects', MADRIX_X, MADRIX_Y, fps=24,  args=args)

    LN2015.load_sprite("Sun", 50, RisingSun((66, 51), (66, 51), 50, 24 * 50, 24 * 30))

    alive = True
    while alive:
        alive = LN2015.run()

        if 'windows' in platform.platform().lower():
            ffmpeg_exe = 'C:\\Users\\admin\\Desktop\\ffmpeg-20150921-git-74e4948-win64-static\\bin\\ffmpeg.exe'
        else:
            ffmpeg_exe = 'ffmpeg'

    LN2015.export_video(MADRIX_X, MADRIX_Y, ffmpeg_exe)
    LN2015.end()
sys.exit()
 
