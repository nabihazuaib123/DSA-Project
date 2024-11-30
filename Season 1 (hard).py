import tkinter as tk
from tkinter import messagebox
import random

# Initialize global variables
root = tk.Tk()
root.title("Shifty Chronicles")
root.geometry("700x700")
root.configure(bg='#DFF2FF')

frame = tk.Frame(root, bg='#003A20', padx=20, pady=20)
frame.pack(expand=True)

cards = []
buttons = []
first_card = None
second_card = None
matched_pairs = 0
locked = False
cover_image = None
front_images = []
time_limit = 40
remaining_time = time_limit
timer_update = None

timer_label = tk.Label(root, text=f"Time: {remaining_time}", font=("Arial", 16), bg='#DFF2FF', fg='#003A20')
timer_label.pack(pady=10)

def load_images():
    global cover_image, front_images
    cover_image = tk.PhotoImage(file="shifty chronicles cover 1.png")

    image_files = [
        "S1cards_back/s1card_0.png", "S1cards_back/s1card_1.png", "S1cards_back/s1card_2.png",
        "S1cards_back/s1card_3.png", "S1cards_back/s1card_4.png", "S1cards_back/s1card_5.png",
        "S1cards_back/s1card_6.png", "S1cards_back/s1card_7.png"
    ]

    for file_name in image_files:
        image = tk.PhotoImage(file=file_name)
        front_images.append(image)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def shuffle_cards():
    global cards
    card_values = list(range(8)) * 2
    random.shuffle(card_values)
    # Use sorting to 'shuffle' further - can switch to bubble_sort or quick_sort
    cards = bubble_sort(card_values) if random.choice([True, False]) else quick_sort(card_values)
    random.shuffle(cards)  # Final random shuffle for better mix

def create_widgets():
    for i in range(4):
        row = []
        for j in range(4):
            button = tk.Button(frame, image=cover_image, width=100, height=100,
                               command=lambda i=i, j=j: card_clicked(i, j))
            button.grid(row=i, column=j)
            row.append(button)
        buttons.append(row)

    for i in range(4):
        frame.grid_columnconfigure(i, weight=1)
    for j in range(4):
        frame.grid_rowconfigure(j, weight=1)

def start_timer():
    update_timer()

def update_timer():
    global remaining_time, timer_update
    if remaining_time > 0:
        timer_label.config(text=f"Time: {remaining_time}")
        remaining_time -= 1
        timer_update = root.after(1000, update_timer)
    else:
        stop_game()

def stop_game():
    global locked
    locked = True
    timer_label.config(text="Time's up!")
    if messagebox.askyesno("Game Over", "Time's up! Would you like to play again?"):
        reset_game()

def card_clicked(i, j):
    global first_card, second_card, locked

    if locked:
        return

    if remaining_time == time_limit:
        start_timer()

    button = buttons[i][j]
    card_index = cards[i * 4 + j]

    if button['image'] == str(cover_image):
        button.config(image=front_images[card_index])

        if first_card is None:
            first_card = (i, j)
        else:
            second_card = (i, j)
            locked = True
            root.after(1000, check_for_match)

def check_for_match():
    global first_card, second_card, matched_pairs, locked
    first_i, first_j = first_card
    second_i, second_j = second_card

    if cards[first_i * 4 + first_j] == cards[second_i * 4 + second_j]:
        matched_pairs += 1
        buttons[first_i][first_j].config(state="disabled")
        buttons[second_i][second_j].config(state="disabled")

        if matched_pairs == 8:
            show_winner()
    else:
        root.after(500, hide_cards, first_i, first_j, second_i, second_j)

    first_card = None
    second_card = None
    locked = False

def hide_cards(first_i, first_j, second_i, second_j):
    buttons[first_i][first_j].config(image=cover_image)
    buttons[second_i][second_j].config(image=cover_image)

def show_winner():
    global locked
    locked = True
    timer_label.config(text="You win!")

    if timer_update is not None:
        root.after_cancel(timer_update)

    if messagebox.askyesno("Play Again?", "You won! Would you like to play again?"):
        reset_game()

def reset_game():
    global cards, first_card, second_card, matched_pairs, locked, remaining_time, timer_update, game_started
    shuffle_cards()
    matched_pairs = 0
    locked = False
    first_card = None
    second_card = None
    remaining_time = time_limit
    game_started = False  # Reset game start status to delay timer

    timer_label.config(text=f"Time: {remaining_time}")

    for row in buttons:
        for button in row:
            button.config(image=cover_image, state="normal")

    if timer_update is not None:
        root.after_cancel(timer_update)


# Initialize game
load_images()
shuffle_cards()
create_widgets()

root.mainloop()
