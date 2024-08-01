import requests
import tkinter as tk
from tkinter import messagebox


def check_website(url, keywords):
    try:
        # Send a GET request to the website
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Convert the content to lowercase for case-insensitive search
            content = response.text.lower()

            # Check if any of the keywords are in the content
            if any(keyword in content for keyword in keywords):
                # Create a root window (it won't be shown)
                root = tk.Tk()
                root.withdraw()

                # Show the message box
                messagebox.showinfo("Keyword Found", "It's available in Brazil!")

                # Destroy the root window
                root.destroy()
            else:
                print("Keywords not found on the website.")
        else:
            print(f"Failed to retrieve the website. Status code: {response.status_code}")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")


# Example usage
# url = "https://www.anthropic.com/claude-ai-locations"  # Replace with the website you want to check
url = 'https://support.anthropic.com/en/articles/8461763-where-can-i-access-claude-ai'
url2 = 'https://www.anthropic.com/claude-ai-locations'
keywords = ["brazil", "brasil"]

check_website(url, keywords)
check_website(url2, keywords)