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
label.grid(row=0, column=0, columnspan=10, sticky="w", padx=5, pady=5)

# Create a Button widget to clear the text
clear_button = Button(window, text="Clear", command=clear_text)
clear_button.grid(row=0, column=10, sticky="e", padx=5, pady=5)

# Create the keyboard buttons inside a frame
frame = Frame(window, borderwidth=4, relief=RIDGE)
frame.grid(row=1, column=0, columnspan=11, padx=5, pady=5)

# Center-aligning the content in the frame
def center_align_buttons(board, frame):
    max_len = max(len(row) for row in board)
    for row_index, row in enumerate(board):
        row_frame = Frame(frame)
        row_frame.grid(row=row_index, column=0, columnspan=11)
        row_frame.grid_columnconfigure(0, weight=1)
        row_frame.grid_columnconfigure(max_len + 1, weight=1)

        for col_index, ch in enumerate(row):
            # Create a frame for each button to set its size to 64x64 pixels
            button_frame = Frame(row_frame, width=64, height=64)
            # Prevent the frame from shrinking
            button_frame.pack_propagate(0)
            button_frame.grid(row=0, column=col_index + 1, padx=1, pady=1)
            # Place the button inside the frame
            button = Button(button_frame, text=ch, command=lambda x=ch: append(x))
            button.pack(fill=BOTH, expand=1)

center_align_buttons(board, frame)

# Make sure the window is resizable and the content scales properly
for i in range(11):
    window.grid_columnconfigure(i, weight=1)
for i in range(2):
    window.grid_rowconfigure(i, weight=1)

window.mainloop()
