from __future__ import division
__author__ = 'Paddy'

import pygame.gfxdraw as pg
from math import atan2, cos, sin


class Shadow:

    def __init__(self, footprint):

        self.footprint = footprint
        self.point_list = [self.footprint.topleft, self.footprint.topright,
                           self.footprint.bottomleft, self.footprint.bottomright]

        # The list used to draw the polygon
        self.poly = []

        # Length shadow projects
        self.distance = 400

    def update(self, source):

        angles = []
        for point in self.point_list:
            # Find angle between source and point
            dx = source[0] - point[0]
            dy = source[1] - point[1]
            rad = atan2(dy, -dx)
            angles.append(rad)

        # Sort the angle and point lists by angle
        angles_sorted, points_sorted = zip(*sorted(zip(angles, self.point_list)))

        # Add the points with the highest and lowest angle to the poly list
        self.poly = [points_sorted[-1], points_sorted[0]]

        # Find two more points along respective angles
        new_points = [[point[0] + self.distance * cos(-angle),
                       point[1] + self.distance * sin(-angle)]
                      for point, angle in zip(points_sorted, angles_sorted)]

        for point in new_points:
            self.poly.append(point)

    def draw(self, surf):

        pg.aapolygon(surf, self.poly, (0, 0, 0))
        pg.filled_polygon(surf, self.poly, (0, 0, 0))


