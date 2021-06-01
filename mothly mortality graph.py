#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries for analysis and data viz
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

get_ipython().run_line_magic('matplotlib', 'inline')

#read in file, change directory to flavor
xlsx = pd.ExcelFile('X:\\FlHealthCharts\\frequency and count of r99 deaths by county and year.xlsx')
#all goodies are on one sheet
df = pd.read_excel(xlsx, 'analysis')


# In[2]:


#pulling X axis index of county names
counties = df.loc[:,'County Name']

#pulling Y_1 axis column of (average monthly garbage deaths)/average(total deaths 1999-2019) from CDC wonder, 358-cause R95-R99,R00-R53,R55-R94
propMonthMort_1999_2019 = df.loc[0:67,'1999-2019 average proportionate monthly mortality']

#pulling Y_2 column of (average monthly garbage deaths)/(total deaths 2020 provisional) for 358-cause R95-R99,R00-R53,R55-R94 source: FDOH into a new dataframe 
propMonthMort_2020 = df.loc[0:67, '2020 average proportionate monthly mortality (through June, provisional)']


# In[3]:


#adds grid behind plot
plt.style.use('ggplot')

#sets plot size to something readable
plt.figure(figsize=(20,10))

#sets axis labels and title, creates list of x labels for easy reading
x_pos = [i for i, _ in enumerate(counties)]

plt.xlabel("County")
plt.ylabel("Average proportion of deaths coded with garbage codes")
plt.title("Proportionate monthly mortality garbage code deaths by county, 1999-2019 and 2020 (provisional)")

#sets tick marks
plt.xticks(x_pos, counties,rotation='vertical')

#plots as bar chart with error bars
plt.bar(x_pos, propMonthMort_2020, color='yellow',width = 0.5, label = "2020 (provisional) Proportionate monthly mortality garbage code deaths",edgecolor='black')
plt.bar(x_pos, propMonthMort_1999_2019, color='green',width = 0.5, label = "1999-2019 Proportionate monthly mortality garbage code deaths",edgecolor='black')

#creates legend for data
plt.legend(loc='best')

#saves graph
plt.savefig('X:\\FlHealthCharts\\Proportionate monthly mortality garbage code deaths 1999_2020.png')
#shows plot
plt.show()


# In[ ]:




