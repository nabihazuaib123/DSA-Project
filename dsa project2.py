import tkinter as tk
from tkinter import messagebox
import random



def season_1_easy():
    # Initialize root window
    root1 = tk.Tk()
    root1.title("Shifty Chronicles")
    root1.geometry("700x700")
    root1.configure(bg='#DFF2FF') 

    frame1 = tk.Frame(root1, bg='#003A20', padx=20, pady=20)
    frame1.pack(expand=True)

    # Declare persistent variables
    global cover_image1, front_images1, cards1, buttons1, first_card1, second_card1, matched_pairs1, locked1
    cards1 = []
    buttons1 = []
    first_card1 = None
    second_card1 = None
    matched_pairs1 = 0
    locked1 = False
    cover_image1 = None
    front_images1 = []

    def load_images1():
        global cover_image1, front_images1
        # Load the cover image
        cover_image1 = tk.PhotoImage(file="shifty chronicles cover 1.png")  # Ensure file path is correct
        root1.cover_image_ref1 = cover_image1  # Keep a reference to prevent garbage collection

        # Load each front image
        front_images1.clear()
        image_files1 = [
            "s1card_0.png", "s1card_1.png", "s1card_2.png",
            "s1card_3.png", "s1card_4.png", "s1card_5.png",
            "s1card_6.png", "s1card_7.png"
        ]

        for file_name1 in image_files1:
            image1 = tk.PhotoImage(file=file_name1)
            front_images1.append(image1)
            root1.front_images_refs1 = front_images1  # Keep a reference to front images
    def generate_cards1():
        # Generates a shuffled list of card values for a new game
        card_values1 = list(range(8)) * 2
        random.shuffle(card_values1)
        return card_values1

    def shuffle_cards1():
        global cards1
        cards1 = generate_cards1()

    def create_widgets1():
        global buttons1
        for i1 in range(4):
            row1 = []
            for j1 in range(4):
                # Create a button with the cover image initially
                button1 = tk.Button(frame1, image=cover_image1, width=100, height=100,
                                   command=lambda i1=i1, j1=j1: card_clicked1(i1, j1))
                button1.grid(row=i1, column=j1)
                row1.append(button1)
            buttons1.append(row1)

        # Adjust grid for alignment
        for i1 in range(4):
            frame1.grid_columnconfigure(i1, weight=1)
        for j1 in range(4):
            frame1.grid_rowconfigure(j1, weight=1)

    def card_clicked1(i1, j1):
        global first_card1, second_card1, locked1
        if locked1:
            return

        button1 = buttons1[i1][j1]
        card_index1 = cards1[i1 * 4 + j1]

        # If the button is still covered, reveal it
        if button1['image'] == str(cover_image1):
            button1.config(image=front_images1[card_index1])  # Show front image based on card index

            if first_card1 is None:
                first_card1 = (i1, j1)  # Save first selected card position
            else:
                second_card1 = (i1, j1)  # Save second selected card position
                locked1 = True
                root1.after(1000, check_for_match1)  # Check for a match after a delay

    def check_for_match1():
        global first_card1, second_card1, matched_pairs1, locked1
        first_i1, first_j1 = first_card1
        second_i1, second_j1 = second_card1

        if cards1[first_i1 * 4 + first_j1] == cards1[second_i1 * 4 + second_j1]:
            matched_pairs1 += 1
            buttons1[first_i1][first_j1].config(state="disabled")  # Disable matched buttons
            buttons1[second_i1][second_j1].config(state="disabled")

            if matched_pairs1 == 8:
                show_winner1()
        else:
            root1.after(500, hide_cards1, first_i1, first_j1, second_i1, second_j1)  # Cover cards again if not a match

        first_card1 = None
        second_card1 = None
        locked1 = False

    def hide_cards1(first_i1, first_j1, second_i1, second_j1):
        # Hide both unmatched cards by setting the cover image again
        buttons1[first_i1][first_j1].config(image=cover_image1)
        buttons1[second_i1][second_j1].config(image=cover_image1)

    def show_winner1():
        global locked1
        locked1 = True

        if messagebox.askyesno("Play Again?", "You won! Would you like to play again?"):
            reset_game1()
            
    def reset_game1():
        global cards1, first_card1, second_card1, matched_pairs1, locked1
        cards1 = generate_cards1()  # Shuffle cards again
        matched_pairs1 = 0
        locked1 = False
        first_card1 = None
        second_card1 = None

        for row1 in buttons1:
            for button1 in row1:
                button1.config(image=cover_image1, state="normal")  # Reset buttons with cover image

    # Initialize game
    load_images1()  # Load images before creating widgets
    shuffle_cards1()
    create_widgets1()

    root1.mainloop()


