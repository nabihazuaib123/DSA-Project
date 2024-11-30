import tkinter as tk
from tkinter import font as tkfont
import os

DATA_FILE = "users_data.txt"

def load_user_names():
    users = {}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            for line in file:
                name = line.strip()
                users[name] = {"age": None, "score": 0, "progress": "Just Started"}
    return users

def save_user_names():
    global users_data
    with open(DATA_FILE, "w") as file:
        for name in users_data.keys():
            file.write(name + "\n")

users_data = load_user_names()

def create_fonts():
    try:
        heading_font = tkfont.Font(family="GAME", size=100)
    except Exception as e:
        print(f"Heading font could not be loaded: {e}")
        heading_font = tkfont.Font(family="Arial", size=100)

    try:
        fighting_spirit_font = tkfont.Font(family="Fighting Spirit turbo", size=50)
    except Exception as e:
        print(f"Fighting Spirit Turbo font could not be loaded: {e}")
        fighting_spirit_font = tkfont.Font(family="Arial", size=50)

    try:
        doctor_glitch_font = tkfont.Font(family="Doctor Glitch", size=40)
    except Exception as e:
        print(f"Doctor Glitch font could not be loaded: {e}")
        doctor_glitch_font = tkfont.Font(family="Arial", size=20)

    try:
        pirate_kids_font = tkfont.Font(family="Pirates Kids", size=20)
    except Exception as e:
        print(f"Pirate Kids font could not be loaded: {e}")
        pirate_kids_font = tkfont.Font(family="Arial", size=20)

    return heading_font, fighting_spirit_font, doctor_glitch_font, pirate_kids_font

# Create a global error label for displaying error messages
def create_error_label(root):
    error_label = tk.Label(root, text="", font=("Simple", 30), fg="black", bg="light blue")
    error_label.pack(pady=20)
    return error_label

# Update the error label text
def update_error_label(error_label, message):
    error_label.config(text=message)


def create_gradient_background(canvas, width, height, color1, color2):
    """Creates a gradient effect in the canvas."""
    for i in range(height):
        r = int(color1[0] + (color2[0] - color1[0]) * (i / height))
        g = int(color1[1] + (color2[1] - color1[1]) * (i / height))
        b = int(color1[2] + (color2[2] - color1[2]) * (i / height))
        color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_line(0, i, width, i, fill=color)


def welcome_screen():
    global window
    window = tk.Tk()
    window.title("Shifty Chronicles")
    window.geometry("1900x1000")

    # Gradient Background
    canvas = tk.Canvas(window, width=1900, height=1000)
    canvas.pack(fill="both", expand=True)
    create_gradient_background(canvas, 1900, 1000, (135, 206, 235), (135, 206, 250))

    # Fonts for the welcome screen
    heading_font, _, _, _ = create_fonts()

    # Game Title with bigger font
    large_heading_font = tkfont.Font(family="GAME", size=130)  # Bigger font for the title
    canvas.create_text(950, 300, text="Shifty \n\tChronicles", font=large_heading_font, fill="dark red")

    # Continue Button with smaller font
    continue_button = tk.Button(window, text="Continue", command=proceed_to_main_window, bg="yellow", font=("Fighting Spirit Turbo", 30))  # Smaller font for the button
    continue_button.place(relx=0.5, rely=0.6, anchor="center")

    window.mainloop()


def proceed_to_main_window():
    window.destroy()  # Close the welcome screen
    open_main_window()  # Open the main application window

