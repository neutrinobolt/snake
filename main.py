#!/usr/bin/python3
"""Main runner file."""


import board
from pynput import keyboard as kb



def main ():
    """Main running function."""
    #Get previous high score
    with open('snake/hscore.txt', "r", encoding= "UTF-8") as infile:
        hi_score = infile.read()

    #Create board and run board
    play_board = board.Board(hi_score)
    play_board.window.mainloop()
    print("Past mainloop")

if __name__ == "__main__":
    main()