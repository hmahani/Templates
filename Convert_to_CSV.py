import os
import csv

folder_path = 'Templates/' 

# Create the 'CSV' folder 
csv_folder = os.path.join(folder_path, 'CSV')
if not os.path.exists(csv_folder):
    os.makedirs(csv_folder)

for filename in os.listdir(folder_path):
    if filename.endswith('.tmpl'):
        file_path = os.path.join(folder_path, filename)
        csv_file = os.path.join(csv_folder, f'{os.path.splitext(filename)[0]}.csv')

        with open(file_path, 'r') as tmpl_file, open(csv_file, 'w', newline='') as csv_file:
            reader = csv.reader(tmpl_file, delimiter=' ', skipinitialspace=True)
            writer = csv.writer(csv_file, delimiter='\t')
            header_row = next(reader)
            header_row = header_row[1:]                                         # Remove the '#' character and shift the header row one cell to the left
            header_row = [column.replace('#', '') for column in header_row]
            writer.writerow(header_row)                                         # Write the modified header row
            writer.writerows(reader)

