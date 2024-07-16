# Import everything from the tkinter module
from tkinter import *

# Import everything from the ttk module, which provides themed widgets
from tkinter.ttk import *

# Define a function to change the value of the IntVar by a specified amount
def change(the_value, n):
    the_value.set(the_value.get() + n)

# Create the main window (root window) for the GUI application
window = Tk()

# Create an IntVar to hold an integer value, starting with 0
value = IntVar(window, 0)

# Create a Label widget to display the value of the IntVar
label = Label(window, textvariable=value)
label.pack()

# Create a Button widget labeled "Left +1, Right -1"
button = Button(window, text="Left +1, Right -1")

# Bind a lambda function to a left-click event (<Button-1>)
# The lambda function calls the change function, incrementing the value by 1
button.bind("<Button-1>", lambda event: change(value, 1))

# Bind a lambda function to a right-click event (<Button-3>)
# The lambda function calls the change function, decrementing the value by 1
button.bind("<Button-3>", lambda event: change(value, -1))

# Pack the Button widget
button.pack()

# Start the main event loop, waiting for user interaction
window.mainloop()
