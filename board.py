#!/usr/bin/python3
"""
File containing board class definition.
Board has:
    - all black canvas with white lines outlining play map
    - Space underneath canvas for displaying current and high score
    - Snake object connected
    - Step function
    - Apple generation function
"""

import tkinter as tk

class Board:
    def __init__(self, 
                 hscore_current):
        
        #Define preset values
        self.hscore = hscore_current

        #Define constants
        TIME_STEP = .1
        GRID_STEP = 10

        #

    def apple(self):
        pass

    def step(self):
        pass
