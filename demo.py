import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Image Example")

# Load the image (ensure the file path is correct)
image = tk.PhotoImage(file="c.png")

# Display the image in a label
label = tk.Label(root, image=image)
label.pack()

# Run the application
root.mainloop()
