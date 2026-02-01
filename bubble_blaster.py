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

# Calculate the center coordinates of the sreen
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2

# Move both parts of the submarine to the center
c.move(sub_id, MID_X, MID_Y)
c.move(sub_id2, MID_X, MID_Y)

