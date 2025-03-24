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
from pynput import keyboard as kb

#Constants
TIME_STEP = .1
GRID_STEP = 30
ACCEPTABLE_INPUTS = ["w", "a", "s", "d"]
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
        
        self.start_button = tk.Button(self.window, 
                                 text = "Play",
                                 command = self.play)
        self.start_button.pack()

        #Spawn snake head
        self.head = objs.Obj(self.canvas, 370, 200, fill_color="light green")

        # Spawn apple
        self.apple = objs.Obj(self.canvas, 600, 200, fill_color="red")

        # Set movement direction
        self.move_current = self.stay_put # Snake doesn't start moving until a key is pressed
        self.dir_funcs = {
            "w": self.move_up,
            "s": self.move_down,
            "a": self.move_left,
            "d": self.move_right
        }
        self.key_press = None

        # Set game status
        self.is_alive = True

        

    def play(self):
        print("Starting Game") #debug
        listener = kb.Listener(on_press=self.on_press, on_release=self.on_release)
        listener.start()
        while self.is_alive:
            #print("running game...")
            time.sleep(TIME_STEP)
            self.step()


    def reset_apple(self):
        """removes apple from current location, adds 1 to length, spawn apple
        in new location"""
        pass

    def step(self):
        """Runs every time step interval. 
        Move head and tail segments, check for collisions, check for apple"""
        print("Running step function") # Debug

        self.move_current()
        #print("moved") #debug

        print(self.key_press) # debug
        if  self.key_press in ACCEPTABLE_INPUTS:
            print("key_press acceptable") # debug
            #self.key_press = keyboard.read_key()
            self.move_current = self.dir_funcs[self.key_press]
            #print("move_current set") # debug

    ### Movement functions
    def move_up(self):
        """create new snegment, move up one space"""
        print("moving up") #debug
        new_snegment = sn.Snegment(self.canvas, self.head.x0, self.head.y0, self.curr_score)
        self.tails.append(new_snegment)

        self.canvas.move(self.head.body, 0, 0 - GRID_STEP)
        self.canvas.update()

    def move_down(self):
        """create new snegment, move down one space"""
        print("moving down") #debug
        new_snegment = sn.Snegment(self.canvas, self.head.x0, self.head.y0, self.curr_score)
        self.tails.append(new_snegment)

        self.canvas.move(self.head.body, 0, GRID_STEP)
        self.canvas.update()

    def move_left(self):
        """create new snegment, move left one space"""
        print("moving left") #debug
        new_snegment = sn.Snegment(self.canvas, self.head.x0, self.head.y0, self.curr_score)
        self.tails.append(new_snegment)

        self.canvas.move(self.head.body, 0 - GRID_STEP, 0)
        self.canvas.update()

    def move_right(self):
        """create new snegment, move right one space"""
        print("moving right") #debug
        new_snegment = sn.Snegment(self.canvas, self.head.x0, self.head.y0, self.curr_score)
        self.tails.append(new_snegment)

        self.canvas.move(self.head.body, GRID_STEP, 0)
        self.canvas.update()

    def stay_put(self):
        """Run on board opening. should be empty"""
        print("staying put")
        pass

    ### Keyboard listening funcs
    def on_press(self, key):
        self.key_press = key.char

    def on_release(self):
        pass