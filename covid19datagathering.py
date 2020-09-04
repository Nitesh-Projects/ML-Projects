#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# import

# In[3]:


import matplotlib.pyplot


# df1 = pd.read('C:/python/Covid_Latest/raw_data1')

# In[74]:



df1 = pd.read_csv('C:/python/Covid_Latest/raw_data1.csv')


# In[75]:


df1.head()


# In[76]:


df2 = pd.read_csv('C:/python/Covid_Latest/raw_data2.csv')
df3 = pd.read_csv('C:/python/Covid_Latest/raw_data3.csv')
df4 = pd.read_csv('C:/python/Covid_Latest/raw_data4.csv')
df5 = pd.read_csv('C:/python/Covid_Latest/raw_data5.csv')
df6 = pd.read_csv('C:/python/Covid_Latest/raw_data6.csv')
df7 = pd.read_csv('C:/python/Covid_Latest/raw_data7.csv')
df8 = pd.read_csv('C:/python/Covid_Latest/raw_data8.csv')
df9 = pd.read_csv('C:/python/Covid_Latest/raw_data9.csv')
df10 = pd.read_csv('C:/python/Covid_Latest/raw_data10.csv')
df11 = pd.read_csv('C:/python/Covid_Latest/raw_data11.csv')
df12 = pd.read_csv('C:/python/Covid_Latest/raw_data12.csv')
df13 = pd.read_csv('C:/python/Covid_Latest/raw_data13.csv')
df14 = pd.read_csv('C:/python/Covid_Latest/raw_data14.csv')


# In[77]:


df1.columns


# 

# In[78]:


df2.columns


# In[79]:


df3.columns


# In[80]:


df4.columns


# In[81]:


df5.columns


# In[82]:


df6.columns


# In[83]:


df1 = df1.rename(columns ={"Patient Number":"Entry_ID"})


# In[84]:


df1.columns


# In[85]:


df2 = df2.rename(columns ={"Patient Number":"Entry_ID"})


# In[86]:


df2.columns


# In[87]:


df1 = df1.loc[:,['Num Cases','Date Announced','Current Status','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State' ]]


# In[88]:


df1.head(50)


# In[89]:


df2 = df2.loc[:,['Num Cases','Date Announced','Current Status','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State' ]]


# In[90]:


df2.head(50)


# In[91]:


df3 = df3.loc[:,['Num Cases','Date Announced','Current Status','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State' ]]
df4 = df4.loc[:,['Num Cases','Date Announced','Current Status','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State' ]]
df5 = df5.loc[:,['Num Cases','Date Announced','Current Status','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State' ]]
df6 = df6.loc[:,['Num Cases','Date Announced','Current Status','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State' ]]
df7 = df7.loc[:,['Num Cases','Date Announced','Current Status','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State' ]]
df8 = df8.loc[:,['Num Cases','Date Announced','Current Status','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State' ]]
df9 = df9.loc[:,['Num Cases','Date Announced','Current Status','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State' ]]
df10 = df10.loc[:,['Num Cases','Date Announced','Current Status','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State' ]]
df11 = df11.loc[:,['Num Cases','Date Announced','Current Status','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State' ]]
df12 = df12.loc[:,['Num Cases','Date Announced','Current Status','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State' ]]
df13 = df13.loc[:,['Num Cases','Date Announced','Current Status','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State' ]]
df14 = df14.loc[:,['Num Cases','Date Announced','Current Status','Age Bracket', 'Gender', 'Detected City',
       'Detected District', 'Detected State' ]]


# In[94]:


df = df1.append([df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14])


# In[95]:


df.shape


# In[96]:


df.head()


# In[97]:


df['Date Announced'].str.split('/',expand=True)


# In[98]:


date = df['Date Announced'].str.split('/',expand=True)


# In[99]:


date.columns = ['Day','Month','Year']


# In[100]:


date


# In[101]:


df.head()


# In[102]:


df = pd.concat([df,date],axis  =1)


# In[103]:


df.head()


# In[104]:


df.to_csv('allcovid19India.csv')


# In[ ]:




