# This program is a Tkinter-based GUI application that checks whether a given string is a palindrome.
# The user enters a string in the input box, and upon clicking the "Reverse" button, 
# the program displays the reversed string and shows a message box indicating whether it is a palindrome or not.
#
# Example:
# Input: "madam"
# Output on GUI: "madam"
# Messagebox: "madam is a Palindrome"
#
# Input: "hello"
# Output on GUI: "olleh"
# Messagebox: "olleh is Not a Palindrome"
#
# How to run:
# 1. Save this file as palindrome_checker_gui.py
# 2. Make sure you have Python installed (Tkinter comes pre-installed with most Python distributions).
# 3. Run the program using:
#       python palindrome_checker_gui.py
# 4. A window will appear. Enter a string, click "Reverse", and see the result.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.geometry("500x500")
root.title('Palindrome Check')
root.resizable(1, 1)

def showReverse():
    given_str = given_string_entry.get()
    if len(given_str.strip()) > 0:
        result_str = given_str[::-1]
        reverse_label.config(text=result_str)
    else:
        messagebox.showwarning("Empty", "Please enter a string")
        return

    if given_str == result_str:
        messagebox.showinfo(result_str, "Palindrome")
    else:
        messagebox.showinfo(result_str, "Not a Palindrome")

pal_label = ttk.Label(root, text="PALINDROME CHECK")
pal_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=35, columnspan=2)

given_string_label = ttk.Label(root, text="Given String")
given_string_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

given_string_entry = ttk.Entry(root)
given_string_entry.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

reverse_btn = ttk.Button(root, text="Reverse", command=showReverse)
reverse_btn.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5, columnspan=2)

result_label = ttk.Label(root, text="Reversed String")
result_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5, columnspan=2)

reverse_label = ttk.Label(root, text="", font='Helvetica 22 bold')
reverse_label.grid(column=0, row=6, sticky=tk.W, padx=5, pady=5, columnspan=2)

root.mainloop()
