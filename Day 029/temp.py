# debug_password_manager.py
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
from PIL import Image, ImageTk
import PIL
import os

print("Current working dir:", os.getcwd())
print("Pillow version:", getattr(PIL, "__version__", "unknown"))

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("0123456789")
    symbols = list("!#$%&()*+")
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    try:
        pyperclip.copy(password)
    except Exception as e:
        print("pyperclip error:", e)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get().strip()
    if not website:
        messagebox.showinfo(title="Error", message="Please enter a website to search.")
        return
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
        return

    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title=website, message=f"Email : {email}\nPassword : {password}\n\nYour Password is copied to your clipboard.")
        try:
            pyperclip.copy(password)
        except Exception as e:
            print("pyperclip error:", e)
    else:
        messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        return

    new_data = {website: {"email": email, "password": password}}
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        with open("data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
    else:
        data.update(new_data)
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
# ensure window is large enough to display UI
window.geometry("720x380")
window.config(padx=20, pady=20)

# make columns behave nicely
window.grid_columnconfigure(0, weight=0)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=0)

# Canvas + Logo (safe image loading & persistent reference)
canvas = Canvas(window, width=200, height=200, highlightthickness=0)
img_path = "/Users/vmangla/Documents/Vaibhav/Programming/Programming in Python/100 - Days of Code/Day 29-30/logo.png"
try:
    img = Image.open(img_path)
    # convert to a safe mode and resize to fit canvas
    img = img.convert("RGBA")
    img.thumbnail((200, 200), Image.LANCZOS)
    logo = ImageTk.PhotoImage(img)
    canvas.create_image(100, 100, image=logo)
    # KEEP A REFERENCE so it is not garbage-collected
    canvas.image = logo
    window.logo = logo
    print("Loaded logo from:", img_path)
except Exception as e:
    print("Failed to load logo:", e)
    canvas.create_text(100, 100, text="🔐\nPassword\nManager", font=("Arial", 16, "bold"))

canvas.grid(row=0, column=1, pady=(0, 10))

# Labels:
website_label = Label(window, text="Website:", font=("Arial", 12))
website_label.grid(row=1, column=0, sticky="w", pady=2)

email_label = Label(window, text="Email/Username:", font=("Arial", 12))
email_label.grid(row=2, column=0, sticky="w", pady=2)

password_label = Label(window, text="Password:", font=("Arial", 12))
password_label.grid(row=3, column=0, sticky="w", pady=2)

# Entries:
website_entry = Entry(window, width=40)
website_entry.grid(row=1, column=1, sticky="we", padx=5)
website_entry.focus()

email_entry = Entry(window, width=60)
email_entry.grid(row=2, column=1, columnspan=2, sticky="we", padx=5)
email_entry.insert(0, "vmangla0704@gmail.com")

password_entry = Entry(window, width=40)
password_entry.grid(row=3, column=1, sticky="we", padx=5)

# Buttons:
generate_pass_button = Button(window, text="Generate Password", command=generate_password)
generate_pass_button.grid(row=3, column=2, sticky="w", padx=5)

add_button = Button(window, text="Add", width=40, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="we", pady=10, padx=5)

search_button = Button(window, text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2, sticky="e", padx=5)

window.mainloop()
