import csv
import glob

# Get the path to the folder containing the CSV files
folder_path = "abc"

# Get a list of all the CSV files in the folder
csv_files = glob.glob(folder_path + "/*.csv")

# Iterate over the list of CSV files
for csv_file in csv_files:

    # Open the CSV file
    with open(csv_file, "r", encoding="utf-8") as csvfile:

        # Create a CSV reader object
        reader = csv.reader(csvfile, delimiter=",")

        # Create a list to store the new rows
        new_rows = []

        # Iterate over the rows in the CSV file
        for row in reader:

            # Create a new row by dropping the last two columns
            new_row = row[:-2]

            # Add the new row to the list of new rows
            new_rows.append(new_row)

    # Open the CSV file in write mode
    with open(csv_file, "w", encoding="utf-8", newline="") as csvfile:

        # Create a CSV writer object
        writer = csv.writer(csvfile, delimiter=",")

        # Write the new rows to the CSV file
        writer.writerows(new_rows)
