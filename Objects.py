__author__ = 'ajtag'

from Renderer import *


class Sprite(pygame.sprite.Sprite):
    def __init__(self, x=None, y=None, surface_flags=0):
        self.log = logging.getLogger(self.__class__.__name__)
        super().__init__()
        if x is not None:
            self.image = pygame.Surface((abs(x), abs(y)), surface_flags)
            self.image.set_colorkey(white)
            self.image.fill(white)
        self.log.debug('##init##')
        self.ticks = 0


class Group(pygame.sprite.Group):
    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)
        super().__init__()
        self.rand = new_random(self.__class__.__name__)

    def end(self):
        raise StopIteration


class MoveableThing(Group):
    def __init__(self, pos, size, fade_duration):
        super().__init__()
        self.x = float(pos[0])
        self.y = float(pos[1])
        self.dx = 0.0
        self.dy = 0.0
        self.steps = 0
        self.size = size
        self.size_speed = 0

        if fade_duration is not None:
            self.fade = 0.0
            self.fade_speed = 1.0 / (get_fps() * fade_duration)
        else:
            self.fade = 1.0
            self.fade_speed = None

    def update(self):
        if self.steps > 0:
            self.steps -= 1
            self.x += self.dx
            self.y += self.dy
            self.size += self.size_speed
        if self.fade_speed is not None:
            self.fade += self.fade_speed
            if self.fade_speed > 0.0 and self.fade >= 1.0:
                self.fade = 1.0;
                self.fade_speed = None
            elif self.fade_speed < 0.0 and self.fade <= 0.0:
                raise StopIteration

    def move(self, newpos, newsize, duration=None):
        if duration is None:
            self.steps = 1
        else:
            self.steps = max(int(duration * get_fps()), 1)
        if newpos is None:
            self.dx = 0.0
            self.dy = 0.0
        else:
            self.dx = (newpos[0] - self.x) / self.steps
            self.dy = (newpos[1] - self.y) / self.steps
        if newsize is None:
            self.size_speed = 0
        else:
            self.size_speed = (newsize - self.size) / self.steps

    def end(self, fade_duration=None):
        if fade_duration is None:
            raise StopIteration
        else:
            self.fade_speed = -1.0 / (get_fps() * fade_duration)
