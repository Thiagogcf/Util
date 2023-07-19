import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import time

# Define the time intervals
inicio = datetime.now().timestamp()
inicioexpediente = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 7, 33, 0).timestamp()
iniciotarde = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 12,49, 0).timestamp()
iniciohora = datetime.now().time()

# Initial end times
final_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 17, 24, 0)
final2_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 11, 55, 0)

final = final_time.timestamp()
final2 = final2_time.timestamp()

# Create a new tkinter window
window = tk.Tk()
window.title("Time Tracker")
window.geometry('400x300')  # Set window size

# Add input fields to edit the final and final2 values
final_label = tk.Label(window, text="Final (HH:MM:SS):", font=('Helvetica', 12))
final_label.pack()
final_entry = tk.Entry(window)
final_entry.pack()
final_entry.insert(0, final_time.strftime("%H:%M:%S"))

final2_label = tk.Label(window, text="Final2 (HH:MM:SS):", font=('Helvetica', 12))
final2_label.pack()
final2_entry = tk.Entry(window)
final2_entry.pack()
final2_entry.insert(0, final2_time.strftime("%H:%M:%S"))

# Add a label to display the time left
time_label = tk.Label(window, text="", font=('Helvetica', 12))
time_label.pack()

# Add a canvas to display the gradient progress bar
canvas = tk.Canvas(window, width=300, height=20)
canvas.pack()

# Add a label to display the progress percentage
percentage_label = tk.Label(window, text="", font=('Helvetica', 12))
percentage_label.pack()

def interpolate_color(min_color, max_color, progress):
    return [int(min_c + (max_c - min_c) * progress) for min_c, max_c in zip(min_color, max_color)]

def update_progress_bar(progress):
    # Clear the canvas
    canvas.delete("all")

    # Define the start (purple) and end (red) colors
    min_color = (128, 0, 128)  # RGB for purple
    max_color = (255, 0, 0)  # RGB for red

    # Calculate the number of rectangles to draw (decreased for performance)
    num_rectangles = 50

    for i in range(num_rectangles):
        # Calculate the color for this rectangle
        rgb_color = interpolate_color(min_color, max_color, i/num_rectangles)
        hex_color = '#%02x%02x%02x' % tuple(rgb_color)

        # Calculate the position of this rectangle
        x1 = i * (canvas.winfo_width() / num_rectangles)
        x2 = x1 + (canvas.winfo_width() / num_rectangles)

        # Only draw the rectangle if it's within the progress
        if x2 <= progress * canvas.winfo_width():
            canvas.create_rectangle(x1, 0, x2, canvas.winfo_height(), fill=hex_color, width=0)

def update():
    # Update the final and final2 values
    try:
        final_time_str = final_entry.get()
        final2_time_str = final2_entry.get()
        final_time = datetime.strptime(final_time_str, '%H:%M:%S')
        final2_time = datetime.strptime(final2_time_str, '%H:%M:%S')
        final = final_time.replace(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day).timestamp()
        final2 = final2_time.replace(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day).timestamp()
    except ValueError:
        messagebox.showerror("Error", "Invalid time format. Please enter time in HH:MM:SS format.")
        return

    if final > datetime.now().timestamp():
        # Update the progress bar and labels
        if 100 >= (((datetime.now().timestamp() - inicio) * 100) / (final2 - inicio)) >= 0:
            progress_value = ((datetime.now().timestamp()-inicio)*100)/(final2-inicio)
            time_label['text'] = 'Time left: ' + str((datetime.fromtimestamp(final2))-datetime.now())
            percentage_label['text'] = f'Progress: {progress_value:.2f}%'
            update_progress_bar(progress_value / 100)
        else:
            progress_value = ((datetime.now().timestamp()-inicio)*100)/(final-inicio)
            time_label['text'] = 'Time left: ' + str((datetime.fromtimestamp(final))-datetime.now())
            percentage_label['text'] = f'Progress: {progress_value:.2f}%'
            update_progress_bar(progress_value / 100)

        # Schedule the next update
        window.after(1000, update)  # Delay is in milliseconds

update()
window.mainloop()
