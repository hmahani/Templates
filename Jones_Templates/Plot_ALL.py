import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

centimeters = 1/2.54
Tick_Size=6
Axis_Label_Size=8

fig, axs = plt.subplots(1, 1, figsize=(11.0*centimeters, 11.0*centimeters))
fig.suptitle('LMC')

result = pd.read_csv('CAGB_353.csv', sep='\t')
data_C_AGBs = result.replace(r'^\s*$', np.nan, regex=True)
#data_C_AGBs = data_Nan.fillna(99)
col_3_6_C_AGBs = data_C_AGBs['[3.6]']  
col_8_0_C_AGBs = data_C_AGBs['[8.0]']   
plt.scatter(col_3_6_C_AGBs - col_8_0_C_AGBs, col_8_0_C_AGBs,label='C_AGBs_353',  c='orange', marker='^')

col_3_6_C_AGBs2 = data_C_AGBs['[3.6]2']  
col_8_0_C_AGBs2 = data_C_AGBs['[8.0]2']   
plt.scatter(col_3_6_C_AGBs2 - col_8_0_C_AGBs2, col_8_0_C_AGBs2, c='orange', marker='^')


result = pd.read_csv('OAGB_207.csv', sep='\t')
data_brightO_AGBs = result.replace(r'^\s*$', np.nan, regex=True)
#data_brightO_AGBs = data_Nan.fillna(99)
col_3_6_brightO_AGBs = data_brightO_AGBs['[3.6]']  
col_8_0_brightO_AGBs = data_brightO_AGBs['[8.0]']   
plt.scatter(col_3_6_brightO_AGBs - col_8_0_brightO_AGBs, col_8_0_brightO_AGBs,label='O_AGBs_207',  c='r', marker='v')

col_3_6_brightO_AGBs2 = data_brightO_AGBs['[3.6]2']  
col_8_0_brightO_AGBs2 = data_brightO_AGBs['[8.0]2']   
plt.scatter(col_3_6_brightO_AGBs2 - col_8_0_brightO_AGBs2, col_8_0_brightO_AGBs2, c='r', marker='v')


result = pd.read_csv('PAGB_93.csv', sep='\t')
data_post_AGBs = result.replace(r'^\s*$', np.nan, regex=True)
#data_post_AGBs = data_Nan.fillna(99)
col_3_6_post_AGBs = data_post_AGBs['[3.6]']  
col_8_0_post_AGBs = data_post_AGBs['[8.0]']   
plt.scatter(col_3_6_post_AGBs - col_8_0_post_AGBs, col_8_0_post_AGBs,label='post_AGBs_93' ,c='gray', marker='H')

col_3_6_post_AGBs2 = data_post_AGBs['[3.6]2']  
col_8_0_post_AGBs2 = data_post_AGBs['[8.0]2']   
plt.scatter(col_3_6_post_AGBs2 - col_8_0_post_AGBs2, col_8_0_post_AGBs2, c='gray', marker='H')


result = pd.read_csv('RSG_158.csv', sep='\t')
data_RSGs = result.replace(r'^\s*$', np.nan, regex=True)
#data_RSGs = data_Nan.fillna(99)
col_3_6_RSGs = data_RSGs['[3.6]']  
col_8_0_RSGs = data_RSGs['[8.0]']   
plt.scatter(col_3_6_RSGs - col_8_0_RSGs, col_8_0_RSGs,label='RSGs_158',c='darkorchid', marker='1')

col_3_6_RSGs2 = data_RSGs['[3.6]2']  
col_8_0_RSGs2 = data_RSGs['[8.0]2']   
plt.scatter(col_3_6_RSGs2 - col_8_0_RSGs2, col_8_0_RSGs2,c='darkorchid', marker='1')

result = pd.read_csv('YSO_208.csv', sep='\t')
data_YSOs = result.replace(r'^\s*$', np.nan, regex=True)
#data_YSOs = data_Nan.fillna(99)
col_3_6_YSOs = data_YSOs['[3.6]']  
col_8_0_YSOs = data_YSOs['[8.0]']   
plt.scatter(col_3_6_YSOs - col_8_0_YSOs, col_8_0_YSOs,label='YSOs_208', c='g', marker='+')

col_3_6_YSOs2 = data_YSOs['[3.6]2']  
col_8_0_YSOs2 = data_YSOs['[8.0]2']   
plt.scatter(col_3_6_YSOs2 - col_8_0_YSOs2, col_8_0_YSOs2,c='g', marker='+')


result = pd.read_csv('STAR_730.csv', sep='\t')
data_MS = result.replace(r'^\s*$', np.nan, regex=True)
#data_YSOs = data_Nan.fillna(99)
col_3_6_MS = data_MS['[3.6]']  
col_8_0_MS = data_MS['[8.0]']   
plt.scatter(col_3_6_MS - col_8_0_MS, col_8_0_MS,label='MS_730', c='cyan', marker='x')

col_3_6_MS2 = data_MS['[3.6]2']  
col_8_0_MS2 = data_MS['[8.0]2']   
plt.scatter(col_3_6_MS2 - col_8_0_MS2, col_8_0_MS2,c='cyan', marker='x') 


plt.xlim(-1,6)
plt.ylim(19,2)  
  
plt.ylabel('[8.0]')
plt.xlabel('[3.6] - [8.0]')
plt.legend(fontsize='small',ncol=2, loc='lower right')

plt.savefig('All.png')
plt.show()
