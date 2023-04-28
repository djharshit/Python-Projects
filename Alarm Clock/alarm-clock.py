#!/usr/bin/env python3

"""
Alarm Clock with GUI using Python

"""
# Importing required modules
import time
import datetime
import winsound
import threading

import tkinter as tk
from tkinter import ttk

# Functions
def curr_time():
    curr_tm_lbl['text'] = time.strftime('%H %M %S')
    curr_tm_lbl.after(1000, curr_time)


def set_alarm():
    alarm_lbl['text'] = ''

    while True:
        time.sleep(1)
        time_now = time.strftime('%H %M %S')
        time_alarm = f'{hour.get()} {minute.get()} {second.get()}'

        if time_alarm == time_now:
            alarm_lbl['text'] = 'Alarm over !!!'

            for i in range(10):
                winsound.Beep(1000, 100)
                time.sleep(0.1)
            break


# Creating a window
wind = tk.Tk()

# Properties of the window
wind.title('Alarm Clock')
wind.geometry('300x300')
wind.resizable(False, False)

head_lbl = ttk.Label(wind, text='Alarm Clock', font=('', 25, 'bold'))
head_lbl.pack(padx=5, pady=5)

curr_tm_lbl = ttk.Label(wind, text='', font=('', 20))
curr_tm_lbl.pack(pady=5)

frame1 = ttk.Frame(wind, height=50, width=300)
frame1.pack(pady=5)

ttk.Label(frame1, text='Hour').grid(row=0, column=0)
hour = ttk.Combobox(frame1, values=list(range(24)), width=10)
hour.grid(row=1, column=0, padx=5)

ttk.Label(frame1, text='Min').grid(row=0, column=1)
minute = ttk.Combobox(frame1, values=list(range(60)), width=10)
minute.grid(row=1, column=1, padx=5)

ttk.Label(frame1, text='Sec').grid(row=0, column=2)
second = ttk.Combobox(frame1, values=list(range(60)), width=10)
second.grid(row=1, column=2, padx=5)

ttk.Button(wind, text='Set',
           command=lambda: threading.Thread(target=set_alarm).start()
           ).pack(pady=5)

alarm_lbl = ttk.Label(wind, text='', font=('', 20))
alarm_lbl.pack()

curr_time()

wind.mainloop()
