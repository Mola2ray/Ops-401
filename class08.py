#!/usr/bin/python3
# Lamin Touray
# Scripts: Add a feature capability to your Python encryption tool to:
# Alter the desktop wallpaper on a Windows PC with a ransomware message
# Create a popup window on a Windows PC with a ransomware message

import os, time
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont
from cryptography.fernet import Fernet

# ... (all previous functions, except set_wallpaper)

# New function for creating an image with ransomware message
def create_ransom_image(message, image_path):
    img = Image.new('RGB', (800, 600), color=(255, 0, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 24)
    draw.text((50, 300), message, font=font, fill=(0, 0, 0))
    img.save(image_path)

def create_popup_window(image_path):
    window = tk.Tk()
    window.title("Ransomware Message")
    img = ImageTk.PhotoImage(Image.open(image_path))
    label = tk.Label(window, image=img)
    label.pack()
    button = tk.Button(window, text="OK", command=window.destroy)
    button.pack(pady=10)
    window.mainloop()

# Update the display_menu function to include the new features
def display_menu():
    menu = ["1: Encrypt a file", "2: Decrypt a file", "3: Encrypt a message", "4: Decrypt a message", "5: Encrypt a folder", "6: Decrypt a folder", "7: Display popup with ransomware message", "8: Exit"]
    for i in menu:
        print(i)

# ... (all other existing functions)

# Main loop with the new options
while True:
    display_menu()
    mode = input("Please select a mode: \n")

    # ... (previous options)

    if mode == "7":
        ransom_message = input("Enter the ransomware message: ")
        image_path = "ransom_image.png"
        create_ransom_image(ransom_message, image_path)
        create_popup_window(image_path)

    elif mode == "8":
        exit()
    else:
        print(f"""
You entered {mode}
That is an invalid input.
Please input a number between 1 and 8.
""")
        time.sleep(2)

# Sources: chaGPT