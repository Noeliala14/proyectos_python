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

