#!/usr/bin/env python
# coding: utf-8

# Read the dataset from the below link

# In[1]:


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


df=pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')
df.head()


# 1. Delete unnamed columns

# In[3]:


df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1)


# 2.Show the distribution of male and female

# In[9]:


Freq_tab = pd.crosstab(index=df["Gender"],  # Make a crosstab
                              columns="count")      # Name the count column

Freq_tab


# 3. Show the top 5 most preferred names

# In[20]:


df_top_freq =pd.crosstab(index=df["Name"],  # Make a crosstab
                              columns="count")

df_top_sort=df_top_freq.sort_values(by="count",ascending=False)
df_top_sort.head()


# 4.What is the median name occurence in the dataset

# In[ ]:


5. Distribution of male and female born count by states


# In[23]:


pd.crosstab(df.Gender, df.State)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




