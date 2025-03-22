#!/usr/bin/python3
"""Class info for the Snegment class, child class of Obj"""

import objects

class Snegment(objects.Obj):
    def __init__(self, xstart, ystart, time_to_live):
        super().__init__(xstart, ystart)

        self.incolor = "light green"
        self.time_to_live = time_to_live
