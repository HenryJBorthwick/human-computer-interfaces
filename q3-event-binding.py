# Import everything from the tkinter module
from tkinter import *

# Import everything from the ttk module, which provides themed widgets
from tkinter.ttk import *

# Function to increment the value by 1
def add_one():
    value.set(value.get() + 1)

# Function to update the text of label2 to "WWWWOOOOWWWW"
# This function is triggered by an event, hence it has an event parameter
def wow(event):
    label2.config(text="WWWWOOOOWWWW")

# Create the main window (root window) for the GUI application
window = Tk()

# Create an IntVar to hold an integer value, starting with 0
value = IntVar(window, 0)

# Create a Label widget to display the value of the IntVar
label = Label(window, textvariable=value)
label.pack()

# Create another Label widget to display the "wow" message
label2 = Label(window)
label2.pack()

# Create a Button widget labeled "Add one"
# The command option specifies that the add_one function is called when the button is clicked
button = Button(window, text="Add one", command=add_one)

# Bind the wow function to a Shift + Double Left Click event on the button
# The event descriptor "<Shift-Double-Button-1>" specifies this combination of key and mouse events
button.bind("<Shift-Double-Button-1>", wow)
button.pack()

# Start the main event loop, waiting for user interaction
window.mainloop()
