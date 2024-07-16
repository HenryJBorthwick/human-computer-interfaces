# Boiler Plate
# Import everything from the tkinter module
from tkinter import *

# Import everything from the ttk module, which provides themed widgets
from tkinter.ttk import *

# Create the main window (root window) for the GUI application
window = Tk()

# Create a StringVar, a special Tkinter class for handling text variables
data = StringVar()

# Set the initial value of the StringVar
data.set("Data to display")

# Create a Label widget, which will display text from the StringVar 'data'
label = Label(window, textvariable=data)

# Use grid geometry manager to place the Label in row 0, column 0
label.grid(row=0, column=0)

# Create an Entry widget, which allows the user to enter text
# The text entered will be linked to the StringVar 'data'
entry = Entry(window, textvariable=data)

# Use grid geometry manager to place the Entry in row 1, column 0
entry.grid(row=1, column=0)

# Q1 Starts
# Define a function to clear the data in the StringVar
def clear_data(data):
    data.set("")

# Q1 Provided Code
# Create a Button widget to clear the text in the Entry and Label widgets
# The button will call the clear_data function when clicked
clear = Button(window, text="Clear", command=lambda: clear_data(data))
clear.grid(row=2, column=0)

# Q2 Provided Code
# Configure the style for all ttk Buttons
s = Style()
s.configure('TButton', font='helvetica 24', foreground='green')

# Q1 Provided Code
# Create a Button widget to quit the application
# The button will destroy the root window when clicked
quit = Button(window, text="Quit", command=window.destroy)
quit.grid(row=3, column=0)

# Start the main event loop, waiting for user interaction
window.mainloop()
