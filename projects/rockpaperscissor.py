import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk



def show_welcome_message():
    """Shows a simple messagebox popup when clicked."""
    messagebox.showinfo("Welcome", "Enjoy looking through my photo album!")

def open_details_window():
    """Opens a new Toplevel window to display photo details."""
  
    details_window = tk.Toplevel(root)
    details_window.title("Photo Details")
    details_window.geometry("300x150")
    
   
    details_label = tk.Label(
        details_window, 
        text="--- Photo Information ---", 
        font=("Arial", 12, "bold")
    )
    details_label.pack(pady=10)
    
    info_text = "Title: Beautiful Landscape\nDate Taken: June 2026\nLocation: National Park"
    info_label = tk.Label(details_window, text=info_text, font=("Arial", 10))
    info_label.pack(pady=5)
    
    close_button = tk.Button(details_window, text="Close", command=details_window.destroy)
    close_button.pack(pady=5)


root = tk.Tk()
root.title("My Photo Album")
root.geometry("450x500")

title_label = tk.Label(root, text="My Photo Album", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

try:
    #
    original_image = Image.open("album_photo.jpg")
    

    resized_image = original_image.resize((350, 250))
    
    tk_image = ImageTk.PhotoImage(resized_image)
    

    image_label = tk.Label(root, image=tk_image)
    image_label.pack(pady=10)
    
except FileNotFoundError:
    # Fallback text if the image file isn't found in the folder
    image_label = tk.Label(
        root, 
        text="[ Image file 'album_photo.jpg' not found. ]\nPlace an image in this directory to load it!", 
        fg="red", 
        font=("Arial", 10, "italic")
    )
    image_label.pack(pady=50)


greet_button = tk.Button(
    root, 
    text="Say Hello", 
    command=show_welcome_message, 
    width=20, 
    bg="lightblue"
)
greet_button.pack(pady=5)


details_button = tk.Button(
    root, 
    text="View Photo Details", 
    command=open_details_window, 
    width=20, 
    bg="lightgreen"
)
details_button.pack(pady=5)


root.mainloop()