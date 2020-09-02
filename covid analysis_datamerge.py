#!/usr/bin/env python
# coding: utf-8

# In[49]:


import pandas as pd


# In[50]:


import numpy as np


# In[51]:


df1 = pd.read_csv('C://python/covid study/raw_data1.csv')


# In[52]:


df1.head(5)


# In[53]:


df1 = pd.read_csv('C://python/covid study/raw_data1.csv')
df2 = pd.read_csv('C://python/covid study/raw_data2.csv')
df3 = pd.read_csv('C://python/covid study/raw_data3.csv')
df4 = pd.read_csv('C://python/covid study/raw_data4.csv')
df5 = pd.read_csv('C://python/covid study/raw_data5.csv')
df6 = pd.read_csv('C://python/covid study/raw_data6.csv')
df7 = pd.read_csv('C://python/covid study/raw_data7.csv')
df8 = pd.read_csv('C://python/covid study/raw_data8.csv')
df9 = pd.read_csv('C://python/covid study/raw_data9.csv')
df10 = pd.read_csv('C://python/covid study/raw_data10.csv')
df11 = pd.read_csv('C://python/covid study/raw_data11.csv')


# In[54]:


df2.shape


# In[55]:


df1.info()


# In[56]:


df1.columns


# In[57]:


df3.columns


# In[58]:


df1 =df1.rename(columns={"Num cases":"Num Cases"})
df2 =df2.rename(columns={"Num cases":"Num Cases"})


# In[59]:


df1.columns


# df1

# In[60]:


df1 = df1.loc[:,['Num Cases','Date Announced','Estimated Onset Date', 'Age Bracket', 'Gender', 'Detected City','Detected District', 'Detected State', 'Current Status']]


# In[61]:


df1


# In[62]:


df2.loc[:,['Num Cases','Date Announced','Estimated Onset Date', 'Age Bracket', 'Gender', 'Detected City','Detected District', 'Detected State', 'Current Status']]


# In[63]:


df2 = df2.loc[:,['Num Cases','Date Announced','Estimated Onset Date', 'Age Bracket', 'Gender', 'Detected City','Detected District', 'Detected State', 'Current Status']]
df3 = df3.loc[:,['Num Cases','Date Announced','Estimated Onset Date', 'Age Bracket', 'Gender', 'Detected City','Detected District', 'Detected State', 'Current Status']]
df4 = df4.loc[:,['Num Cases','Date Announced','Estimated Onset Date', 'Age Bracket', 'Gender', 'Detected City','Detected District', 'Detected State', 'Current Status']]
df5 = df5.loc[:,['Num Cases','Date Announced','Estimated Onset Date', 'Age Bracket', 'Gender', 'Detected City','Detected District', 'Detected State', 'Current Status']]
df6 = df6.loc[:,['Num Cases','Date Announced','Estimated Onset Date', 'Age Bracket', 'Gender', 'Detected City','Detected District', 'Detected State', 'Current Status']]
df7 = df7.loc[:,['Num Cases','Date Announced','Estimated Onset Date', 'Age Bracket', 'Gender', 'Detected City','Detected District', 'Detected State', 'Current Status']]
df8 = df8.loc[:,['Num Cases','Date Announced','Estimated Onset Date', 'Age Bracket', 'Gender', 'Detected City','Detected District', 'Detected State', 'Current Status']]
df9 = df9.loc[:,['Num Cases','Date Announced','Estimated Onset Date', 'Age Bracket', 'Gender', 'Detected City','Detected District', 'Detected State', 'Current Status']]
df10 = df10.loc[:,['Num Cases','Date Announced','Estimated Onset Date', 'Age Bracket', 'Gender', 'Detected City','Detected District', 'Detected State', 'Current Status']]
df11 = df11.loc[:,['Num Cases','Date Announced','Estimated Onset Date', 'Age Bracket', 'Gender', 'Detected City','Detected District', 'Detected State', 'Current Status']]


# In[64]:


df = df1.append([df2,df3,df4,df5,df6,df7,df8,df9,df10,df11])


# In[65]:


df


# In[66]:


df = df.loc[: ,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City','Detected District', 'Detected State', 'Current Status']]


# In[67]:


df


# In[68]:


DATE =df['Date Announced'].str.split('/', expand =True)


# In[69]:


DATE.columns = ['Day','Month','Year']


# In[70]:


DATE.columns 


# In[71]:


DATE 


# In[72]:


df =pd.concat([df,DATE],axis =1)


# In[73]:


df 


# In[102]:


df.to_csv('CovidAnalysis.csv')


# In[101]:


df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




