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


class Star(Sprite):
    # TODO: shooting star

    def __init__(self, lamp):
        # Call the parent class (Sprite) constructor
        Sprite.__init__(self, 1, 1)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.rect = pygame.Rect(lamp.x, lamp.y, 1, 1)

        self.color = white
        self.rand_color()

        self.lamp = lamp

        self.log.debug('created star at {},{}'.format(lamp.x, lamp.y))

    def rand_color(self):
        self.color = hls_to_rgb(randint(40, 60), randint(20, 100), randint(80, 100))

    def update(self):
        self.rand_color()
        self.image.set_at((0, 0), self.color)


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

    LN2015.load_sprite("STARS", Star(Lamp(67, 50)))

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
 
