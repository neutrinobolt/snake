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

#Constants
TIME_STEP = .1
GRID_STEP = 30

class Board:
    def __init__(self, 
                 hscore_current):
        
        #Define preset values
        self.hscore = hscore_current

        
        

        #Iteration specific stuff
        self.curr_score = 0
        self.tails = []

        #Gui setup
        self.window = tk.Tk()
        self.window.title("Snake")
        self.canvas = tk.Canvas(self.window, width=800, height=600, bg="black")
        self.canvas.pack()
        #Setup appearance
        self.canvas.create_rectangle(25, 25, 775, 525, fill='black', outline='white')
        self.canvas.create_text(400, 540,
                                text = f'Current score: {self.curr_score}',
                                fill= 'white',
                                font=('Helvetica 10 bold'))
        self.canvas.create_text(400, 560,
                                text = f'High score: {self.hscore}',
                                fill= 'white',
                                font=('Helvetica 10 bold'))


    def apple(self):
        pass

    def step(self):
        pass
