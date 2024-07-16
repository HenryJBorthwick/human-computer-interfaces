from tkinter import *
from tkinter.ttk import *

# Function to append character to the label
def append(char):
    current_text = label_var.get()
    label_var.set(current_text + char)

# Function to clear the label
def clear_text():
    label_var.set("")

# Create the main window (root window) for the GUI application
window = Tk()
window.title("Keyboard GUI")

# Define the content of the keyboard
board = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

# Create a StringVar to hold the text for the label
label_var = StringVar()
label_var.set("")

# Create a Label widget to display the text
label = Label(window, textvariable=label_var, font=('Arial', 14))
label.pack(anchor="w", padx=5, pady=5)

# Create a Button widget to clear the text
clear_button = Button(window, text="Clear", command=clear_text)
clear_button.pack(anchor="e", padx=5, pady=5)

# Create the keyboard buttons inside a frame
frame = Frame(window, borderwidth=4, relief=RIDGE)
frame.pack(padx=5, pady=5)

# Center-aligning the content in the frame using .pack()
def center_align_buttons(board, frame):
    for row in board:
        row_frame = Frame(frame)
        row_frame.pack(fill='x')
        row_frame.pack_propagate(False)  # Prevent the frame from resizing to fit its content
        # Center the row frame
        row_frame.grid_columnconfigure(0, weight=1)
        for ch in row:
            button = Button(row_frame, text=ch, command=lambda x=ch: append(x), width=3)
            button.pack(side=LEFT, padx=1, pady=1)
        row_frame.grid_columnconfigure(len(row) + 1, weight=1)

center_align_buttons(board, frame)

window.mainloop()
