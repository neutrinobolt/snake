#!/usr/bin/python3
"""
File containing board and apple class definitions.
Board has:
    - all black canvas with white lines outlining play map
    - Space underneath canvas for displaying current and high score
    - Snake object connected
    - Step function
    - Apple generation function
"""

import time
import tkinter as tk
import objects as objs
import snegments as sn
import keyboard

#Constants
TIME_STEP = .1
GRID_STEP = 30
ACCEPTABLE_INPUTS = ["w","a,", "s", "d"]
class Board:
    """Contains and manages all objects within board canvas."""
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
                                font=('Helvetica 10 bold')
                                )
        self.canvas.create_text(400, 560,
                                text = f'High score: {self.hscore}',
                                fill= 'white',
                                font=('Helvetica 10 bold')
                                )

        #Spawn snake head
        self.head_init = objs.Obj(370, 200)
        self.head = self.canvas.create_rectangle(self.head_init.x0, self.head_init.y0,
                                                 self.head_init.x1, self.head_init.y1,
                                                 fill= "light green")

        # Spawn apple
        self.apple_init = objs.Obj(600, 200)
        self.apple = self.canvas.create_rectangle(self.apple_init.x0, self.apple_init.y0,
                                                  self.apple_init.x1, self.apple_init.y1,
                                                  fill= "red")

        # Set movement direction
        self.move_current = self.stay_put # Snake doesn't start moving until a key is pressed
        self.dir_funcs = {
            "w": self.move_up,
            "s": self.move_down,
            "a": self.move_left,
            "d": self.move_right
        }

        # Set game status
        self.is_alive = True

        # Run the game
        while self.is_alive:
            time.sleep(TIME_STEP)
            self.step()

    def reset_apple(self):
        """removes apple from current location, adds 1 to length, spawn apple
        in new location"""
        pass

    def step(self):
        """Runs every time step interval. 
        Move head and tail segments, check for collisions, check for apple"""
        key_press = keyboard.read_key()
        if key_press in ACCEPTABLE_INPUTS:
            self.move_current = self.dir_funcs[key_press]
            self.move_current()

    def move_up(self):
        """create new snegment, move up one space"""
        new_snegment = sn.Snegment(self.head_init.x0, self.head_init.y0, self.curr_score)
        self.tails.append(new_snegment)

        current_coords = self.canvas.coords(self.head)
        self.canvas.move(self.head, current_coords[0] - GRID_STEP, current_coords[1])

    def move_down(self):
        """create new snegment, move down one space"""
        new_snegment = sn.Snegment(self.head_init.x0, self.head_init.y0, self.curr_score)
        self.tails.append(new_snegment)

        current_coords = self.canvas.coords(self.head)
        self.canvas.move(self.head, current_coords[0] + GRID_STEP, current_coords[1])

    def move_left(self):
        """create new snegment, move left one space"""
        new_snegment = sn.Snegment(self.head_init.x0, self.head_init.y0, self.curr_score)
        self.tails.append(new_snegment)

        current_coords = self.canvas.coords(self.head)
        self.canvas.move(self.head, current_coords[0], current_coords[1] - GRID_STEP)

    def move_right(self):
        """create new snegment, move right one space"""
        new_snegment = sn.Snegment(self.head_init.x0, self.head_init.y0, self.curr_score)
        self.tails.append(new_snegment)

        current_coords = self.canvas.coords(self.head)
        self.canvas.move(self.head, current_coords[0], current_coords[1] + GRID_STEP)

    def stay_put(self):
        """Run on board opening. should be empty"""
        new_snegment = sn.Snegment(self.head_init.x0, self.head_init.y0, self.curr_score)
        self.tails.append(new_snegment)

        current_coords = self.canvas.coords(self.head)
        self.canvas.move(self.head, current_coords[0] - GRID_STEP, current_coords[1])