def season_1_medium():
    # Initialize global variables
    cover_image = None
    front_images = []
    cards = []
    buttons = []
    first_card = None
    second_card = None
    matched_pairs = 0
    locked = False
    time_limit = 60
    remaining_time = time_limit
    timer_update = None

    # Initialize root window
    root = tk.Tk()
    root.title("Shifty Chronicles")
    root.geometry("700x700")
    root.configure(bg='#DFF2FF')

    # Timer label
    timer_label = tk.Label(root, text=f"Time: {remaining_time}", font=("Arial", 16), bg='#DFF2FF', fg='#003A20')
    timer_label.pack(side="bottom", pady=10)

    frame = tk.Frame(root, bg='#003A20', padx=20, pady=20)
    frame.pack(expand=True)

    def load_images():
        nonlocal cover_image, front_images
        cover_image = tk.PhotoImage(file="shifty chronicles cover 1.png")
        image_files = [
            "s1card_0.png", "s1card_1.png", "s1card_2.png",
            "s1card_3.png", "s1card_4.png", "s1card_5.png",
            "s1card_6.png", "s1card_7.png"
        ]
        for file_name in image_files:
            image = tk.PhotoImage(file=file_name)
            front_images.append(image)

    def shuffle_cards():
        nonlocal cards
        card_values = list(range(8)) * 2
        random.shuffle(card_values)
        cards = random.sample(card_values, len(card_values))

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
        nonlocal remaining_time, timer_update
        if remaining_time > 0:
            timer_label.config(text=f"Time: {remaining_time}")
            remaining_time -= 1
            timer_update = root.after(1000, update_timer)
        else:
            stop_game()

    def stop_game():
        nonlocal locked
        locked = True
        timer_label.config(text="Time's up!")
        if messagebox.askyesno("Game Over", "Time's up! Would you like to play again?"):
            reset_game()

    def card_clicked(i, j):
        nonlocal first_card, second_card, locked
        if locked:
            return
        if remaining_time == time_limit:
            start_timer()

        button = buttons[i][j]
        card_index = cards[i * 4 + j]

        # Compare the image objects directly
        if button['image'] == str(cover_image):
            button.config(image=front_images[card_index])

            if first_card is None:
                first_card = (i, j)
            else:
                second_card = (i, j)
                locked = True
                root.after(1000, check_for_match)

    def check_for_match():
        nonlocal first_card, second_card, matched_pairs, locked
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
        nonlocal locked
        locked = True
        timer_label.config(text="You win!")

        if timer_update is not None:
            root.after_cancel(timer_update)

        if messagebox.askyesno("Play Again?", "You won! Would you like to play again?"):
            reset_game()

    def reset_game():
        nonlocal cards, first_card, second_card, matched_pairs, locked, remaining_time, timer_update
        shuffle_cards()
        matched_pairs = 0
        locked = False
        first_card = None
        second_card = None
        remaining_time = time_limit

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



