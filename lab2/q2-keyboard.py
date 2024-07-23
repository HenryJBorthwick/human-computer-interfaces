from tkinter import *
from tkinter.ttk import *
import random
import time
import csv

# Initialize the log file based on the mode
# mode = 'static'
mode = 'dynamic'

log_filename = f'experiment_{mode}_log.txt'
with open(log_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["User Name", "Condition", "Target Character", "Block Count", "Time Taken (ms)"])

# Function to append character to the label
def append(char):
    current_text = label_var.get()
    label_var.set(current_text + char)

# Function to clear the label
def clear_text():
    label_var.set("")

# Function to start a new block of targets
def start_new_block():
    global current_block, block_count, target_start_time
    if block_count > 0:
        current_block = list(target_letters)
        random.shuffle(current_block)
        block_count -= 1
        next_target()
    else:
        label_var.set("Completed!")
        target_var.set("")
        target_start_time = None

# Function to set the next target letter
def next_target():
    global target_start_time
    if current_block:
        target_var.set(current_block.pop())
        target_start_time = time.time()  # Start timing for the next target
    else:
        start_new_block()

# Function to handle button press
def button_press(char):
    if char == target_var.get():
        # Calculate time taken in milliseconds and round to 1 dp
        time_taken = round((time.time() - target_start_time) * 1000, 1)
        log_selection(char, time_taken)
        append(char)
        next_target()
        # Makes keyboard change after each correct selection
        if mode == 'dynamic':
            randomize_keyboard()

# Function to log the selection
def log_selection(char, time_taken):
    global block_count
    name = "User"  # Replace with the actual user's name
    condition = mode
    with open(log_filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, condition, char, block_count, time_taken])

# Function to randomize the keyboard layout
def randomize_keyboard():
    random.shuffle(keys)
    for widget in frame.winfo_children():
        widget.destroy()
    center_align_buttons(keys, frame)

# Create the main window (root window) for the GUI application
window = Tk()
window.title("Keyboard GUI")

# Define the content of the keyboard
board = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

# Flatten the board to a single list of keys
keys = [char for row in board for char in row]

# Create variables to hold the target letters and blocks
target_letters = 'abcdef'
block_count = 1  # Set a lower number for development, change to 6 for actual use
current_block = []
target_start_time = None

# Create a StringVar to hold the text for the label
label_var = StringVar()
label_var.set("")

# Create a Label widget to display the text
label = Label(window, textvariable=label_var, font=('Arial', 14))
label.grid(row=0, column=0, columnspan=10, sticky="w", padx=5, pady=5)

# Create a Label widget to display the target letter
target_var = StringVar()
target_label = Label(window, textvariable=target_var, font=('Arial', 14), foreground="red")
target_label.grid(row=0, column=10, sticky="e", padx=5, pady=5)

# Create a Button widget to clear the text
clear_button = Button(window, text="Clear", command=clear_text)
clear_button.grid(row=1, column=10, sticky="e", padx=5, pady=5)

# Create the keyboard buttons inside a frame
frame = Frame(window, borderwidth=4, relief=RIDGE)
frame.grid(row=1, column=0, columnspan=10, padx=5, pady=5)

# Center-aligning the content in the frame
def center_align_buttons(keys, frame):
    # Use the shuffelded keys list
    rows = [keys[i:i + 10] for i in range(0, len(keys), 10)]

    for row_index, row in enumerate(rows):
        row_frame = Frame(frame)
        row_frame.grid(row=row_index, column=0, columnspan=11)
        row_frame.grid_columnconfigure(0, weight=1)
        row_frame.grid_columnconfigure(len(row) + 1, weight=1)


        for col_index, ch in enumerate(row):
            # Create a frame for each button to set its size to 64x64 pixels
            button_frame = Frame(row_frame, width=64, height=64)
            # Prevent the frame from shrinking
            button_frame.pack_propagate(0)
            button_frame.grid(row=0, column=col_index + 1, padx=1, pady=1)
            # Place the button inside the frame
            button = Button(button_frame, text=ch, command=lambda x=ch: button_press(x))
            button.pack(fill=BOTH, expand=1)

# Randomize the keyboard layout initially
randomize_keyboard()

# Make sure the window is resizable and the content scales properly
for i in range(11):
    window.grid_columnconfigure(i, weight=1)
for i in range(2):
    window.grid_rowconfigure(i, weight=1)

# Start the first block
start_new_block()

window.mainloop()
