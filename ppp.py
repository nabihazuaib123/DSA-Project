import tkinter as tk
import random
from tkinter import messagebox

# List of images (text for demonstration purposes)
images = ["apple", "banana", "cherry", "grape", "lemon", "orange", "pear", "strawberry"]
images = images * 2  # duplicate for pairs
random.shuffle(images)  # shuffle to randomize order

# Initialize global variables
first_selection = None
second_selection = None
buttons = []

def on_tile_click(row, col):
    """Handle tile click, flip and check for matches"""
    global first_selection, second_selection

    button = buttons[row][col]
    button.config(text=images[row * 4 + col], state=tk.DISABLED)

    if first_selection is None:
        first_selection = (row, col)
    elif second_selection is None:
        second_selection = (row, col)
        check_for_match()

def check_for_match():
    """Check if the two selected tiles match"""
    global first_selection, second_selection

    first_row, first_col = first_selection
    second_row, second_col = second_selection

    if images[first_row * 4 + first_col] == images[second_row * 4 + second_col]:
        messagebox.showinfo("Match", "You found a match!")
        reset_selections()
        check_game_over()
    else:
        # No match, reset after a delay
        root.after(1000, reset_tiles)

def reset_tiles():
    """Reset the tiles if no match is found"""
    global first_selection, second_selection

    first_row, first_col = first_selection
    second_row, second_col = second_selection

    buttons[first_row][first_col].config(text="", state=tk.NORMAL)
    buttons[second_row][second_col].config(text="", state=tk.NORMAL)

    reset_selections()

def reset_selections():
    """Reset the selections"""
    global first_selection, second_selection
    first_selection = None
    second_selection = None

def check_game_over():
    """Check if the game is over"""
    if all(button['state'] == tk.DISABLED for row in buttons for button in row):
        messagebox.showinfo("Game Over", "Congratulations! You've matched all the tiles.")

# Create the main window
root = tk.Tk()
root.title("Memory Tile Matching Game")

# Create the game board with buttons
for row in range(4):
    button_row = []
    for col in range(4):
        button = tk.Button(root, width=10, height=3, command=lambda r=row, c=col: on_tile_click(r, c))
        button.grid(row=row, column=col)
        button_row.append(button)
    buttons.append(button_row)

# Run the Tkinter event loop
root.mainloop()
