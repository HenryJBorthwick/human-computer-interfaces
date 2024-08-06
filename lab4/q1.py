import csv
import math
from collections import defaultdict

# Path to your CSV log file
log_file_path = '../lab3/Participant1_fitts_law_log.csv'
summary_file_path = 'summary.csv'

# Dictionary to store data, grouped by (amplitude, width)
data = defaultdict(list)

# Read the CSV log file
with open(log_file_path, 'r') as log_file:
    reader = csv.reader(log_file)
    next(reader)  # Skip the header if there is one
    for row in reader:
        # Assuming the CSV format is: participant, amplitude, width, selection_number, time
        amplitude = int(row[1])
        width = int(row[2])
        selection_number = int(row[3])
        time = float(row[4])  # Times are already in seconds

        key = (amplitude, width)
        data[key].append(time)

# Dictionary to store the average times grouped by ID
id_data = defaultdict(list)

# Calculate mean time for each ID, ignoring the first two selections
for (amplitude, width), times in data.items():
    # Sort times based on the selection number
    times = sorted(times)
    # Ignore the first two selections
    valid_times = times[2:]
    if valid_times:
        mean_time = sum(valid_times) / len(valid_times)
        ID = math.log2(amplitude / width + 1)
        id_data[ID].append(mean_time)

# Calculate overall mean time for each ID and write to summary file
with open(summary_file_path, 'w', newline='') as csvfile:
    fieldnames = ['ID', 'mean_time']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for ID, times in id_data.items():
        overall_mean_time = sum(times) / len(times)
        writer.writerow({'ID': round(ID, 3), 'mean_time': round(overall_mean_time, 3)})

print(f"Summary data written to {summary_file_path}")
