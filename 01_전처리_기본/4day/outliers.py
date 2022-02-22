#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
def outerLIne_iqr(df_data, data):
    q1,q3 = np.percentile(df_data[data],[25,75])
    iqr = q3 - q1
    lower_bound = q1 - (1.5*iqr)
    lower_bound
    
    upper_bound = q3 + (1.5*iqr)
    upper_bound
    
    print('최대',upper_bound, '최소', lower_bound)
    return df_data[(df_data[data] < lower_bound) | (df_data[data] > upper_bound)]

