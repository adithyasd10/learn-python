# This Tkinter program creates a GUI application that checks if a given string is a palindrome,
# reverses the string, and records the data based on user type:
# 
# - Administrator (radio button 1): If the entered string is a palindrome, it is stored in a text file (`PalindromeText.txt`).
# - User (radio button 0): The entered string and its reversed version are stored in a CSV file (`ReversedTable.csv`).
#
# Features:
# 1. GUI built with Tkinter and ttk widgets.
# 2. Input validation: Only alphanumeric characters allowed.
# 3. Reverse string display.
# 4. File handling (creates text and CSV files if they do not exist).
#
# Example Run:
# - Select "Administrator", type "madam" → Display reversed string "madam" → Added to PalindromeText.txt
# - Select "User", type "hello" → Display reversed string "olleh" → Added to ReversedTable.csv
#
# How to run:
# 1. Save this file as palindrome_checker_gui.py
# 2. Make sure Python's Tkinter module is installed (it is included in standard Python).
# 3. Run in terminal:
#       python palindrome_checker_gui.py
# 4. Use the GUI to test palindrome functionality.

import tkinter as tk
import os.path
from tkinter import ttk
from tkinter import messagebox
import csv

def verify_user_entry(event):
    reverse_label.config(text="")
    if not event.char.isalnum():
        given_string_entry.delete(0, tk.END)
        given_string_entry.insert(0, given_string_entry.get()[:-1])

def showReverse():
    given_str = given_string_entry.get()
    if len(given_str.strip()) > 0:
        result_str = given_str[::-1]
        reverse_label.config(text=result_str)
        record_data(privilege.get())
    else:
        messagebox.showwarning("Empty", "Please enter a string")

def clear_all():
    given_string_entry.delete(0, tk.END)
    reverse_label.config(text="")

def record_data(user_type):
    if user_type == 1:
        given_str = given_string_entry.get()
        reversed_str = given_str[::-1]
        if given_str == reversed_str:
            with open(txt_file, 'a', newline='') as fp:
                fp.write(given_str + '\n')
        else:
            with open(csv_file, 'a', newline='') as fp:
                writer = csv.writer(fp)
                writer.writerow([given_str, reversed_str])

root = tk.Tk()
root.geometry("500x500")
root.title('Palindrome Check')
root.resizable(1, 1)

privilege = tk.IntVar()
pal_label = ttk.Label(root, text="PALINDROME CHECK")
pal_label.grid(column=0, row=0, sticky=tk.W, padx=20, pady=20, columnspan=2)

admin_rdo_btn = ttk.Radiobutton(root, text="Administrator", variable=privilege, value=1, command=clear_all)
admin_rdo_btn.grid(column=0, row=1, sticky=tk.W, padx=20, pady=20)

user_rdo_btn = ttk.Radiobutton(root, text="User", variable=privilege, value=0, command=clear_all)
user_rdo_btn.grid(column=1, row=1, sticky=tk.W, padx=20, pady=20)

txt_file = 'PalindromeText.txt'
csv_file = 'ReversedTable.csv'

if not os.path.exists(txt_file):
    with open(txt_file, 'w', newline='') as fp:
        fp.write('Palindrome List\n===============\n')

if not os.path.exists(csv_file):
    with open(csv_file, 'w', newline='') as fp:
        writer = csv.writer(fp)
        writer.writerow(['Given', 'Reversed'])

given_string_label = ttk.Label(root, text="Given String")
given_string_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

given_string_entry = ttk.Entry(root)
given_string_entry.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
given_string_entry.bind('<KeyRelease>', verify_user_entry)

reverse_btn = ttk.Button(root, text="Reverse", command=showReverse)
reverse_btn.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5, columnspan=2)

result_label = ttk.Label(root, text="Reversed String")
result_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5, columnspan=2)

reverse_label = ttk.Label(root, text="", font='Helvetica 22 bold')
reverse_label.grid(column=0, row=6, sticky=tk.W, padx=5, pady=5, columnspan=2)

root.mainloop()
