"""
PROJECT: Bubble Blaster
GOAL: Create a game to practice GUI logic and event handling.
AUTHOR: Noelia Lázaro
DATE: 2026
"""

import tkinter as tk

# 1. SETUP CONSTANTS
HEIGHT = 500
WIDTH = 800

# 2. INITIALIZE WINDOW (We give the game the name "Bubble Blaster")
window = tk.Tk()
window.title("Bubble Blaster - Python Learning Project")

# 3. CREATE THE CANVAS (The 'ocean' where the game happens)
c = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="darkblue")
c.pack()

# Draw a triangle for the submarine body
# ID for tracking the polygon shape
sub_id = c.create_polygon(5, 5, 5, 25, 30, 15, fill="red")

# Draw the outline of a circle (the submarine's hull)
sub_id2 = c.create_oval(0, 0, 30, 30, outline="white")

# Submarine radius for collision detection logic
SUB_R = 15

# Calculate the center coordinates of the screen
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2

# Move both parts of the submarine to the center
c.move(sub_id, MID_X, MID_Y)
c.move(sub_id2, MID_X, MID_Y)

# SUB_SPEED is the distance the sub moves per key press
SUB_SPEED = 10

def move_submarine(event):
    """ Event handler to move the submarine with arrow keys """
    if event.keysym == 'Up':
        c.move(sub_id, 0, -SUB_SPEED)
        c.move(sub_id2, 0, -SUB_SPEED)
    elif event.keysym == 'Down':
        c.move(sub_id, 0, SUB_SPEED)
        c.move(sub_id2, 0, SUB_SPEED)
    elif event.keysym == 'Left':
        c.move(sub_id, -SUB_SPEED, 0)
        c.move(sub_id2, -SUB_SPEED, 0)
    elif event.keysym == 'Right':
        # ERROR FIX: In your book it says -SUB_SPEED for right, 
        # but to go right you need a POSITIVE number (+)
        c.move(sub_id, SUB_SPEED, 0)
        c.move(sub_id2, SUB_SPEED, 0)
    c.bind_all('<Key>', move_submarine)


from random import randint

# These lists act as our database for active bubbles
bub_id = list()
bub_r = list()
bub_speed = list()

# Constants for bubble generation
MIN_BUB_R = 10
MAX_BUB_R = 30
MAX_BUB_SPEED = 10
GAP = 100

def create_bubble():
    """ Generates a new bubble with random size and speed """
    # Set the starting position (off-screen to the right)
    x = WIDTH + GAP
    y = randint(0, HEIGHT)
    
    # Choose a random radius
    r = randint(MIN_BUB_R, MAX_BUB_R)
    
    # Draw the bubble 

    id1 = c.create_oval(x - r, y - r, x + r, y + r, outline="white")
    
    # Save the bubble data into our lists
    bub_id.append(id1)
    bub_r.append(r)
    bub_speed.append(randint(1, MAX_BUB_SPEED))

from time import sleep, time

# This function goes through the list of bubbles and moves each one
def move_bubbles():
    """ Iterates through all bubbles and moves them according to their speed """
    for i in range(len(bub_id)):
        # Move the bubble on the canvas
        c.move(bub_id[i], -bub_speed[i], 0)

def get_coords(id_num):
    """ Returns the center coordinates of a specific bubble """
    pos = c.coords(id_num)
    # The list 'pos' contains [x1, y1, x2, y2]
    # We calculate the midpoint to find the center
    x = (pos[0] + pos[2]) / 2
    y = (pos[1] + pos[3]) / 2
    return x, y

# MAIN GAME LOOP
BUB_CHANCE = 10

while True:
    # 1. Randomly decide if a new bubble should be created
    if randint(1, BUB_CHANCE) == 1:
        create_bubble()
    
    # 2. Update positions of all existing bubbles
    move_bubbles()
    
    # 3. Refresh the window to show the movement
    window.update()
    
    # 4. Control the game speed (frame rate)
    sleep(0.01)
    