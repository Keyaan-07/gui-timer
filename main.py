import tkinter as tk
import time
from threading import Thread

root = tk.Tk()
root.geometry('500x500')
root.title('GUI Timer')

hours_remaining = int()
minutes_remaining = int()
seconds_remaining  = int()
time_remaining = int()

title_label = tk.Label(root, text='T~TTI~TTIME~~TIMERR', font=('Arial', 24))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

hours_label = tk.Label(root, text='Hours:', font=('Arial', 18))
hours_label.grid(row=1, column=0, padx=10, pady=10)
hours = tk.Entry(root, font=('Arial', 18), width=5)
hours.grid(row=1, column=1, padx=10, pady=10)

minutes_label = tk.Label(root, text='Minutes:', font=('Arial', 18))
minutes_label.grid(row=2, column=0, padx=10, pady=10)
minutes = tk.Entry(root, font=('Arial', 18), width=5)
minutes.grid(row=2, column=1, padx=10, pady=10)

seconds_label = tk.Label(root, text='Seconds:', font=('Arial', 18))
seconds_label.grid(row=3, column=0, padx=10, pady=10)
seconds = tk.Entry(root, font=('Arial', 18), width=5)
seconds.grid(row=3, column=1, padx=10, pady=10)

time_remaining_label = tk.Label(root, text='00:00:00', font=('Arial', 24))
time_remaining_label.grid(row=4, column=0, columnspan=2, pady=10)


def update_timer_label(hours_remaining, minutes_remaining, seconds_remaining):
    time_remaining_label.config(
        text=f'{hours_remaining:02}:{minutes_remaining:02}:{seconds_remaining:02}'
    )


def countdown():
    global time_remaining

    hours_value = int(hours.get()) if hours.get().isdigit() else 0
    minutes_value = int(minutes.get()) if minutes.get().isdigit() else 0
    seconds_value = int(seconds.get()) if seconds.get().isdigit() else 0

    time_remaining = hours_value * 3600 + minutes_value * 60 + seconds_value

    while time_remaining > 0:
        hours_remaining = time_remaining // 3600
        minutes_remaining = (time_remaining % 3600) // 60
        seconds_remaining = time_remaining % 60
        update_timer_label(hours_remaining, minutes_remaining, seconds_remaining)

        time.sleep(1)
        time_remaining -= 1

    update_timer_label(0, 0, 0)

def stop_timer():
    global time_remaining

    update_timer_label(0, 0, 0)
    time_remaining=0

def start_timer():
    timer_thread = Thread(target=countdown)
    timer_thread.daemon = True
    timer_thread.start()


start_tim = tk.Button(root, text='Start', command=start_timer)
start_tim.grid(row=5, column=0, columnspan=2)
stop_tim = tk.Button(root, text='Stop', command=stop_timer)
stop_tim.grid(row=5, column=1, columnspan=2)


root.mainloop()