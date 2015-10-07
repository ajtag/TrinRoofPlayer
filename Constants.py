__author__ = 'ajtag'

from  pygame import Rect
import collections
import csv
import os.path

MADRIX_X = 132
MADRIX_Y = 70
MADRIX_SIZE = (MADRIX_X, MADRIX_Y)

white = 255, 255, 255, 0xff
black = 0, 0, 0, 0xff
red = 255, 0, 0, 0xff
green = 0, 255, 0, 0xff
blue = 0, 0, 255, 0xff
dark_grey = 0x30, 0x30, 0x30, 0xff
transparent = 0xff, 0xff, 0xff, 0xff

bubbleroof = Rect((50, 34), (28, 33))
island = Rect((0, 41), (12, 7))

left_arm = Rect(16, 37, 37, 14)
left_outer_arm = Rect((16, 42), (18, 8))
left_inner_arm = Rect((33, 37), (21, 14))

top_arm = Rect(60, 0, 12, 36)
top_outer_arm = Rect((57, 0), (12, 18))
top_inner_arm = Rect((60, 18), (9, 18))

right_arm = Rect(77, 39, 51, 12)
right_inner_arm = Rect((78, 39), (20, 13))
right_outer_arm = Rect((98, 40), (33, 11))

offscreen = [
        Rect((0, 0), (62, 39)),
        Rect((71, 0), (57, 40)),
        Rect((0, 50), (53, 20)),
        Rect((80, 52), (52, 18)),
]

Lamp = collections.namedtuple("Lamp", ["x", "y"])

def readlamps(filename):
    # Generate array of lights fixture locations
    lamps = []
    f = open(filename)
    csv_f = csv.DictReader(f)
    for row in csv_f:
        # Adjusted XY coordinates -1 as Madrix counts from 1
        lamps.append(Lamp(int(row['X']) - 1, int(row['Y']) - 1))
    return lamps

class Ceiling:
    def __init__(self, spawn_filename, render_filename):
        self.lamps = readlamps(render_filename)
        spawn_lamps = readlamps(spawn_filename)
        self.bubbleroof_lamps = list(filter(lambda lamp: bubbleroof.collidepoint(lamp.x, lamp.y), spawn_lamps))


ceiling = Ceiling(os.path.join('Resources', 'pixels_rework.csv'), os.path.join('Resources', 'pixels_mapped.csv'))
