import tkinter as tk
import requests
import json

# Function to make the API request and parse the response
def get_movie_info():
    # Get the movie name from the form
    movie_name = movie_name_entry.get()

    # Make a GET request to the Rotten Tomatoes API to search for the movie
    api_key = "f779f5fd"
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={movie_name}"
    response = requests.get(url)

    # Parse the response data
    data = json.loads(response.text)

    # Clear any existing labels
    for widget in root.winfo_children():
        widget.destroy()

    # Add a label for each key-value pair in the data dictionary
    row = 0
    for key, value in data.items():
        label = tk.Label(root, text=f"{key}: {value}")
        label.grid(row=row, column=0, padx=10, pady=10)
        row += 1

# Create the form
root = tk.Tk()
root.title("Movie Info")

# Add a label for the movie name input
movie_name_label = tk.Label(root, text="Enter movie name:")
movie_name_label.grid(row=0, column=0, padx=10, pady=10)

# Add an entry for the movie name
movie_name_entry = tk.Entry(root)
movie_name_entry.grid(row=0, column=1, padx=10, pady=10)

# Add a button to submit the movie name\\\\\
submit_button = tk.Button(root, text="Submit", command=get_movie_info)
submit_button.grid(row=0, column=2, padx=10, pady=10)

root.mainloop()