def season_1_hard():
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
        nonlocal cover_image, front_images
        cover_image = tk.PhotoImage(file="shifty chronicles cover 1.png")

        image_files = [
            "s1card_0.png", "s1card_1.png", "s1card_2.png",
            "s1card_3.png", "s1card_4.png", "s1card_5.png",
            "s1card_6.png", "s1card_7.png"
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
        nonlocal cards
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
        nonlocal remaining_time, timer_update
        if remaining_time > 0:
            timer_label.config(text=f"Time: {remaining_time}")
            remaining_time -= 1
            timer_update = root.after(1000, update_timer)
        else:
            stop_game()

    def stop_game():
        nonlocal locked
        locked = True
        timer_label.config(text="Time's up!")
        if messagebox.askyesno("Game Over", "Time's up! Would you like to play again?"):
            reset_game()

    def card_clicked(i, j):
        nonlocal first_card, second_card, locked

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
        nonlocal first_card, second_card, matched_pairs, locked
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
        nonlocal locked
        locked = True
        timer_label.config(text="You win!")

        if timer_update is not None:
            root.after_cancel(timer_update)

        if messagebox.askyesno("Play Again?", "You won! Would you like to play again?"):
            reset_game()

    def reset_game():
        nonlocal cards, first_card, second_card, matched_pairs, locked, remaining_time, timer_update
        shuffle_cards()
        matched_pairs = 0
        locked = False
        first_card = None
        second_card = None
        remaining_time = time_limit
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



def season_2_easy():
    # Initialize the main game window
    root = tk.Tk()
    root.title("Shifty Chronicles")
    root.geometry("700x700")
    root.configure(bg='#FFE1DC')

    frame = tk.Frame(root, bg='#720000', padx=20, pady=20)
    frame.pack(expand=True)

    cards = []
    buttons = []
    first_card = None
    second_card = None
    matched_pairs = 0
    locked = False
    cover_image = tk.PhotoImage(file="shifty chronicles cover 2.png")  # Cover image

    # Load front images for the cards
    front_images = []
    image_files = [
        "s2card_0.png", "s2card_1.png", "s2card_2.png",
        "s2card_3.png", "s2card_4.png", "s2card_5.png",
        "s2card_6.png", "s2card_7.png"
    ]
    for file_name in image_files:
        front_images.append(tk.PhotoImage(file=file_name))

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
        nonlocal cards
        card_values = list(range(8)) * 2
        random.shuffle(card_values)
        cards = bubble_sort(card_values) if random.choice([True, False]) else quick_sort(card_values)
        random.shuffle(cards)

    def create_widgets():
        nonlocal buttons
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

    def card_clicked(i, j):
        nonlocal first_card, second_card, locked
        if locked:
            return
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
        nonlocal first_card, second_card, matched_pairs, locked
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
        nonlocal locked
        locked = True
        if messagebox.askyesno("Play Again?", "You won! Would you like to play again?"):
            reset_game()

    def reset_game():
        nonlocal cards, first_card, second_card, matched_pairs, locked
        cards = shuffle_cards()
        matched_pairs = 0
        locked = False
        first_card = None
        second_card = None

        for row in buttons:
            for button in row:
                button.config(image=cover_image, state="normal")

    shuffle_cards()
    create_widgets()
    root.mainloop()


def season_2_medium():
    # Initialize global variables
    root = tk.Tk()
    root.title("Shifty Chronicles")
    root.geometry("700x700")
    root.configure(bg='#FFE1DC')

    frame = tk.Frame(root, bg='#720000', padx=20, pady=20)
    frame.pack(expand=True)

    cards = []
    buttons = []
    first_card = None
    second_card = None
    matched_pairs = 0
    locked = False
    cover_image = None
    front_images = []
    time_limit = 60
    remaining_time = time_limit
    timer_update = None

    timer_label = tk.Label(root, text=f"Time: {remaining_time}", font=("Arial", 16), bg='#FFE1DC', fg='#720000')
    timer_label.pack(pady=10)

    def load_images():
        nonlocal cover_image, front_images
        cover_image = tk.PhotoImage(file="shifty chronicles cover 2.png")

        image_files = [
        "s2card_0.png", "s2card_1.png", "s2card_2.png",
        "s2card_3.png", "s2card_4.png", "s2card_5.png",
        "s2card_6.png", "s2card_7.png"
        ]

        for file_name in image_files:
            image = tk.PhotoImage(file=file_name)
            front_images.append(image)

    def shuffle_cards():
        nonlocal cards
        card_values = list(range(8)) * 2
        random.shuffle(card_values)
        # Use sorting to 'shuffle' further - can switch to bubble_sort or quick_sort
        cards = bubble_sort(card_values) if random.choice([True, False]) else quick_sort(card_values)
        random.shuffle(cards)  # Final random shuffle for better mix

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

    def create_widgets():
        nonlocal buttons
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
        nonlocal remaining_time, timer_update
        if remaining_time > 0:
            timer_label.config(text=f"Time: {remaining_time}")
            remaining_time -= 1
            timer_update = root.after(1000, update_timer)
        else:
            stop_game()

    def stop_game():
        nonlocal locked
        locked = True
        timer_label.config(text="Time's up!")
        if messagebox.askyesno("Game Over", "Time's up! Would you like to play again?"):
            reset_game()

    def card_clicked(i, j):
        nonlocal first_card, second_card, locked

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
        nonlocal first_card, second_card, matched_pairs, locked
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
        nonlocal locked
        locked = True
        timer_label.config(text="You win!")

        if timer_update is not None:
            root.after_cancel(timer_update)

        if messagebox.askyesno("Play Again?", "You won! Would you like to play again?"):
            reset_game()

    def reset_game():
        nonlocal cards, first_card, second_card, matched_pairs, locked, remaining_time, timer_update
        shuffle_cards()
        matched_pairs = 0
        locked = False
        first_card = None
        second_card = None
        remaining_time = time_limit

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


def season_2_hard():
    # Initialize global variables
    root = tk.Tk()
    root.title("Shifty Chronicles")
    root.geometry("700x700")
    root.configure(bg='#FFE1DC')

    frame = tk.Frame(root, bg='#720000', padx=20, pady=20)
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

    timer_label = tk.Label(root, text=f"Time: {remaining_time}", font=("Arial", 16), bg='#FFE1DC', fg='#720000')
    timer_label.pack(pady=10)

    def load_images():
        nonlocal cover_image, front_images
        cover_image = tk.PhotoImage(file="shifty chronicles cover 2.png")

        image_files = [
        "s2card_0.png", "s2card_1.png", "s2card_2.png",
        "s2card_3.png", "s2card_4.png", "s2card_5.png",
        "s2card_6.png", "s2card_7.png"
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
        nonlocal cards
        card_values = list(range(8)) * 2
        random.shuffle(card_values)
        cards = bubble_sort(card_values) if random.choice([True, False]) else quick_sort(card_values)
        random.shuffle(cards)

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
        nonlocal remaining_time, timer_update
        if remaining_time > 0:
            timer_label.config(text=f"Time: {remaining_time}")
            remaining_time -= 1
            timer_update = root.after(1000, update_timer)
        else:
            stop_game()

    def stop_game():
        nonlocal locked
        locked = True
        timer_label.config(text="Time's up!")
        if messagebox.askyesno("Game Over", "Time's up! Would you like to play again?"):
            reset_game()

    def card_clicked(i, j):
        nonlocal first_card, second_card, locked

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
        nonlocal first_card, second_card, matched_pairs, locked
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
        nonlocal locked
        locked = True
        timer_label.config(text="You win!")

        if timer_update is not None:
            root.after_cancel(timer_update)

        if messagebox.askyesno("Play Again?", "You won! Would you like to play again?"):
            reset_game()

    def reset_game():
        nonlocal cards, first_card, second_card, matched_pairs, locked, remaining_time, timer_update
        shuffle_cards()
        matched_pairs = 0
        locked = False
        first_card = None
        second_card = None
        remaining_time = time_limit

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



def season_3_easy():
    # Initialize global variables
    root = tk.Tk()
    root.title("Shifty Chronicles")
    root.geometry("700x700")
    root.configure(bg='#E8D7FF') 

    frame = tk.Frame(root, bg='#3E015E', padx=20, pady=20)
    frame.pack(expand=True)

    cards = []
    buttons = []
    first_card = None
    second_card = None
    matched_pairs = 0
    locked = False
    cover_image = None
    front_images = []  # To store the front images

    def load_images():
        nonlocal cover_image, front_images
        cover_image = tk.PhotoImage(file="shifty chronicles cover 3.png")  # Make sure cover image is in this path

        front_images.clear()
        image_files = [
            "s3card_0.png", "s3card_1.png", "s3card_2.png",
            "s3card_3.png", "s3card_4.png", "s3card_5.png",
            "s3card_6.png", "s3card_7.png"
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
        nonlocal cards
        card_values = list(range(8)) * 2
        random.shuffle(card_values)
        # Use sorting to 'shuffle' further - can switch to bubble_sort or quick_sort
        cards = bubble_sort(card_values) if random.choice([True, False]) else quick_sort(card_values)
        random.shuffle(cards)  # Final random shuffle for better mix

    def create_widgets():
        for i in range(4):
            row = []
            for j in range(4):
                # Create a button with the cover image initially
                button = tk.Button(frame, image=cover_image, width=100, height=100,
                                   command=lambda i=i, j=j: card_clicked(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            buttons.append(row)

        # Adjust grid for alignment
        for i in range(4):
            frame.grid_columnconfigure(i, weight=1)
        for j in range(4):
            frame.grid_rowconfigure(j, weight=1)

    def card_clicked(i, j):
        nonlocal first_card, second_card, locked

        if locked:
            return

        button = buttons[i][j]
        card_index = cards[i * 4 + j]

        # If the button is still covered, reveal it
        if button['image'] == str(cover_image):
            button.config(image=front_images[card_index])  # Show front image based on card index

            if first_card is None:
                first_card = (i, j)  # Save first selected card position
            else:
                second_card = (i, j)  # Save second selected card position
                locked = True
                root.after(1000, check_for_match)  # Check for a match after a delay

    def check_for_match():
        nonlocal first_card, second_card, matched_pairs, locked
        first_i, first_j = first_card
        second_i, second_j = second_card

        if cards[first_i * 4 + first_j] == cards[second_i * 4 + second_j]:
            matched_pairs += 1
            buttons[first_i][first_j].config(state="disabled")  # Disable matched buttons
            buttons[second_i][second_j].config(state="disabled")

            if matched_pairs == 8:
                show_winner()
        else:
            root.after(500, hide_cards, first_i, first_j, second_i, second_j)  # Cover cards again if not a match

        first_card = None
        second_card = None
        locked = False

    def hide_cards(first_i, first_j, second_i, second_j):
        # Hide both unmatched cards by setting the cover image again
        buttons[first_i][first_j].config(image=cover_image)
        buttons[second_i][second_j].config(image=cover_image)

    def show_winner():
        nonlocal locked
        locked = True

        if messagebox.askyesno("Play Again?", "You won! Would you like to play again?"):
            reset_game()

    def reset_game():
        nonlocal cards, first_card, second_card, matched_pairs, locked
        cards = generate_cards()  # Shuffle cards again
        matched_pairs = 0
        locked = False
        first_card = None
        second_card = None

        for row in buttons:
            for button in row:
                button.config(image=cover_image, state="normal")  # Reset buttons with cover image

    # Initialize game
    load_images()
    shuffle_cards()
    create_widgets()

    root.mainloop()


def season_3_medium():
    # Initialize the main window
    root = tk.Tk()
    root.title("Shifty Chronicles")
    root.geometry("700x700")
    root.configure(bg='#E8D7FF')

    # Initialize frame and other UI components
    frame = tk.Frame(root, bg='#3E015E', padx=20, pady=20)
    frame.pack(expand=True)

    # Global game variables
    cards = []
    buttons = []
    first_card = None
    second_card = None
    matched_pairs = 0
    locked = False
    cover_image = None
    front_images = []
    time_limit = 60
    remaining_time = time_limit
    timer_update = None

    # Timer label
    timer_label = tk.Label(root, text=f"Time: {remaining_time}", font=("Arial", 16), bg='#E8D7FF', fg='#3E015E')
    timer_label.pack(pady=10)

    def load_images():
        nonlocal cover_image, front_images
        cover_image = tk.PhotoImage(file="shifty chronicles cover 3.png")

        image_files = [
            "s3card_0.png", "s3card_1.png", "s3card_2.png",
            "s3card_3.png", "s3card_4.png", "s3card_5.png",
            "s3card_6.png", "s3card_7.png"
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
        nonlocal cards
        card_values = list(range(8)) * 2
        random.shuffle(card_values)
        cards = bubble_sort(card_values) if random.choice([True, False]) else quick_sort(card_values)
        random.shuffle(cards)

    def create_widgets():
        nonlocal buttons
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
        nonlocal remaining_time, timer_update
        if remaining_time > 0:
            timer_label.config(text=f"Time: {remaining_time}")
            remaining_time -= 1
            timer_update = root.after(1000, update_timer)
        else:
            stop_game()

    def stop_game():
        nonlocal locked
        locked = True
        timer_label.config(text="Time's up!")
        if messagebox.askyesno("Game Over", "Time's up! Would you like to play again?"):
            reset_game()

    def card_clicked(i, j):
        nonlocal first_card, second_card, locked
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
        nonlocal first_card, second_card, matched_pairs, locked
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
        nonlocal locked
        locked = True
        timer_label.config(text="You win!")

        if timer_update is not None:
            root.after_cancel(timer_update)

        if messagebox.askyesno("Play Again?", "You won! Would you like to play again?"):
            reset_game()

    def reset_game():
        nonlocal cards, first_card, second_card, matched_pairs, locked, remaining_time, timer_update
        shuffle_cards()
        matched_pairs = 0
        locked = False
        first_card = None
        second_card = None
        remaining_time = time_limit

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


def season_3_hard():
    # Initialize main window
    root = tk.Tk()
    root.title("Shifty Chronicles")
    root.geometry("700x700")
    root.configure(bg='#E8D7FF')

    frame = tk.Frame(root, bg='#3E015E', padx=20, pady=20)
    frame.pack(expand=True)

    # Initialize variables
    cards = []
    buttons = []
    first_card = None
    second_card = None
    matched_pairs = 0
    locked = False
    cover_image = tk.PhotoImage(file="shifty chronicles cover 3.png")
    front_images = []
    time_limit = 40
    remaining_time = time_limit
    timer_update = None

    timer_label = tk.Label(root, text=f"Time: {remaining_time}", font=("Arial", 16), bg='#E8D7FF', fg='#3E015E')
    timer_label.pack(pady=10)

    def load_images():
        image_files = [
            "s3card_0.png", "s3card_1.png", "s3card_2.png",
            "s3card_3.png", "s3card_4.png", "s3card_5.png",
            "s3card_6.png", "s3card_7.png"
        ]
        for file_name in image_files:
            image = tk.PhotoImage(file=file_name)
            front_images.append(image)

    def shuffle_cards():
        nonlocal cards
        card_values = list(range(8)) * 2
        random.shuffle(card_values)
        cards = card_values

    def create_widgets():
        nonlocal buttons
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
        nonlocal remaining_time, timer_update
        if remaining_time > 0:
            timer_label.config(text=f"Time: {remaining_time}")
            remaining_time -= 1
            timer_update = root.after(1000, update_timer)
        else:
            stop_game()

    def stop_game():
        nonlocal locked
        locked = True
        timer_label.config(text="Time's up!")
        if messagebox.askyesno("Game Over", "Time's up! Would you like to play again?"):
            reset_game()

    def card_clicked(i, j):
        nonlocal first_card, second_card, locked
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
        nonlocal first_card, second_card, matched_pairs, locked
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
        nonlocal locked
        locked = True
        timer_label.config(text="You win!")

        if timer_update is not None:
            root.after_cancel(timer_update)

        if messagebox.askyesno("Play Again?", "You won! Would you like to play again?"):
            reset_game()

    def reset_game():
        nonlocal cards, first_card, second_card, matched_pairs, locked, remaining_time, timer_update
        shuffle_cards()
        matched_pairs = 0
        locked = False
        first_card = None
        second_card = None
        remaining_time = time_limit

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

season_1_easy()
season_1_medium()
season_1_hard()
season_2_easy()
season_2_medium()
season_2_hard()
season_3_easy()
season_3_medium()
season_3_hard()
