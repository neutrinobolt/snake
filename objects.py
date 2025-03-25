#!/usr/bin/python3

"""
    File contains instructions for apple, snegment and tail classes.
    Snegment:
    - Canvas appearance
    - Location
    tail:
    - Death timer
"""

import tkinter as tk

class Obj():
    """Contains: 
    Instructions to create snegment
    Location
    """
    def __init__(
            self,
            root: tk.Canvas,
            xstart:int,
            ystart:int,
            fill_color:str
                ):
        
        self.x0 = xstart
        self.y0 = ystart
        self.root = root

        #Set x and y coords
        self.x1 = self.x0 + 25
        self.y1 = self.y0 + 25

        self.body = self.root.create_rectangle(self.x0, self.y0,
                                               self.x1, self.y1,
                                               fill= fill_color)
        
    def delete(self):
        """Cleanly delete all object data"""
        self.root.delete(self.body)
        del self

