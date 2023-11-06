import os
import csv
import pandas as pd
from astropy import units as u
from astropy.coordinates import SkyCoord



#folder_path = os.getcwd()  # Specify the path to the subfolder
folder_path = 'Templates/'

#                                                                                Delete '#'               

file_list = [f for f in os.listdir(folder_path) if f.endswith('.tmpl')]

for file_name in file_list:
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # Delete '#'
    modified_lines = [line.replace('#', '') for line in lines]
    # Write the modified lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(modified_lines)

#                                                                                Convert to Tab-separated CSV

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

            # Write the header row with a modified number of columns
            header_row = next(reader)
            num_columns = min(len(header_row), 34)  # Restrict number of columns to 34 or less
            header_row = header_row[:num_columns]  # Limit the header row to the restricted number of columns
            writer.writerow(header_row)

            # Write the data rows with a modified number of columns
            for row in reader:
                row = row[:num_columns]  # Limit each data row to the restricted number of columns
                filled_row = [value if value else 'NaN' for value in row]
                writer.writerow(filled_row)
               
#                                                                                Pairs Cross-matching


input_dir = 'Templates/CSV/'
output_dir = 'Cross_Match/'
os.makedirs(output_dir, exist_ok=True)

csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

for i in range(len(csv_files)):
    for j in range(i + 1, len(csv_files)):
        file1 = pd.read_csv(os.path.join(input_dir, csv_files[i]), sep='\t')
        file2 = pd.read_csv(os.path.join(input_dir, csv_files[j]), sep='\t')
#        
        coords1 = SkyCoord(ra=file1['RA'] * u.degree, dec=file1['DEC'] * u.degree)
        coords2 = SkyCoord(ra=file2['RA'] * u.degree, dec=file2['DEC'] * u.degree)
#        
        idx, d2d, d3d = coords1.match_to_catalog_sky(coords2)
        matches = d2d < 1 * u.arcsecond
        matched_file1 = file1[matches]
        matched_file2 = file2.iloc[idx[matches]]
        matched_data = pd.concat([matched_file1.reset_index(drop=True), matched_file2.reset_index(drop=True)],
                                 axis=1)
#
        if not matched_data.empty:
            output_file = os.path.join(output_dir, f'Cross_Match_{csv_files[i]}_{csv_files[j]}.csv')
            matched_data.to_csv(output_file, sep='\t', index=False)
            print(f'Saved non-empty result to: {output_file}')


















