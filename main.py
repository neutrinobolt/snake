#!/usr/bin/python3
"""Main runner file."""

import board

def main ():
    """Main running function."""
    #Get previous high score
    with open("hscore.txt", "r", encoding= "UTF-8") as infile:
        hi_score = infile.read()
    #Create board
    play_board = board.Board(hi_score)
    #Run board

if __name__ == "__main__":
    main()