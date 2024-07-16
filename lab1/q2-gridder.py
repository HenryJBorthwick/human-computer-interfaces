# Import everything from the tkinter module
from tkinter import *

# Import everything from the ttk module, which provides themed widgets
from tkinter.ttk import *

# Create the main window (root window) for the GUI application
window = Tk()

# Loop through numbers 0 to 5
for label_num in range(6):
    # Create a Button widget with text "Button" followed by the current number
    button = Button(window, text="Button" + str(label_num))
    # Use the grid geometry manager to place the button
    # The button's row is determined by integer division of label_num by 3
    # The button's column is determined by the remainder of label_num divided by 3
    button.grid(row=label_num // 3, column=label_num % 3)

# Start the main event loop, waiting for user interaction
window.mainloop()
