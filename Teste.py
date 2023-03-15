import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import requests
import json

def get_movie_info():
    movie_name = movie_name_entry.get()

    api_key = "f779f5fd"
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={movie_name}"
    response = requests.get(url)

    data = json.loads(response.text)

    for widget in frame.winfo_children():
        widget.destroy()

    row = 0
    for key, value in data.items():
        label = ttk.Label(frame, text=f"{key}: {value}", font=("Helvetica", 12))
        label.grid(row=row, column=0, padx=10, pady=10)
        row += 1

root = ThemedTk(theme="equilux")
root.title("Movie Info")

root.configure(bg="#3a3a3a")

frame = ttk.Frame(root, padding=10)
frame.grid(row=1, column=0, columnspan=3, padx=20, pady=20)

style = ttk.Style()
style.configure("TLabel", background="#3a3a3a", foreground="#e6e6e6", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12), borderwidth=0)
style.configure("TEntry", font=("Helvetica", 12))

movie_name_label = ttk.Label(root, text="Enter movie name:")
movie_name_label.grid(row=0, column=0, padx=10, pady=10)

movie_name_entry = ttk.Entry(root, width=30)
movie_name_entry.grid(row=0, column=1, padx=10, pady=10)

submit_button = ttk.Button(root, text="Submit", command=get_movie_info)
submit_button.grid(row=0, column=2, padx=10, pady=10)

root.update()
root.minsize(root.winfo_width(), root.winfo_height())

root.mainloop()
