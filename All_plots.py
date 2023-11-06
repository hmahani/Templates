import os
import pandas as pd
import matplotlib.pyplot as plt

input_dir = 'Templates/CSV/'
csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

markers = ['o', '^', 's', 'v', '1', '2', '8', 'p', 'H', 'x', 'd', '+']
x_columns = ['[3.6]', '[4.5]', '[5.8]', '[24]']

output_dir = 'ALL_Plots'
os.makedirs(output_dir, exist_ok=True)  # Create the output directory if it doesn't exist

for file_name in csv_files:
    plt.figure()
    file_path = os.path.join(input_dir, file_name)
    df = pd.read_csv(file_path, delimiter='\t')

    col_8_0 = df['[8.0]']
    
    legend_label = file_name.split('_')[0].strip()
    
    for i, x_column in enumerate(x_columns):
        col_x = df[x_column] - col_8_0
        
        plt.scatter(col_x, col_8_0, label=f'{legend_label} ({x_column} - [8.0])', marker=markers[i])

        plt.xlim(-1, 6)
        plt.ylim(19, 4)

        plt.ylabel('[8.0]')
        plt.xlabel(f'{x_column} - [8.0]')
        plt.legend(fontsize='small', ncol=4)

        output_file = os.path.join(output_dir, f'{legend_label}_{x_column}_plot.png')
        plt.savefig(output_file)
        plt.close()

        print(f'Plot saved as {output_file}')
