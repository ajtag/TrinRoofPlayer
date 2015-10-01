import logging
import Renderer

from Constants import MADRIX_X, MADRIX_Y, white, Lamp
from random import randint

import pygame


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
    return [i * 255 for i in colorsys.hls_to_rgb(hue / 360.0, lightness / 100.0, saturation / 100.0)]


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

        self.time = 0.0
        self.alpha = 1.0
        self.log.debug('initing sun')
        self.render()

    def render(self):
        p = pygame.PixelArray(self.image)
        d2 = self.size * self.size
        for x in range(p.shape[0]):
            for y in range(p.shape[1]):
                dx = self.size - x
                dy = self.size - y
                dist = dx * dx + dy * dy
                if dist < d2:
                    color = (255, 255 - int(255 * dist / d2), 0)
                    p[x, y] = color

    def update(self):
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
    import sys, argparse, platform, colorsys
    logging.getLogger().setLevel(logging.INFO)
    logging.basicConfig()

    parser = argparse.ArgumentParser()
    parser.add_argument("--warp", type=float, default=0.0)
    parser.add_argument("--no-mask", action="store_false", dest="mask")
    parser.add_argument("--no_images", action="store_false", dest="save_images")
    parser.add_argument("--save-video", action="store_true")
    parser.add_argument("--quick", action="store_true")
    args = parser.parse_args()

    print(args)

    if args.save_images:
        Renderer.clean_images()

    LN2015 = Renderer.Player('objects', MADRIX_X, MADRIX_Y, fps=24, display_scale=8,  args=args)

    LN2015.load_sprite("Sun", RisingSun((66, 78), (66, 51), 8, 24 * 5, 24 * 3))

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
 
