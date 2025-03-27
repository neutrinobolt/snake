# snake

My attempt on creating the classic game in Python. Just for fun, to say I did.
Last updated: 3/27/25

## Dependencies

- Python's builtin module tkinter for creating the UI
- Pynput for tracking keyboard input

## Todo

- Add ability to control snake with arrow keys
- Add other keybinds: Enter(start/play game), Space(pause game)
- Fix bug: As is, snake can be made to move in opposite direction of current
direction. This leads to immediately losing. Fix: make it so snake can't go
backwards.
- Fix bug: snake immediately begins moving in last selected direction on
game reset. Fix: Either set so snake stays put or always starts moving right
(towards first apple).
- Simplify installation process

### Additional functions

- Add sound effects
- Add settings to customize keybinds
- Add function to reset high score

## Files

### main.py

- Runs whole program
- relies on board.py and hscore.txt
- Gets high score from hscore.txt
- create board class using high score

### board.py

- Creates tkinter window, canvas and play/quit buttons
- relies on objects.py, snegments.py, time, random, tkinter, pynput

#### Class Components

- Window. Contains canvas, play button, quit button

#### Class Actions

- On initialization, create game boundaries, score view, apple, head of
snake, and list containing all tail segments (starts empty). Head and apple are
both object.Obj objects, tail segments use additional snegment data.
- On clicking play button, the play loop starts. Player can control snake with
WASD keys. Snake will continue in one direction until a new key is pressed, or
head collides with wall or tail. When head hits apple, score increases by one
and apple moves to a random open location. On every step, a new tail segment is
created with time_to_live (ttl) equal to current score, decrement ttl of all
tail segments by one, and any tail segments with ttl less than 0 are destroyed,
thus creating the illusion that the tail is "following" the head.
- When the play loop has concluded (the head collides with wall or tail),
the board state is returned to initial state. If the final score is greater
than the current recorded high score, hscore.txt is updated with the new high
score. All tails are destroyed, the head and apple are returned to their
starting positions, and the running score is set to zero.
- On clicking quit button, the window is closed and the program ends.

### objects.py

#### Obj Class components

- Given a single coordinate pair, class Obj creates a canvas rectangle with
given coords at top left. Object color can also be input as a string.

### snegments.py

- Snegment class inherits Obj class components.

### Unique Snegment Class components

- time_to_live: integer. Used to keep track of how long until snegment is
destroyed.

### hscore.txt

- Just contains a single number. Used to track highest score achieved.
