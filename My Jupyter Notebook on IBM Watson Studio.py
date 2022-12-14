#!/usr/bin/env python
# coding: utf-8

# # My Jupyter Notebook on IBM Watson Studio

# **Kade MacDougall**
# 
# Geologist

# *I am interested in data scinece because it allows more efficient manipulation and use of data for decision making in the geologic fields.*

# ### The following code generates a random sample list

# In[1]:


import random
import csv

random_sample_list = range(int(1),1+int(10))

quantity = 1 + (max(random_sample_list) - min(random_sample_list))

print(quantity, "Total Random Values Were Generated.")
print(random.sample(random_sample_list, quantity))

with open('random_sampleID.csv', 'w') as f:
        csv.writer(f).writerow(random_sample_list)


#   * 1
#   * 2
#   * 3
#   * 4
#   * 5
#   * 6
#   * 7
#   * 8
#   * 9
#   * 10
# 
# 
# ***
# First | Last | Ocupation
# --- | --- | ---
# *Kade* | `MacDougall` | **Geologist**
# *John* | 'Doe' | **Data Scientist**
# 
# 
# ***
# <https://github.com/sanjuangeo/IBM-Data-Science-Projects.git>
