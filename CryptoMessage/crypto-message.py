#!/usr/bin/env python3

"""
Message encoder decoder using Python

"""
# Importing required modules
import tkinter as tk

from cryptography.fernet import Fernet
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

# Functions
def generate_new_key():
    global key
    key = Fernet.generate_key()
    with open('key.key', 'wb') as file:
        file.write(key)
    messagebox.showinfo('Saved', 'Key is saved in key.key file')

def insert_new_key():
    global key
    key_file = filedialog.askopenfilename(title='Select key',
                                          filetypes=[('Key', '*.key')])
    if key_file:
        with open(key_file, 'rb') as file:
            key = file.read()

def encrypt_msg():
    if key is None:
        messagebox.showwarning('Insert', 'Insert a key')
        return
    try:
        f = Fernet(key)
        token = f.encrypt(e_msg.get().encode())
        e_msg.set(token.decode())
    except:
        messagebox.showwarning('Invalid', 'Cannot encrypt!')

def decrypt_msg():
    if key is None:
        messagebox.showwarning('Insert', 'Insert a key')
        return
    try:
        f = Fernet(key)
        token = f.decrypt(d_msg.get().encode())
        d_msg.set(token.decode())
    except:
        messagebox.showwarning('Invalid', 'Cannot decrypt!')

# Creating a window
wind = tk.Tk()

# Properties of the window
wind.title('Mesagge Coding')
wind.geometry('500x300')
wind.resizable(False, False)

# Variables
key = None
e_msg = tk.StringVar()
d_msg = tk.StringVar()

# Creating frames
key_frame = ttk.Frame(wind, height=50, width=500)
key_frame.grid_propagate(0)
key_frame.grid(row=0, column=0, columnspan=2)

encrypt_frame = ttk.Frame(wind, height=250, width=250)
encrypt_frame.grid_propagate(0)
encrypt_frame.grid(row=1, column=0)

decrypt_frame = ttk.Frame(wind, height=250, width=250)
decrypt_frame.grid_propagate(0)
decrypt_frame.grid(row=1, column=1)

# Key frame
gen_key_label = ttk.Label(key_frame, text='Generate key')
gen_key_label.grid(row=0, column=0, padx=5, pady=5)

gen_key_but = ttk.Button(key_frame, text='Generate',
                         command=generate_new_key)
gen_key_but.grid(row=0, column=1, padx=5, pady=5)

ins_key_label = ttk.Label(key_frame, text='\t\tInsert key')
ins_key_label.grid(row=0, column=2, padx=5, pady=5)

ins_key_but = ttk.Button(key_frame, text='Insert',
                         command=insert_new_key)
ins_key_but.grid(row=0, column=4, padx=5, pady=5)

# Encryption frame
encrypt_lab = ttk.Label(encrypt_frame, text='Encrypted message')
encrypt_lab.grid(row=0, column=0, padx=5, pady=5)

encrypt_ent = ttk.Entry(encrypt_frame, textvariable=e_msg, width=30)
encrypt_ent.grid(row=1, column=0, padx=5, pady=5)

encrypt_but = ttk.Button(encrypt_frame, text='Encrypt', command=encrypt_msg)
encrypt_but.grid(row=2, column=0, padx=5, pady=5)

encrypt_clr = ttk.Button(encrypt_frame, text='Clear',
                         command=lambda: e_msg.set(''))
encrypt_clr = ttk.Button(encrypt_frame, text='Clear', command=lambda: e_msg.set(''))
encrypt_clr.grid(row=3, column=0, padx=5, pady=5)

# Decryption frame
decrypt_lab = ttk.Label(decrypt_frame, text='Decrypted message')
decrypt_lab.grid(row=0, column=0, padx=5, pady=5)

decrypt_ent = ttk.Entry(decrypt_frame, textvariable=d_msg, width=30)
decrypt_ent.grid(row=1, column=0, padx=5, pady=5)

decrypt_but = ttk.Button(decrypt_frame, text='Decrypt', command=decrypt_msg)
decrypt_but.grid(row=2, column=0, padx=5, pady=5)

decrypt_clr = ttk.Button(decrypt_frame, text='Clear',
                         command=lambda: d_msg.set(''))
decrypt_clr = ttk.Button(decrypt_frame, text='Clear', command=lambda: d_msg.set(''))
decrypt_clr.grid(row=3, column=0, padx=5, pady=5)

wind.mainloop()
