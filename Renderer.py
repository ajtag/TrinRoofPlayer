__author__ = 'ajtag'

import subprocess as sp
import glob
import pygame
import logging
from Constants import *
import os
import math
import random

pygame.font.init()
FONT = pygame.font.Font(None, 24)

_fps = None
def get_fps():
    return _fps

random_seed = str(random.random())
def new_random(name):
    return random.Random(random_seed + name)

class Trigger(object):
    """Create a new Group, or run a method on an existing group"""
    def __init__(self, scene, method=None, *args):
        self.scene = scene
        self.method = method
        self.args = args

    def __repr__(self):
        return "Trigger(%s,%s,%s)" % (self.scene, self.method, self.args)


def clean_images():
    # delete any files saved from previous runs
    [os.unlink(i) for i in glob.glob(os.path.join('images', '*.bmp'))]


class Player:
    log = logging.getLogger('Player')

    def __init__(self, title, width, height, display_scale=1, fps=24, args=()):
        pygame.init()
        global _fps
        _fps = fps
        try:
            global random_seed
            random_seed = args.random_seed
        except AttributeError:
            pass
        self.title = title
        self.width = width
        self.height = height
        self.size = (width, height)
        self.display_scale = display_scale
        self.lightmask = args.mask
        self.mask = pygame.Surface(self.size)
        self.mask.fill(dark_grey)
        self.mask.set_colorkey(white)
        for x, y in ceiling.lamps:
            self.mask.set_at((x, y), white)
        self.screen = pygame.Surface(self.size)
        self.display = pygame.display.set_mode((display_scale * width, display_scale * height))
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.pause = args.pause
        self.step = False
        self.objects = {}
        self.ticks = 0
        self.background = black
        self.save_images = args.save_images
        self.save_video = args.save_video
        self.cursor_loc_start = None
        self.cursor_loc_end = None
        self.warp = int(self.fps * args.warp)
        if self.warp >= 0 and (self.save_images or self.save_video):
            raise Exception("Can not save when warping")
        if self.warp < 0:
            self.warp = None
        self.quick = args.quick
        self.sparse = args.sparse
        if self.sparse > self.display_scale:
            raise Exception("Pixels bigger than screen")

        self.scene_data = {}
        self.scene_layer = {}

        self.key_triggers = {}
        self.timed_events = {}

        self.log.info('done init')

    def set_key_triggers(self, key, trig):
        self.key_triggers[key] = trig

    def load_sprite(self, name, layer, sprite):
        self.scene_layer[name] = layer
        self.objects[name] = sprite

    def load_scene(self, scene_name, layer, *scene_data):
        self.scene_data[scene_name] = scene_data
        self.scene_layer[scene_name] = layer

    def load_timed_event(self, time, events):
        ticks = int(time * self.fps)
        current_events = self.timed_events.get(ticks, [])
        if isinstance(events, Trigger):
            current_events.append(events)
        else:
            for e in events:
                current_events.append(e)
        self.timed_events[ticks] = current_events

    def export_video(self, x, y, ffmpeg_exe='ffmpeg'):
        command = [ffmpeg_exe,
               '-y',  # (optional) overwrite output file if it exists
               '-r', '{}'.format(self.fps),  # frames per second
               '-i', os.path.join('images', '{}_%d.bmp'.format(self.title)),
               '-s', '{}x{}'.format(x, y),
               '-an',  # Tells FFMPEG not to expect any audio
                '-c:v', 'qtrle',
               '-tune', 'animation',
                '-q', '0',
               '-s', '{}x{}'.format(x, y),  # size of one frame
               '{}.mov'.format(self.title)
               ]
        self.log.info(' '.join(command))

        if not self.save_video:
            return

        sp.call(command)

    def run_trigger(self, trigger):
        if trigger.method is None:
            try:
                d = self.scene_data[trigger.scene]
            except:
                self.log.error("No such scene '%s'" % trigger.scene)
                return
            try:
                self.objects[trigger.scene] = d[0](*d[1:])
            except:
                self.log.error("Failed to create '%s' %s" % (trigger.scene, d))
                raise
        else:
            try:
                try:
                    o = self.objects[trigger.scene]
                except KeyError:
                    self.log.error("Scene '%s' not running" % trigger.scene)
                    return
                getattr(o, trigger.method)(*trigger.args)
            except StopIteration:
                del self.objects[trigger.scene]
            except:
                self.log.error("%s" % (trigger))
                raise

    def sparse_blit(self):
        self.display.fill(0)
        scale = int(self.display_scale)
        width = self.sparse
        offset = (scale - width) // 2
        dest = pygame.PixelArray(self.display)
        src = pygame.PixelArray(self.screen)



        if not(self.lightmask):
            lamps = []
            for i in range(self.size[0]):
                for j in range(self.size[1]):
                    lamps.append(Lamp(i,j))
        else:
            lamps = ceiling.lamps

        for lamp in lamps:
            base_x = lamp.x * scale + offset
            base_y = lamp.y * scale + offset
            for x in range(self.sparse):
                for y in range(self.sparse):
                    dest[base_x + x, base_y + y] = src[lamp.x, lamp.y]

    def run(self):
        for event in pygame.event.get():

            # Check for quit
            if event.type == pygame.QUIT:
                return False
            # Mouse events
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # left start click
                self.cursor_loc_start = event.pos
                self.cursor_loc_end = None

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # left finish click
                self.cursor_loc_end = event.pos
                print('pygame.Rect({}, {}, {}, {})'.format(
                        math.floor(min(self.cursor_loc_start[0], self.cursor_loc_end[0])/self.display_scale),
                        math.floor(min(self.cursor_loc_start[1], self.cursor_loc_end[1])/self.display_scale),
                        math.floor((max(self.cursor_loc_end[0], self.cursor_loc_start[0]) - min(self.cursor_loc_end[0], self.cursor_loc_start[0]))/self.display_scale),
                        math.floor((max(self.cursor_loc_start[1], self.cursor_loc_end[1]) - min(self.cursor_loc_start[1], self.cursor_loc_end[1]))/self.display_scale)
                     )
             )

            if event.type == pygame.MOUSEBUTTONUP and event.button == 3:  # right click
                self.cursor_loc_start = None
                self.cursor_loc_end = None

            # Check Keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False

                elif event.key == pygame.K_HASH:
                    if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
                        self.log.info('Verbose Output Off')
                        logging.getLogger().setLevel(logging.INFO)
                    else:
                        self.log.info('Verbose Output On')
                        logging.getLogger().setLevel(logging.DEBUG)

                elif event.key == pygame.K_SLASH:
                    self.log.info('''
/  - help
#  - print key triggers
F1 - save video on exit
F2 - view mask
F3 - toggle fps limiter
F4 - play/pause
F5 - step frame

esc - quit

========================================================
''')
                    for k,t in self.key_triggers.items():
                        self.log.info('{} -  {}'.format(chr(k), t))

                elif event.key == pygame.K_F4:
                    self.pause = not(self.pause)
                    self.log.info('pause video: {}'.format(self.pause))

                elif event.key == pygame.K_F5:
                    self.step = True

                elif event.key == pygame.K_F1:
                    self.save_video = not self.save_video
                    self.log.info('save video: {}'.format(self.save_video))

                elif event.key == pygame.K_F2:
                    self.lightmask = not self.lightmask
                    self.log.info('Mask: {}'.format(self.lightmask))

                elif event.key == pygame.K_F3:
                    self.quick = not self.quick
                    self.log.info('FPS de-limiter: {}'.format(self.quick))

                if event.key in self.key_triggers:
                    self.log.debug('pressed {}'.format(event.key))
                    self.run_trigger(self.key_triggers[event.key])




        running = not self.pause
        if self.step or self.warp is not None:
            running = True
        if running:
            self.background = black
            self.screen.fill(self.background)
            for e in self.timed_events.get(self.ticks, []):
                self.run_trigger(e)

            if self.warp is not None and self.ticks == self.warp:
                self.log.info("Warp finished")
                self.warp = None

            draw = (self.warp is None) or (self.ticks % (2 * self.fps) == 0)
            remove = []
            items = [(k,v) for k,v in self.scene_layer.items() if k in self.objects.keys()]

            items.sort(key=lambda ele: ele[1])
            for name, layer in items:
                element = self.objects[name]
                try:
                    element.update()
                    if draw:
                        try:
                            drawfn = element.draw
                        except AttributeError:
                            self.screen.blit(element.image, element.rect.topleft)
                        else:
                            drawfn(self.screen)
                except StopIteration:
                    remove.append(name)
                except:
                    self.log.error('Error while drawing {}'.format(name))
                    raise
            for name in remove:
                del self.objects[name]

            self.step = False
            self.ticks += 1
        else:
            draw = True



        if draw:
            if self.sparse == 0:
                if self.lightmask:
                    pygame.Surface.blit(self.screen, self.mask, (0, 0))
                pygame.transform.scale(self.screen, self.display.get_size(), self.display)
            else:
                self.sparse_blit()

            #  draw a red rect overlay to the display surface by dragging the mouse
            if self.cursor_loc_start is not None:
                i, j = self.cursor_loc_start
                if self.cursor_loc_end is None:
                    x, y = pygame.mouse.get_pos()
                else:
                    x, y = self.cursor_loc_end
                r = pygame.Rect((min(i, x), min(j, y)), (max(i, x) - min(i, x), max(j, y) - min(j, y)))
                pygame.draw.rect(self.display, (255, 0, 0), r, 2)

            self.display.blit(FONT.render('{:.2f}/{:0} fps'.format(self.clock.get_fps(), self.fps), False, (255, 0, 0), ), (10,10))
            self.display.blit(FONT.render('{:.2f}'.format(
                    self.ticks/self.fps
                ), False, (255, 0, 0),), (10,45))

            pygame.display.flip()

        if self.save_images:
            savepath = os.path.join('images')

            if not (os.path.isdir(savepath)):
                os.mkdir(savepath)

            savefile = os.path.join('images', '{}_{}.bmp'.format(self.title, self.ticks))
            pygame.image.save(self.screen, savefile)

        if draw:
            if self.quick or self.warp is not None:
                self.clock.tick()
            else:
                self.clock.tick(self.fps)

        return True


    def end(self):
        pygame.quit()
