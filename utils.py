__author__ = 'ajtag'

import colorsys

def hls_to_rgb(hue, lightness, saturation):
    """
    :param hue: 0-360
    :param lightness:  0-100
    :param saturation:  0-100
    :return: list(int)
    """
    return [int(i * 255) for i in colorsys.hls_to_rgb(hue / 360.0, lightness / 100.0, saturation / 100.0)]


def hlsa_to_rgba(hue, lightness, saturation, alpha):
    """
    :param hue: 0-360
    :param lightness:  0-100
    :param saturation:  0-100
    :return: list(int)
    """
    rgb = colorsys.hls_to_rgb(hue / 360.0, lightness / 100.0, saturation / 100.0)

    rgba = [0,0,0,alpha]
    for n, i in enumerate(rgb):
        rgba[n] = int(i * 255)
    return rgba



# dist_Point_to_Segment(): get the distance of a point to a segment
#     Input:  a Point P and a Segment S (in any dimension)
#     Return: the shortest distance from P to S

def dist_Point_to_Segment( point, line):
     v = line[0] - line[1] #
     w = point - line[0] #  P - S.P0;

     c1 = w.dot(v) #dot(w,v);
     if c1 <= 0:
          point.distance_to(line[0])

     c2 = v.dot(v)
     if c2 <= c1:
          point.distance_to(line[1])

     b = c1 / c2
     Pb = line[0] + b * v

     return point.distance_to(Pb)

