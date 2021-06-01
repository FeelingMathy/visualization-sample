#!/usr/bin/env python
# coding: utf-8

# In[1]:


#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import pingouin as pg

#import data, change the 'C:/Users/bague/Downloads/svi vs cases.csv' to whatever directory and file you like
df = pd.read_csv('C:/Users/bague/Downloads/cases vs hosp vs deaths.csv', header=0, dtype = float)

#does correlation matrix for plots using Spearman Rho to account for squirrley data
corrMatrix = df.corr(method='spearman').round(2)

#lotsa variables calls for bigger fonts
sn.set(font_scale = 2)

#plots ginormous ugly heatmap. play with figsize=(x,y) to change page size as needed
plt.figure(figsize=(45, 25))
mask = np.zeros_like(corrMatrix)
mask[np.triu_indices_from(mask)] = True
hmap = sn.heatmap(corrMatrix, cmap = 'Blues', mask = mask, square = True, vmin=-1, vmax=1, annot=True, annot_kws={"size":12})
#fontsize can be adjusted to not be giant
hmap.axes.set_title("Correlation between COVID19 outcomes by race and ethnicity", fontsize = 18)
#labelsize can be adjusted to not be giant
hmap.tick_params(labelsize = 10)

#saves plot output, change'C:/Users/bague/Downloads/cases_correlation.png' to whatever your directory should be and the new filename
plt.savefig('C:/Users/bague/Downloads/outcomes_correlation.png')


#runs matrix using Pingouin library allowing for significance flagging
dfOutput = df.rcorr(stars=True, method = 'spearman')

#saves significance flag output to digital format, correlations on bottom half, significance at top using pingouin. change file directory/name to your choice
dfOutput.to_csv('C:/Users/bague/Downloads/outcomes STARS.csv')

#runs matrix using Pingouin library allowing for pVal display
dfOutput = df.rcorr(stars=False, method = 'spearman')

#saves significance pVal output to digital format, correlations on bottom half, significance at top using pingouin. change file directory/name to your choice
dfOutput.to_csv('C:/Users/bague/Downloads/outcomes pVal.csv')


# In[ ]:




