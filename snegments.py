#!/usr/bin/python3
"""
Class info for the Snegment class, child class of Obj
Dependencies:
    -objects.py 
"""

import objects

class Snegment(objects.Obj):
    """
    Child class of Obj

    Args:
        - All object args
        - time_to_live: int
    """
    def __init__(self, root, xstart, ystart, time_to_live:int):
        super().__init__(root, xstart, ystart, fill_color="light green")

        self.time_to_live = time_to_live
