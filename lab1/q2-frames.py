# Import everything from the tkinter module
from tkinter import *

# Import everything from the ttk module, which provides themed widgets
from tkinter.ttk import *

# Create the main window (root window) for the GUI application
window = Tk()

# Create a Frame widget with a border and a raised ridge
frame_left = Frame(window, borderwidth=4, relief=RIDGE)
# Use the pack geometry manager to place the frame on the left side of the window
# The frame will fill the vertical space (y-axis), and have padding of 5 pixels on all sides
frame_left.pack(side="left", fill="y", padx=5, pady=5)

# Create another Frame widget without any border
frame_right = Frame(window)
# Use the pack geometry manager to place the frame on the right side of the window
frame_right.pack(side="right")

# Create a Button widget inside the left frame, with text "Button 1"
button1 = Button(frame_left, text="Button 1")
# Use the pack geometry manager to place the button at the top of the left frame
button1.pack(side="top")

# Create another Button widget inside the left frame, with text "Button 2"
button2 = Button(frame_left, text="Button 2")
# Use the pack geometry manager to place the button at the bottom of the left frame
button2.pack(side="bottom")

# Loop through numbers 0 to 3
for label_num in range(4):
    # Create a Button widget with text "Button" followed by the current number + 3
    button = Button(frame_right, text="Button" + str(label_num + 3))
    # Use the grid geometry manager to place the button in a grid
    # The button's row is determined by integer division of label_num by 2
    # The button's column is determined by the remainder of label_num divided by 2
    button.grid(row=label_num // 2, column=label_num % 2)

# Start the main event loop, waiting for user interaction
window.mainloop()
