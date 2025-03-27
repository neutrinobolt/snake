#!/usr/bin/python3

"""
File contains instructions for all objects on canvas.
"""

import tkinter as tk

class Obj():
    """
    Args:
        - root: canvas object
        - xstart: int
        - ystart: int
        - fill_color: string
    Variables: 
        - x0:int
        - y0:int
        - x1:int
        - y1:int
        - body: canvas rectangle
    Functions:
        - unalive
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

    def unalive(self):
        """Cleanly delete all object data"""
        self.root.delete(self.body)
        del self.x0
        del self.y0
        del self.x1
        del self.y1
        del self

