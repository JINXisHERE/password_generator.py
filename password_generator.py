import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    length = length_entry.get()
    try:
        if not length:
            length = 6
        else:
            length = int(length)
        if length <= 0:
            raise ValueError("Password length must be greater than 0")
        characters = ''
        if use_letters.get():
            characters += string.ascii_letters
        if use_numbers.get():
            characters += string.digits
        if use_special_chars.get():
            characters += string.punctuation
        if not characters:
            raise ValueError("Select at least one option")
        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def copy_password():
    password = password_entry.get()
    pyperclip.copy(password)
    messagebox.showinfo("Password Copied", "Password copied to clipboard")

def toggle_visibility():
    if password_entry['show'] == '':
        password_entry.config(show='*')
        show_button.config(text='Show Password')
    else:
        password_entry.config(show='')
        show_button.config(text='Hide Password')

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Length label and entry
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=5)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=5)
length_entry.insert(0, '6')  # Default length

# Character type checkboxes
use_letters = tk.BooleanVar()
letters_check = tk.Checkbutton(root, text="Use Letters", variable=use_letters)
letters_check.grid(row=1, column=0, padx=10, pady=5)

use_numbers = tk.BooleanVar()
numbers_check = tk.Checkbutton(root, text="Use Numbers", variable=use_numbers)
numbers_check.grid(row=1, column=1, padx=10, pady=5)

use_special_chars = tk.BooleanVar()
special_chars_check = tk.Checkbutton(root, text="Use Special Characters", variable=use_special_chars)
special_chars_check.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Password entry
password_entry = tk.Entry(root, width=30)
password_entry.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Show/Hide Password button
show_button = tk.Button(root, text="Show Password", command=toggle_visibility)
show_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Copy Password button
copy_button = tk.Button(root, text="Copy Password", command=copy_password)
copy_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Run the main event loop
root.mainloop()