def open_main_window():
    global window
    window = tk.Tk()
    window.title("One Piece Login & Signup System")
    window.geometry("1900x1000")
    window.resizable(False, False)
    window.configure(bg="lightblue")

    # Main container frame to hold both signup and login frames vertically
    main_frame = tk.Frame(window, bg="lightblue")
    main_frame.pack(pady=50)

    # Signup Frame
    signup_frame = tk.Frame(main_frame, bg="lightblue")
    signup_frame.pack(pady=20)  # Add space between frames

    tk.Label(signup_frame, text="Signup", font=("Fighting Spirit Turbo", 80, "bold"), bg="lightblue").grid(row=0, column=0, columnspan=2)
    tk.Label(signup_frame, text="Name:", bg="lightblue", font=("Pirates Kids", 30)).grid(row=1, column=0)
    
    global entry_name_signup, entry_age_signup
    entry_name_signup = tk.Entry(signup_frame, font=("Arial", 20), width=20)
    entry_name_signup.grid(row=1, column=1)

    tk.Label(signup_frame, text="Age:", bg="lightblue", font=("Pirates Kids", 30)).grid(row=2, column=0)
    entry_age_signup = tk.Entry(signup_frame, font=("Arial", 20), width=20)
    entry_age_signup.grid(row=2, column=1)

    signup_button = tk.Button(signup_frame, text="Signup", command=lambda: signup(error_label), bg="blue", fg="white", font=("Hey Comic", 15))
    signup_button.grid(row=3, column=0, columnspan=2)

    # Login Frame
    login_frame = tk.Frame(main_frame, bg="lightblue")
    login_frame.pack(pady=20)  # Add space between frames

    tk.Label(login_frame, text="Login", font=("Fighting Spirit Turbo", 70, "bold"), bg="lightblue").grid(row=0, column=0, columnspan=2)
    tk.Label(login_frame, text="Name:", bg="lightblue", font=("Pirates Kids", 30)).grid(row=1, column=0)
    
    global entry_name_login
    entry_name_login = tk.Entry(login_frame, font=("Arial", 20), width=20)
    entry_name_login.grid(row=1, column=1)

    # Create error label and pass to the login function
    error_label = create_error_label(window)

    login_button = tk.Button(login_frame, text="Login", command=lambda: login(error_label), bg="blue", fg="white", font=("Hey Comic", 15))
    login_button.grid(row=2, column=0, columnspan=2)

    window.mainloop()

def signup(error_label):
    global users_data
    name = entry_name_signup.get().strip().lower() 
    age = entry_age_signup.get()
    
    if not name or not age:
        update_error_label(error_label, "Please enter both name and age.")
    elif name in (user.lower() for user in users_data): 
        update_error_label(error_label, "This name is already registered.")
    else:
        try:
            age = int(age)
            users_data[name] = {"age": age, "score": 0, "progress": "Just Started"}
            update_error_label(error_label, f"{name.capitalize()} has been registered successfully!")
            entry_name_signup.delete(0, tk.END)
            entry_age_signup.delete(0, tk.END)
            save_user_names()
        except ValueError:
            update_error_label(error_label, "Please enter a valid age.")

# Initialize global variables
locked = False
paused = False




def hover_in(button, color):
    button.config(bg=color)

def hover_out(button, original_color):
    button.config(bg=original_color)

def clear_window(root):
    for widget in root.winfo_children():
        widget.destroy()

def main_menu(root, heading_font, fighting_spirit_font, doctor_glitch_font, pirate_kids_font):
    clear_window(root)

    canvas = tk.Canvas(root, width=1600, height=200, bg="sky blue", bd=0, highlightthickness=0)
    canvas.pack(pady=80)
    canvas.create_text(800, 100, text="Shifty Chronicles", font=heading_font, fill="red", tags="text")

    def glow_text():
        canvas.itemconfig("text", fill="orange")
        canvas.after(500, lambda: canvas.itemconfig("text", fill="red"))
        canvas.after(1000, glow_text)

    glow_text()

    season_frame = tk.Frame(root, bg="sky blue")
    season_frame.pack(pady=10)

    for i, (text, command) in enumerate([
    ("East Blue Saga", lambda root=root: select_complexity(root, "East Blue Saga", fighting_spirit_font, doctor_glitch_font, pirate_kids_font, heading_font)),
    ("Alabasta Saga", lambda root=root: select_complexity(root, "Alabasta Saga", fighting_spirit_font, doctor_glitch_font, pirate_kids_font, heading_font)),
    ("Skypiea Saga", lambda root=root: select_complexity(root, "Skypiea Saga", fighting_spirit_font, doctor_glitch_font, pirate_kids_font, heading_font))
    ]):
        button = tk.Button(season_frame, text=text, command=command, bg="light yellow", font=fighting_spirit_font)
        button.grid(row=0, column=i, padx=20)
        button.bind("<Enter>", lambda e, btn=button: hover_in(btn, "light green"))
        button.bind("<Leave>", lambda e, btn=button: hover_out(btn, "light yellow"))



