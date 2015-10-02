__author__ = 'ajtag'

import pygame
import collections
import csv

MADRIX_X = 132
MADRIX_Y = 70

white = 255, 255, 255, 0xff
black = 0, 0, 0, 0xff
red = 255, 0, 0, 0xff
green = 0, 255, 0, 0xff
blue = 0, 0, 255, 0xff
dark_grey = 0x30, 0x30, 0x30, 0xff
transparent = 0xff, 0xff, 0xff, 0xff

bubbleroof = pygame.Rect((50, 34), (28, 33))
island = pygame.Rect((0, 41), (12, 7))
left_arm = pygame.Rect(16, 37, 37, 14)
left_outer_arm = pygame.Rect((16, 42), (18, 8))
left_inner_arm = pygame.Rect((33, 37), (16, 13))
top_outer_arm = pygame.Rect((61, 1), (0, 18))
top_inner_arm = pygame.Rect((60, 18), (9, 18))
top_arm = pygame.Rect(60, 0, 12, 36)
right_inner_arm = pygame.Rect((77, 40), (21, 12))
right_outer_arm = pygame.Rect((97, 40), (28, 12))
right_arm = pygame.Rect(77, 39, 51, 12)

Lamp = collections.namedtuple("Lamp", ["x", "y"])

def hardcoded_lamps():
    return (Lamp(58, 59), Lamp(65, 65),
    Lamp(18, 47), Lamp(18, 45), Lamp(18, 43), Lamp(19, 44), Lamp(19, 45), Lamp(19, 46), Lamp(20, 47), Lamp(20, 46),
    Lamp(20, 45), Lamp(21, 44), Lamp(21, 45), Lamp(21, 46), Lamp(22, 45), Lamp(22, 43), Lamp(23, 44), Lamp(23, 45),
    Lamp(23, 46), Lamp(24, 47), Lamp(24, 45), Lamp(24, 44), Lamp(25, 44), Lamp(25, 45), Lamp(25, 46), Lamp(26, 45),
    Lamp(26, 43), Lamp(27, 44), Lamp(27, 45), Lamp(27, 46), Lamp(28, 47), Lamp(28, 46), Lamp(28, 45), Lamp(29, 44),
    Lamp(29, 45), Lamp(29, 46), Lamp(30, 45), Lamp(30, 44), Lamp(30, 43), Lamp(31, 44), Lamp(31, 45), Lamp(31, 46),
    Lamp(32, 47), Lamp(32, 45), Lamp(33, 44), Lamp(33, 45), Lamp(33, 46), Lamp(34, 43), Lamp(36, 48), Lamp(36, 47),
    Lamp(36, 46), Lamp(36, 45), Lamp(37, 44), Lamp(37, 45), Lamp(37, 46), Lamp(37, 47), Lamp(37, 48), Lamp(38, 49),
    Lamp(38, 48), Lamp(38, 47), Lamp(38, 46), Lamp(38, 45), Lamp(38, 44), Lamp(39, 48), Lamp(39, 47), Lamp(39, 46),
    Lamp(39, 45), Lamp(39, 44), Lamp(39, 43), Lamp(40, 48), Lamp(40, 47), Lamp(40, 46), Lamp(40, 45), Lamp(40, 44),
    Lamp(41, 48), Lamp(41, 47), Lamp(41, 46), Lamp(41, 45), Lamp(41, 44), Lamp(41, 43), Lamp(42, 44), Lamp(42, 45),
    Lamp(42, 46), Lamp(42, 47), Lamp(42, 48), Lamp(43, 43), Lamp(43, 44), Lamp(43, 45), Lamp(43, 46), Lamp(43, 47),
    Lamp(43, 48), Lamp(44, 48), Lamp(44, 47), Lamp(44, 46), Lamp(44, 45), Lamp(44, 44), Lamp(45, 43), Lamp(45, 44),
    Lamp(45, 45), Lamp(45, 46), Lamp(45, 47), Lamp(45, 48), Lamp(46, 49), Lamp(46, 48), Lamp(46, 47), Lamp(46, 46),
    Lamp(46, 45), Lamp(46, 44), Lamp(47, 43), Lamp(47, 44), Lamp(47, 45), Lamp(47, 46), Lamp(47, 47), Lamp(47, 48),
    Lamp(48, 49), Lamp(48, 48), Lamp(48, 47), Lamp(48, 46), Lamp(48, 45), Lamp(48, 44), Lamp(49, 43), Lamp(49, 44),
    Lamp(49, 45), Lamp(49, 46), Lamp(49, 47), Lamp(49, 48), Lamp(126, 43),Lamp(126, 46),Lamp(126, 47),Lamp(126, 48),
    Lamp(126, 49),Lamp(126, 50), Lamp(125, 50), Lamp(125, 49),Lamp(125, 48), Lamp(125, 47),Lamp(125, 46), Lamp(125, 45),
    Lamp(124, 43), Lamp(124, 45),Lamp(124, 46), Lamp(124, 47),Lamp(124, 48), Lamp(124, 49),Lamp(123, 49), Lamp(123, 48),
    Lamp(123, 47), Lamp(123, 46),Lamp(123, 44), Lamp(122, 43),Lamp(122, 46), Lamp(122, 47),Lamp(122, 48), Lamp(121, 48),
    Lamp(121, 47), Lamp(121, 46),Lamp(121, 45), Lamp(120, 44),Lamp(120, 46), Lamp(120, 48),Lamp(119, 45), Lamp(119, 46),
    Lamp(119, 47), Lamp(119, 48),Lamp(118, 43), Lamp(118, 46),Lamp(118, 48), Lamp(117, 48),Lamp(117, 47), Lamp(117, 46),
    Lamp(117, 45), Lamp(116, 46),Lamp(116, 48), Lamp(116, 44), Lamp(115, 45), Lamp(115, 46),Lamp(115, 47), Lamp(114, 48),
    Lamp(114, 46), Lamp(114, 43),Lamp(113, 45), Lamp(113, 46), Lamp(113, 47), Lamp(112, 46), Lamp(112, 44), Lamp(111, 45),
    Lamp(111, 46), Lamp(111, 47), Lamp(110, 48), Lamp(110, 46),
    Lamp(110, 43), Lamp(109, 45), Lamp(109, 46), Lamp(109, 47), Lamp(108, 46), Lamp(108, 44), Lamp(107, 45), Lamp(107, 46),
    Lamp(107, 47), Lamp(106, 48), Lamp(106, 46), Lamp(106, 44), Lamp(106, 43), Lamp(105, 45), Lamp(105, 46), Lamp(105, 47),
    Lamp(104, 48), Lamp(104, 46), Lamp(104, 44), Lamp(103, 45), Lamp(103, 46), Lamp(103, 47), Lamp(102, 48), Lamp(102, 46),
    Lamp(102, 44), Lamp(102, 43), Lamp(101, 45), Lamp(101, 46), Lamp(101, 47), Lamp(100, 48), Lamp(100, 46), Lamp(100, 44),
    Lamp(99, 45), Lamp(99, 46), Lamp(99, 47), Lamp(97, 48), Lamp(97, 46), Lamp(97, 44), Lamp(97, 42), Lamp(96, 43),
    Lamp(96, 45), Lamp(96, 46), Lamp(96, 47), Lamp(96, 49), Lamp(95, 48), Lamp(95, 46), Lamp(95, 44), Lamp(95, 41),
    Lamp(94, 43), Lamp(94, 45), Lamp(94, 46), Lamp(94, 47), Lamp(94, 49), Lamp(93, 48), Lamp(93, 46), Lamp(93, 44),
    Lamp(93, 42), Lamp(92, 43), Lamp(92, 45), Lamp(92, 46), Lamp(92, 47), Lamp(92, 49), Lamp(91, 48), Lamp(91, 46),
    Lamp(91, 43), Lamp(91, 42), Lamp(90, 43), Lamp(90, 45), Lamp(90, 46), Lamp(90, 47), Lamp(90, 49), Lamp(89, 50),
    Lamp(89, 48), Lamp(89, 46), Lamp(89, 44), Lamp(89, 42), Lamp(88, 43), Lamp(88, 45), Lamp(88, 46), Lamp(88, 47),
    Lamp(88, 49), Lamp(87, 42), Lamp(87, 46), Lamp(87, 47), Lamp(87, 48), Lamp(87, 50), Lamp(86, 49), Lamp(86, 47),
    Lamp(86, 46), Lamp(86, 45), Lamp(86, 43), Lamp(85, 42), Lamp(85, 44), Lamp(85, 46), Lamp(85, 47), Lamp(85, 48),
    Lamp(85, 50), Lamp(84, 51), Lamp(84, 49), Lamp(84, 47), Lamp(84, 46), Lamp(84, 45), Lamp(84, 43), Lamp(83, 42),
    Lamp(83, 44), Lamp(83, 46), Lamp(83, 47), Lamp(83, 48), Lamp(83, 50), Lamp(82, 51), Lamp(82, 49), Lamp(82, 47),
    Lamp(82, 46), Lamp(82, 45), Lamp(82, 43), Lamp(81, 44), Lamp(81, 46), Lamp(81, 47), Lamp(81, 48), Lamp(81, 50),
    Lamp(80, 51), Lamp(79, 50), Lamp(80, 49), Lamp(80, 46), Lamp(80, 47), Lamp(64, 0), Lamp(63, 0), Lamp(67, 1),
    Lamp(66, 1), Lamp(65, 1), Lamp(64, 1), Lamp(64, 2), Lamp(65, 2), Lamp(66, 2), Lamp(67, 2), Lamp(66, 3), Lamp(65, 3),
    Lamp(64, 3), Lamp(64, 4), Lamp(65, 4), Lamp(66, 4), Lamp(66, 5), Lamp(65, 5), Lamp(64, 5), Lamp(64, 6), Lamp(65, 6),
    Lamp(66, 6), Lamp(66, 7), Lamp(65, 7), Lamp(64, 7), Lamp(64, 8), Lamp(65, 8), Lamp(66, 8), Lamp(66, 9), Lamp(65, 9),
    Lamp(64, 9), Lamp(64, 10), Lamp(65, 10), Lamp(66, 10), Lamp(66, 11), Lamp(65, 11), Lamp(64, 11), Lamp(64, 12),
    Lamp(65, 12), Lamp(66, 12), Lamp(66, 13), Lamp(65, 13), Lamp(64, 13), Lamp(64, 14), Lamp(65, 14), Lamp(66, 14),
    Lamp(66, 15), Lamp(65, 15), Lamp(64, 15), Lamp(66, 17), Lamp(65, 17), Lamp(62, 18), Lamp(63, 17), Lamp(65, 16),
    Lamp(66, 16), Lamp(67, 19), Lamp(66, 19), Lamp(65, 19), Lamp(64, 19), Lamp(63, 20), Lamp(65, 20), Lamp(66, 20),
    Lamp(67, 20), Lamp(68, 21), Lamp(67, 21), Lamp(66, 21), Lamp(64, 21), Lamp(65, 22), Lamp(66, 22), Lamp(67, 23),
    Lamp(66, 23), Lamp(65, 23), Lamp(66, 24), Lamp(67, 24), Lamp(68, 25), Lamp(67, 25), Lamp(66, 25), Lamp(66, 26),
    Lamp(67, 26), Lamp(67, 27), Lamp(66, 27), Lamp(65, 27), Lamp(66, 28), Lamp(68, 29), Lamp(67, 29), Lamp(66, 29),
    Lamp(65, 29), Lamp(66, 30), Lamp(67, 30), Lamp(67, 31), Lamp(66, 31), Lamp(65, 31), Lamp(66, 32), Lamp(67, 32),
    Lamp(68, 32), Lamp(68, 33), Lamp(67, 33), Lamp(66, 33), Lamp(66, 34), Lamp(67, 34), Lamp(13, 46), Lamp(13, 45),
    Lamp(13, 44), Lamp(12, 43), Lamp(12, 44), Lamp(12, 45), Lamp(12, 46), Lamp(12, 47), Lamp(11, 48), Lamp(11, 47),
    Lamp(11, 46), Lamp(11, 45), Lamp(11, 44), Lamp(11, 43), Lamp(11, 42), Lamp(10, 42), Lamp(10, 43), Lamp(10, 44),
    Lamp(10, 45), Lamp(10, 46), Lamp(10, 47), Lamp(10, 48), Lamp(9, 48), Lamp(9, 47), Lamp(8, 48), Lamp(8, 47),
    Lamp(8, 46), Lamp(9, 46), Lamp(9, 45), Lamp(9, 44), Lamp(9, 43), Lamp(9, 42), Lamp(8, 42), Lamp(8, 43), Lamp(8, 44),
    Lamp(8, 45), Lamp(7, 45), Lamp(7, 44), Lamp(7, 43), Lamp(7, 42), Lamp(6, 42), Lamp(6, 43), Lamp(6, 44), Lamp(6, 45),
    Lamp(6, 46), Lamp(7, 46), Lamp(7, 47), Lamp(7, 48), Lamp(5, 48), Lamp(6, 48), Lamp(6, 47), Lamp(5, 47), Lamp(5, 46),
    Lamp(5, 45), Lamp(5, 44), Lamp(5, 43), Lamp(5, 42), Lamp(4, 42), Lamp(4, 43), Lamp(4, 44), Lamp(4, 45), Lamp(4, 46),
    Lamp(4, 47), Lamp(4, 48), Lamp(3, 48), Lamp(3, 47), Lamp(3, 46), Lamp(3, 45), Lamp(3, 44), Lamp(3, 43), Lamp(3, 42),
    Lamp(2, 43), Lamp(2, 47), Lamp(2, 46), Lamp(2, 45), Lamp(2, 44), Lamp(1, 44), Lamp(1, 45), Lamp(1, 46), Lamp(62, 62),
    Lamp(63, 62), Lamp(64, 62), Lamp(65, 62), Lamp(66, 62), Lamp(67, 62), Lamp(68, 62), Lamp(69, 62), Lamp(70, 62),
    Lamp(71, 62), Lamp(72, 62), Lamp(63, 63), Lamp(64, 63), Lamp(65, 63), Lamp(66, 63), Lamp(67, 63), Lamp(68, 63),
    Lamp(69, 63), Lamp(70, 63), Lamp(71, 63), Lamp(72, 63), Lamp(65, 64), Lamp(65, 64), Lamp(66, 64), Lamp(67, 64),
    Lamp(68, 64), Lamp(69, 64), Lamp(70, 64), Lamp(71, 64), Lamp(65, 65), Lamp(66, 65), Lamp(67, 65), Lamp(68, 65),
    Lamp(69, 65), Lamp(66, 66), Lamp(67, 66), Lamp(68, 66), Lamp(66, 67), Lamp(67, 67), Lamp(67, 68), Lamp(61, 61),
    Lamp(62, 61), Lamp(63, 61), Lamp(64, 61), Lamp(65, 61), Lamp(66, 61), Lamp(67, 61), Lamp(68, 61), Lamp(69, 61),
    Lamp(70, 61), Lamp(71, 61), Lamp(72, 61), Lamp(61, 60), Lamp(62, 60), Lamp(63, 60), Lamp(64, 60), Lamp(65, 60),
    Lamp(66, 60), Lamp(67, 60), Lamp(68, 60), Lamp(69, 60), Lamp(70, 60), Lamp(71, 60), Lamp(72, 60), Lamp(65, 54),
    Lamp(59, 59), Lamp(60, 59), Lamp(61, 59), Lamp(62, 59), Lamp(63, 59), Lamp(64, 59), Lamp(65, 59), Lamp(66, 59),
    Lamp(67, 59), Lamp(68, 59), Lamp(69, 59), Lamp(70, 59), Lamp(71, 59), Lamp(72, 59), Lamp(73, 59), Lamp(74, 59),
    Lamp(75, 59), Lamp(59, 58), Lamp(60, 58), Lamp(61, 58), Lamp(62, 58), Lamp(63, 58), Lamp(64, 58), Lamp(65, 58),
    Lamp(66, 58), Lamp(67, 58), Lamp(68, 58), Lamp(69, 58), Lamp(70, 58), Lamp(71, 58), Lamp(72, 58), Lamp(73, 58),
    Lamp(74, 58), Lamp(75, 58), Lamp(76, 58), Lamp(77, 58), Lamp(58, 57), Lamp(59, 57), Lamp(60, 57), Lamp(61, 57),
    Lamp(62, 57), Lamp(63, 57), Lamp(64, 57), Lamp(65, 57), Lamp(66, 57), Lamp(67, 57), Lamp(68, 57), Lamp(69, 57),
    Lamp(70, 57), Lamp(71, 57), Lamp(72, 57), Lamp(73, 57), Lamp(74, 57), Lamp(75, 57), Lamp(76, 57), Lamp(77, 57),
    Lamp(57, 56), Lamp(58, 56), Lamp(59, 56), Lamp(60, 56), Lamp(61, 56), Lamp(62, 56), Lamp(63, 56), Lamp(64, 56),
    Lamp(65, 56), Lamp(66, 56), Lamp(67, 56), Lamp(68, 56), Lamp(69, 56), Lamp(70, 56), Lamp(71, 56), Lamp(72, 56),
    Lamp(73, 56), Lamp(74, 56), Lamp(75, 56), Lamp(76, 56), Lamp(77, 56), Lamp(78, 56), Lamp(56, 55), Lamp(57, 55),
    Lamp(58, 55), Lamp(59, 55), Lamp(60, 55), Lamp(61, 55), Lamp(62, 55), Lamp(63, 55), Lamp(64, 55), Lamp(65, 55),
    Lamp(66, 55), Lamp(67, 55), Lamp(68, 55), Lamp(69, 55), Lamp(70, 55), Lamp(71, 55), Lamp(72, 55), Lamp(73, 55),
    Lamp(74, 55), Lamp(75, 55), Lamp(76, 55), Lamp(77, 55), Lamp(78, 55), Lamp(55, 54), Lamp(56, 54), Lamp(57, 54),
    Lamp(58, 54), Lamp(59, 54), Lamp(60, 54), Lamp(61, 54), Lamp(62, 54), Lamp(63, 54), Lamp(64, 54), Lamp(65, 54),
    Lamp(66, 54), Lamp(67, 54), Lamp(68, 54), Lamp(69, 54), Lamp(70, 54), Lamp(71, 54), Lamp(72, 54), Lamp(73, 54),
    Lamp(74, 54), Lamp(75, 54), Lamp(76, 54), Lamp(77, 54), Lamp(56, 53), Lamp(57, 53), Lamp(58, 53), Lamp(59, 53),
    Lamp(60, 53), Lamp(61, 53), Lamp(62, 53), Lamp(63, 53), Lamp(64, 53), Lamp(65, 53), Lamp(66, 53), Lamp(67, 53),
    Lamp(68, 53), Lamp(69, 53), Lamp(70, 53), Lamp(71, 53), Lamp(72, 53), Lamp(73, 53), Lamp(74, 53), Lamp(75, 53),
    Lamp(76, 53), Lamp(77, 53), Lamp(78, 53), Lamp(55, 52), Lamp(56, 52), Lamp(57, 52), Lamp(58, 52), Lamp(59, 52),
    Lamp(60, 52), Lamp(61, 52), Lamp(62, 52), Lamp(63, 52), Lamp(64, 52), Lamp(65, 52), Lamp(66, 52), Lamp(67, 52),
    Lamp(68, 52), Lamp(69, 52), Lamp(70, 52), Lamp(71, 52), Lamp(72, 52), Lamp(73, 52), Lamp(74, 52), Lamp(75, 52),
    Lamp(76, 52), Lamp(77, 52), Lamp(78, 52), Lamp(54, 51), Lamp(55, 51), Lamp(56, 51), Lamp(57, 51), Lamp(58, 51),
    Lamp(59, 51), Lamp(60, 51), Lamp(61, 51), Lamp(62, 51), Lamp(63, 51), Lamp(64, 51), Lamp(65, 51), Lamp(66, 51),
    Lamp(67, 51), Lamp(68, 51), Lamp(69, 51), Lamp(70, 51), Lamp(71, 51), Lamp(72, 51), Lamp(73, 51), Lamp(74, 51),
    Lamp(75, 51), Lamp(76, 51), Lamp(77, 51), Lamp(53, 50), Lamp(54, 50), Lamp(55, 50), Lamp(56, 50), Lamp(57, 50),
    Lamp(58, 50), Lamp(59, 50), Lamp(60, 50), Lamp(61, 50), Lamp(62, 50), Lamp(63, 50), Lamp(64, 50), Lamp(65, 50),
    Lamp(66, 50), Lamp(67, 50), Lamp(68, 50), Lamp(69, 50), Lamp(70, 50), Lamp(71, 50), Lamp(72, 50), Lamp(73, 50),
    Lamp(74, 50), Lamp(75, 50), Lamp(76, 50), Lamp(77, 50), Lamp(52, 49), Lamp(53, 49), Lamp(54, 49), Lamp(55, 49),
    Lamp(56, 49), Lamp(57, 49), Lamp(58, 49), Lamp(59, 49), Lamp(60, 49), Lamp(61, 49), Lamp(62, 49), Lamp(63, 49),
    Lamp(64, 49), Lamp(65, 49), Lamp(66, 49), Lamp(67, 49), Lamp(68, 49), Lamp(69, 49), Lamp(70, 49), Lamp(71, 49),
    Lamp(72, 49), Lamp(73, 49), Lamp(74, 49), Lamp(75, 49), Lamp(76, 49), Lamp(77, 49), Lamp(76, 48), Lamp(75, 48),
    Lamp(74, 48), Lamp(73, 48), Lamp(72, 48), Lamp(71, 48), Lamp(70, 48), Lamp(69, 48), Lamp(68, 48), Lamp(67, 48),
    Lamp(66, 48), Lamp(65, 48), Lamp(64, 48), Lamp(63, 48), Lamp(62, 48), Lamp(61, 48), Lamp(60, 48), Lamp(59, 48),
    Lamp(58, 48), Lamp(57, 48), Lamp(56, 48), Lamp(55, 48), Lamp(54, 48), Lamp(76, 47), Lamp(75, 47), Lamp(74, 47),
    Lamp(73, 47), Lamp(72, 47), Lamp(71, 47), Lamp(70, 47), Lamp(69, 47), Lamp(68, 47), Lamp(67, 47), Lamp(66, 47),
    Lamp(65, 47), Lamp(64, 47), Lamp(63, 47), Lamp(62, 47), Lamp(61, 47), Lamp(60, 47), Lamp(59, 47), Lamp(58, 47),
    Lamp(57, 47), Lamp(56, 47), Lamp(55, 47), Lamp(54, 47), Lamp(53, 47), Lamp(75, 46), Lamp(74, 46), Lamp(73, 46),
    Lamp(72, 46), Lamp(71, 46), Lamp(70, 46), Lamp(69, 46), Lamp(68, 46), Lamp(67, 46), Lamp(66, 46), Lamp(65, 46),
    Lamp(64, 46), Lamp(63, 46), Lamp(62, 46), Lamp(61, 46), Lamp(60, 46), Lamp(59, 46), Lamp(58, 46), Lamp(57, 46),
    Lamp(56, 46), Lamp(55, 46), Lamp(74, 45), Lamp(73, 45), Lamp(72, 45), Lamp(71, 45), Lamp(70, 45),
    Lamp(69, 45), Lamp(68, 45), Lamp(67, 45), Lamp(66, 45), Lamp(65, 45), Lamp(64, 45), Lamp(63, 45), Lamp(62, 45),
    Lamp(61, 45), Lamp(60, 45), Lamp(59, 45), Lamp(58, 45), Lamp(57, 45), Lamp(56, 45), Lamp(55, 45), Lamp(54, 45),
    Lamp(75, 44), Lamp(74, 44), Lamp(73, 44), Lamp(72, 44), Lamp(71, 44), Lamp(70, 44), Lamp(69, 44), Lamp(68, 44),
    Lamp(67, 44), Lamp(66, 44), Lamp(65, 44), Lamp(64, 44), Lamp(63, 44), Lamp(62, 44), Lamp(61, 44), Lamp(60, 44),
    Lamp(59, 44), Lamp(58, 44), Lamp(57, 44), Lamp(56, 44), Lamp(55, 44), Lamp(73, 43), Lamp(72, 43), Lamp(71, 43),
    Lamp(70, 43), Lamp(69, 43), Lamp(68, 43), Lamp(67, 43), Lamp(66, 43), Lamp(65, 43), Lamp(64, 43), Lamp(63, 43),
    Lamp(62, 43), Lamp(61, 43), Lamp(60, 43), Lamp(59, 43), Lamp(58, 43), Lamp(57, 43), Lamp(72, 42), Lamp(71, 42),
    Lamp(70, 42), Lamp(69, 42), Lamp(68, 42), Lamp(67, 42), Lamp(66, 42), Lamp(65, 42), Lamp(64, 42), Lamp(63, 42),
    Lamp(62, 42), Lamp(61, 42), Lamp(60, 42), Lamp(59, 42), Lamp(70, 41), Lamp(69, 41), Lamp(68, 41), Lamp(67, 41),
    Lamp(66, 41), Lamp(65, 41), Lamp(64, 41), Lamp(63, 41), Lamp(62, 41), Lamp(61, 41), Lamp(60, 41), Lamp(59, 41),
    Lamp(58, 41), Lamp(58, 40), Lamp(59, 40), Lamp(60, 40), Lamp(61, 40), Lamp(62, 40), Lamp(63, 40), Lamp(59, 39),
    Lamp(58, 39), Lamp(57, 39), Lamp(71, 40), Lamp(70, 40), Lamp(69, 40), Lamp(68, 40), Lamp(67, 40), Lamp(67, 39),
    Lamp(68, 39), Lamp(69, 39), Lamp(70, 39), Lamp(69, 38), Lamp(68, 38), Lamp(67, 38), Lamp(68, 37), Lamp(67, 37),
    Lamp(66, 37), Lamp(80, 43), Lamp(50, 43), Lamp(51, 43), Lamp(52, 43), Lamp(53, 43), Lamp(50, 44), Lamp(51, 44),
    Lamp(52, 44), Lamp(53, 44), Lamp(42, 49), Lamp(41, 39), Lamp(41, 40), Lamp(41, 41), Lamp(41, 42), Lamp(79, 55)
)

class Ceiling:
    def __init__(self, filename=None):
        if filename is not None:
            self.readlamps(filename)
        else:
            self.lamps = hardcoded_lamps()
        self.bubbleroof_lamps = list(filter(lambda lamp: bubbleroof.collidepoint(lamp.x, lamp.y), self.lamps))

    def readlamps(self, filename):
        # Generate array of lights fixture locations
        f = open(filename)
        csv_f = csv.DictReader(f)
        for row in csv_f:
            # Adjusted XY coordinates -1 as Madrix counts from 1
            self.lamps.append(Lamp(int(row['X']) - 1, int(row['Y']) - 1))

ceiling = Ceiling()
