# Import everything from the tkinter module
from tkinter import *

# Import everything from the ttk module, which provides themed widgets
from tkinter.ttk import *

# Create the main window (root window) for the GUI application
window = Tk()

# List of labels for the buttons, indicating their placement sides
side_labels = ["bottom1", "bottom2", "top1", "top2", "left1", "right1"]

# Loop through each label in side_labels
for theside in side_labels:
    # Create a Button widget with text from the current label
    button = Button(window, text=theside)
    # Use the pack geometry manager to place the button
    # The side argument specifies which side of the window the button should be placed
    button.pack(side=theside[0:-1])

# Start the main event loop, waiting for user interaction
window.mainloop()
