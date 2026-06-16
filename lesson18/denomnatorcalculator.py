# 1) Import required libraries:

# a) Import Tkinter widgets (`from tkinter import *`) and `messagebox`.

# b) Import PIL tools (`Image`, `ImageTk`) to load and show an image.

# 2) Create the main window:

# a) Create `root` using `Tk()`.

# b) Set title, background color, and window size using `.title()`, `.configure()`, `.geometry()`.

# 3) Add an image to the main window:

# a) Open an image file using `Image.open()`.

# b) Resize it using `.resize()`.

# c) Convert it to Tkinter format using `ImageTk.PhotoImage()`.

# d) Place the image on the window using a `Label` and `.place()`.

# 4) Add a welcome text label:

# a) Create a label with a welcome message.

# b) Position it near the bottom using `.place()`.

# 5) Create a function to show a message box:

# a) Display an info box using `messagebox.showinfo()`.

# b) If user clicks OK, open the top window by calling `topwin()`.

# 6) Add a button on the main window:

# a) Create a button with text like "Let's get started!".

# b) Connect it to the message box function using `command=...`.

# c) Place the button using `.place()`.

# 7) Create a function to open the top window:

# a) Create a new window using `Toplevel(root)`.

# b) Set title, background, and size.

# c) Place/position widgets inside the top window (labels, entries, buttons, output fields).

# d) Run the top window loop.

# 8) Start the main application:

# a) Use `root.mainloop()` to keep the main window running.






# Import necessary libraries
from tkinter import *
 
# Setting up Main Window
root = Tk()
root.geometry("400x300")
root.title("main")

# Function to open New (Top Level) Window
def topwin():
	# Setting up Top Window
	top = Toplevel()
	top.geometry("180x100")
	top.title("toplevel")
	# Adding a label widget to Top Window
	l2 = Label(top, text = "This is toplevel window")
	l2.pack()

	top.mainloop()

# Adding a label and button Widget to Root (Main) Window
l = Label(root, text = "This is root window")
btn = Button(root, text = "Click here to open another window", command = topwin)

# Arranging widgets
l.pack()
btn.pack()


