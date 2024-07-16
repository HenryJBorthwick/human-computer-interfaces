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
    # The button's row is determined by integer division of label_num by 2
    # The button's column is determined by the remainder of label_num divided by 3
    button.grid(row=label_num // 2, column=label_num % 3)

    # Special configuration for button 1
    if label_num == 1:
        button.grid(columnspan=2, sticky="ew")  # span 2 columns, expand horizontally
    # Special configuration for button 3
    elif label_num == 3:
        button.grid(rowspan=2, sticky="ns")  # span 2 rows, expand vertically

# Configure column 1 to expand as the window is resized
window.columnconfigure(1, weight=1)
# Configure rows 1 and 2 to expand as the window is resized
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)

# Start the main event loop, waiting for user interaction
window.mainloop()
