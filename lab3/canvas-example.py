from tkinter import *

from tkinter.ttk import *

# Create main window
master = Tk()

# Create canvas. Creates inside the main window.
c = Canvas(master, width=200, height=200)

# Display canvas to window.
c.pack()

# Draw straight line from top left (0,0) to (200, 100) near bottom right
c.create_line(0, 0, 200, 100)

# Draw straight line.
c.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

# Create rectangle
c.create_rectangle(50, 25, 150, 75, fill="blue")

# Start GUI event loop
master.mainloop()