import tkinter as tk
import random
import time
import csv


class FittsLawExperiment:
    def __init__(self, master, distances, widths, repetitions, participant_name):
        self.master = master
        self.canvas = tk.Canvas(master, width=800, height=600)
        self.canvas.pack()

        self.distances = distances
        self.widths = widths
        self.repetitions = repetitions
        self.participant_name = participant_name

        self.target1 = None
        self.target2 = None

        self.current_width = None
        self.current_distance = None

        # Create a list of all compilations of distances and widths
        self.combinations = [(d, w) for d in distances for w in widths]
        # randomize the order of experiments
        random.shuffle(self.combinations)

        self.current_combination_index = 0
        self.current_repetition = 0
        self.start_time = None

        # Open CSV file to log results
        self.log_file = open(f'{participant_name}_fitts_law_log.csv', 'w', newline='')
        self.log_writer = csv.writer(self.log_file)
        # Write header row to csv
        self.log_writer.writerow(['Name', 'Distance', 'Width', 'Selection Number', 'Time'])

        # Create the green and blue targets
        self.create_targets()
        # Make the green target change the experiment
        self.canvas.bind('<Button-1>', self.on_click)

    def create_targets(self):
        # Check if all combinations have been tested
        # If they have end experiment
        if self.current_combination_index >= len(self.combinations):
            self.log_file.close()
            print("Experiment completed")
            self.master.quit()
            return

        # Delete existing targets if exist
        if self.target1:
            self.canvas.delete(self.target1)
            self.canvas.delete(self.target2)

        # Get width and distance for this experiment
        self.current_distance, self.current_width = self.combinations[self.current_combination_index]

        # Calc margin to center the targets
        margin = (800 - (self.current_distance + self.current_width)) // 2

        # Create the green target
        self.target1 = self.canvas.create_rectangle(
            margin, 0, margin + self.current_width, 600, fill='green', tags='target'
        )

        # Create the blue target
        self.target2 = self.canvas.create_rectangle(
            margin + self.current_distance + self.current_width, 0,
            margin + 2 * self.current_width + self.current_distance, 600, fill='blue', tags='target'
        )

    def on_click(self, event):
        # Check if click is in the green target
        if not self.is_within_green_target(event.x, event.y):
            return

        # Record the start time if its the first click
        if self.start_time is None:
            self.start_time = time.time()
            return

        # Calculate and round the time since the last click.
        elapsed_time = time.time() - self.start_time
        self.start_time = time.time()
        rounded_time = round(elapsed_time, 3)

        # Record results
        self.log_writer.writerow([
            self.participant_name,
            self.current_distance,
            self.current_width,
            self.current_repetition + 1,
            rounded_time
        ])

        self.current_repetition += 1

        # Check if repetitions for current width, distance experiment are completed
        if self.current_repetition >= self.repetitions:
            # Create new set of targets
            self.current_repetition = 0
            self.current_combination_index += 1
            self.create_targets()
        else:
            # Change the colors for the next repetition
            self.swap_colors()

    def is_within_green_target(self, x, y):
        target_color = self.canvas.itemcget(self.target1, 'fill')
        target_coords = self.canvas.coords(self.target1) if target_color == 'green' else self.canvas.coords(
            self.target2)
        x1, y1, x2, y2 = target_coords
        return x1 <= x <= x2 and y1 <= y <= y2

    def swap_colors(self):
        current_color = self.canvas.itemcget(self.target1, 'fill')
        new_color = 'blue' if current_color == 'green' else 'green'
        self.canvas.itemconfigure(self.target1, fill=new_color)
        self.canvas.itemconfigure(self.target2, fill='green' if new_color == 'blue' else 'blue')


if __name__ == '__main__':
    # Number of distances between the two bars to do with each bar width
    distances = [64, 128, 256, 512]
    # Number of different widths of the bars to do
    widths = [8, 16, 32]
    # Number of times click between bars
    repetitions = 2
    participant_name = 'Participant1'  # Change as needed

    root = tk.Tk()
    experiment = FittsLawExperiment(root, distances, widths, repetitions, participant_name)
    root.mainloop()
