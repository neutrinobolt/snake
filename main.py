#!/usr/bin/python3
"""Main runner file."""


import board

def main ():
    """Main running function.
    - Get current score
    - Create and run board
    """
    #Get previous high score
    with open('hscore.txt', "r", encoding= "UTF-8") as infile:
        hi_score = infile.read()

    #Create board and run board
    play_board = board.Board(hi_score)
    play_board.window.mainloop()
    #print("Past mainloop") # debug

if __name__ == "__main__":
    main()
