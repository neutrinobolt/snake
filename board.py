#!/usr/bin/python3
"""
File containing board class definition.
- Dependencies:
    - pynput (exterior library)
    - objects.py
    - snegments.py
- Constants:
    - TIME_STEP:float
    - GRID_STEP:int
    - ACCEPTABLE_INPUTS:list of strings
- Board:
    - All black canvas with white lines outlining play map
    - Space under map on canvas for displaying current and high score
    - Space underneath canvas for play and quit buttons
    - Snake object
    - Step and move functions
    - Apple generation function
"""

import time
import random
import tkinter as tk
import objects as objs
import snegments as sn
from pynput import keyboard as kb

#Constants
TIME_STEP = .1
GRID_STEP = 25
ACCEPTABLE_INPUTS = ["w",
                     "a",
                     "s",
                     "d",
                     "Key.up",
                     "Key.down",
                     "Key.left",
                     "Key.right"
                     ]
class Board:
    """
    Contains and manages all objects within board canvas.
    - Args:
        - hscore_current:string
    - Variables:
        - hscore:int
        - curr_score:int
        - tails:list of snegments
        - window:tk window
        - canvas:tk canvas
        - field: rectangle
        - cscore_field: text field
        - hscore_field: text field
        - start_button: tk button
        - end-button: tk button
        - head: objects obj
        - apple: objects obj
        - move_current: function
        - dir_funcs: dictionary
        - key_press: string
        - is_alive: boolean
        - listener: pynput keyboard listener
    - Functions:
        - play
        - quit
        - reset_apple
        - step
        - move_up
        - move_down
        - move_left
        - move_right
        - stay_put
        - on_press
    """
    def __init__(self,
                 hscore_current):

        #Define preset values
        self.hscore = int(hscore_current)

        #Iteration specific stuff
        self.curr_score = 0
        self.tails:list[sn.Snegment] = []

        #Gui setup
        self.window = tk.Tk()
        self.window.title("Snake")
        self.canvas = tk.Canvas(self.window, width=800, height=600, bg="black")
        self.canvas.pack()
        #Setup appearance
        self.field = self.canvas.create_rectangle(25, 25, 775, 525, fill='black', outline='white')
        self.cscore_field = self.canvas.create_text(400, 540,
                                text = f'Current score: {self.curr_score}',
                                fill= 'white',
                                font=('Helvetica 10 bold')
                                )
        self.hscore_field = self.canvas.create_text(400, 560,
                                text = f'High score: {self.hscore}',
                                fill= 'white',
                                font=('Helvetica 10 bold')
                                )

        self.start_button = tk.Button(self.window,
                                 text = "Play",
                                 command = self.play)
        self.start_button.pack()

        self.end_button = tk.Button(self.window,
                                    text = "Quit",
                                    command = self.quit)
        self.end_button.pack()

        #Spawn snake head
        self.head = objs.Obj(self.canvas, 375, 200, fill_color="light green")

        # Spawn apple
        self.apple = objs.Obj(self.canvas, 600, 200, fill_color="red")

        # Set movement direction
        self.move_current = self.stay_put # Snake doesn't start moving until a key is pressed
        self.dir_funcs = {
            "w": self.move_up,
            "s": self.move_down,
            "a": self.move_left,
            "d": self.move_right,
            "Key.up": self.move_up,
            "Key.down": self.move_down,
            "Key.left": self.move_left,
            "Key.right": self.move_right
        }
        self.key_press = None

        # Set game status
        self.is_alive = False

        self.listener = kb.Listener(on_press=self.on_press)
        self.listener.start()

    def play(self):
        """
        Main gameplay loop.
        - run step() every time-step until a collision occurs
        - Reset game:
            - Show score on play button
            - Clear out self.tails
            - Put head and apple back in original locations
            - reset current score to zero
            - set is_alive back to true
        """

        #Run game
        print("Running Game") #debug
        self.is_alive = True
        while self.is_alive:
            print("In game loop") #debug
            time.sleep(TIME_STEP)
            self.step()

        #Game end
        print("Game over.") #debug
        self.move_current = self.stay_put

        #Prep for reset
        self.start_button.configure(text=f'Final score: {self.curr_score}. Play again?')
        while len(self.tails) > 0:
            for snegment in self.tails:
                snegment.time_to_live -= 1
                if snegment.time_to_live <= 0:
                    self.tails.pop(self.tails.index(snegment))
                    snegment.unalive()
        if len(self.tails) != 0:
            print("There are still snegments.")

        self.canvas.moveto(self.head.body, 374, 199)
        self.canvas.moveto(self.apple.body, 599, 199)
        #Update high score
        if self.curr_score > self.hscore:
            self.hscore = self.curr_score
            self.canvas.itemconfigure(self.hscore_field,
                                      text= f'High score: {self.hscore}')
            with open('snake/hscore.txt', "w", encoding= "UTF-8") as infile:
                infile.write(f'{self.hscore}')
        self.curr_score = 0
        self.canvas.itemconfigure(self.cscore_field,
                                  text = f'Current Score: {self.curr_score}')

    def quit(self):
        """Ends game, closes window"""
        self.listener.stop()
        self.window.destroy()

    def reset_apple(self):
        """
        - Add 1 to score
        - Move apple to random open location
        """
        # Add 1 to score
        self.curr_score += 1

        #Get new random coordinates, make sure they don't overlap with tail
        while True:
            new_x = random.randint(1, 30) * 25
            new_y = random.randint(1, 20) * 25
            collisions = 0
            for snegment in self.tails:
                sneg_coords = self.canvas.coords(snegment.body)
                if new_x == sneg_coords[0] and new_y == sneg_coords[1]:
                    collisions += 1
            if collisions == 0:
                break

        self.canvas.itemconfigure(self.cscore_field,
                                  text=f'Current score: {self.curr_score}')

        # Set apple coords to new coords
        self.canvas.moveto(self.apple.body, new_x - 1, new_y - 1)

    def step(self):
        """
        Runs every time step interval. 
        - Update move_current
        - Move head
        - Update tail:
            - Decrement ttl on snegments
            - Kill dead snegments
        - check for collisions
        - check for apple
        """

        print(self.key_press) #debug
        if  self.key_press in ACCEPTABLE_INPUTS:
            self.move_current = self.dir_funcs[self.key_press]

        self.move_current()

        #Decrement ttl on all snegments, remove ones with tt -1 or less
        for snegment in self.tails:
            snegment.time_to_live -= 1
            if snegment.time_to_live < 0:
                self.tails.pop(self.tails.index(snegment))
                snegment.unalive()

        #Death conditions
        head_coords = self.canvas.coords(self.head.body)
        #Leave field boundaries
        if head_coords[0] < 25 or head_coords[0] >= 775 or head_coords[1] < 25 or head_coords[1] >= 525:
            self.is_alive = False
        #Hit tail
        for snegment in self.tails:
            sneg_coords = self.canvas.coords(snegment.body)
            if head_coords[0] == sneg_coords[0] and head_coords[1] == sneg_coords[1]:
                self.is_alive = False

        # Check for apple
        apple_coords = self.canvas.coords(self.apple.body)
        if head_coords[0] == apple_coords[0] and head_coords[1] == apple_coords[1]:
            self.reset_apple()

    ### Movement functions
    def move_up(self):
        """create new snegment, move up one space"""
        #Get head current position
        head_coords = self.canvas.coords(self.head.body)

        #Create new snegment at head location
        new_snegment = sn.Snegment(self.canvas, head_coords[0], head_coords[1], self.curr_score)
        self.tails.append(new_snegment)

        #Move head
        self.canvas.move(self.head.body, 0, 0 - GRID_STEP)
        self.canvas.update()

    def move_down(self):
        """create new snegment, move down one space"""
        #Get head current position
        head_coords = self.canvas.coords(self.head.body)

        #Create new snegment at head location
        new_snegment = sn.Snegment(self.canvas, head_coords[0], head_coords[1], self.curr_score)
        self.tails.append(new_snegment)

        self.canvas.move(self.head.body, 0, GRID_STEP)
        self.canvas.update()

    def move_left(self):
        """create new snegment, move left one space"""
        #Get head current position
        head_coords = self.canvas.coords(self.head.body)

        #Create new snegment at head location
        new_snegment = sn.Snegment(self.canvas, head_coords[0], head_coords[1], self.curr_score)
        self.tails.append(new_snegment)

        self.canvas.move(self.head.body, 0 - GRID_STEP, 0)
        self.canvas.update()

    def move_right(self):
        """create new snegment, move right one space"""
        #Get head current position
        head_coords = self.canvas.coords(self.head.body)

        #Create new snegment at head location
        new_snegment = sn.Snegment(self.canvas, head_coords[0], head_coords[1], self.curr_score)
        self.tails.append(new_snegment)

        self.canvas.move(self.head.body, GRID_STEP, 0)
        self.canvas.update()

    def stay_put(self):
        """Run on board opening. should be empty"""

    ### Keyboard listening funcs
    def on_press(self, key):
        """On key press, update self.key_press"""
        try:
            self.key_press = key.char
        except AttributeError:
            print(key)
            self.key_press = str(key)
            
