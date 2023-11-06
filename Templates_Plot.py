import os
import pandas as pd
import matplotlib.pyplot as plt

input_dir = 'Templates/CSV/'

csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

plt.figure()

markers = ['o', '^', 's','v', '1', '2','8', 'p', 'H', 'x', 'd', '+']

for i, file_name in enumerate(csv_files):

  file_path = os.path.join(input_dir, file_name)
  df = pd.read_csv(file_path, delimiter='\t')

  col_3_6 = df['[3.6]']  
  col_8_0 = df['[8.0]']   

  legend_label = file_name.split('_')[0].strip()
  print(legend_label,len(file_name))

  plt.scatter(col_3_6 - col_8_0, col_8_0,  
              label=legend_label, 
              marker=markers[i])

plt.xlim(-1,6)
plt.ylim(19,4)  
  
plt.ylabel('[8.0]')
plt.xlabel('[3.6] - [8.0]')
plt.legend(fontsize='small',ncol=4)

plt.savefig('output.png')
plt.show()