def select_complexity(root, saga_selection, fighting_spirit_font, doctor_glitch_font, pirate_kids_font, heading_font):
    global saga  # Store the selected saga globally for access in start_game
    saga = saga_selection  # Update the saga based on the user's selection
    clear_window(root)
    tk.Label(root, text=f"Choose Your Crew's Challenge\n\n in the {saga}!", font=doctor_glitch_font, bg="sky blue").pack(pady=90)

    for level, text in [
        ("Beginner Pirate", "Beginner Pirate"),
        ("Bounty Hunter", "Bounty Hunter"),
        ("Warlord", "Warlord")
    ]:
        button = tk.Button(root, text=text, command=lambda level=level: start_game(root, level, fighting_spirit_font, pirate_kids_font, doctor_glitch_font, heading_font), bg="light green", font=fighting_spirit_font)
        button.pack(pady=5)
        button.bind("<Enter>", lambda e, btn=button: hover_in(btn, "light blue"))
        button.bind("<Leave>", lambda e, btn=button: hover_out(btn, "light green"))

        
def start_game(root, complexity, fighting_spirit_font, pirate_kids_font, doctor_glitch_font, heading_font):
    global locked, paused
    locked = False
    paused = False
    clear_window(root)

    tk.Label(root, text=f"Onward to the adventure as a {complexity}!", font=fighting_spirit_font, bg="sky blue").pack(pady=20)

    for text, command in [("Pause Game", lambda: pause_game(root, doctor_glitch_font)),
                          ("Reset Game", lambda: reset_game(root, fighting_spirit_font, doctor_glitch_font, heading_font, pirate_kids_font))]:
        button = tk.Button(root, text=text, command=command, bg="gold", font=pirate_kids_font)
        button.pack(pady=10)
        button.bind("<Enter>", lambda e, btn=button: hover_in(btn, "orange"))
        button.bind("<Leave>", lambda e, btn=button: hover_out(btn, "gold"))


def pause_game(root, doctor_glitch_font):
    global paused
    paused = True
    tk.Label(root, text="Game Paused", font=doctor_glitch_font, bg="sky blue").pack(pady=50)

def reset_game(root, fighting_spirit_font, doctor_glitch_font, heading_font, pirate_kids_font):
    global locked
    locked = False
    main_menu(root, heading_font, fighting_spirit_font, doctor_glitch_font, pirate_kids_font)


def login(error_label):
    name = entry_name_login.get().strip().lower()
    if name in users_data:
        start_application()  # Start the game when the user logs in
    else:
        update_error_label(error_label, "This name is not registered. Please sign up first.")

def start_application():
    global window
    window.destroy()  # Destroy the current window
    main_window = tk.Tk()  # Create a new Tk object
    main_window.geometry("1900x1000")
    main_window.configure(bg="sky blue")

    # Get the fonts before calling main_menu
    heading_font, fighting_spirit_font, doctor_glitch_font, pirate_kids_font = create_fonts()

    # Example - Main menu function to build gameplay
    main_menu(main_window, heading_font, fighting_spirit_font, doctor_glitch_font, pirate_kids_font)

    main_window.mainloop()

# Start the program with the welcome screen
welcome_screen()
