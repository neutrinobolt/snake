#!/usr/bin/python3
"""Main runner file."""

import board

def main ():
    """Main running function."""
    #Get previous high score
    with open('snake\hscore.txt', "r", encoding= "UTF-8") as infile:
        hi_score = infile.read()
    #Create board
    play_board = board.Board(hi_score)
    #Run board
    play_board.window.mainloop()

if __name__ == "__main__":
    main()