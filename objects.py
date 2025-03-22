#!/usr/bin/python3

"""
    File contains instructions for apple, snegment and tail classes.
    Snegment:
    - Canvas appearance
    - Location
    tail:
    - Death timer
"""

class Obj():
    """Contains: 
    Instructions to create snegment
    Location
    """
    def __init__(
            self,
            xstart:int,
            ystart:int
                ):
        
        self.x0 = xstart
        self.y0 = ystart

        #Set x and y coords
        self.x1 = self.x0 + 25
        self.y1 = self.y0 + 25
