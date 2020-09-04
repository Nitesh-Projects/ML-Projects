#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[4]:


import matplotlib.pyplot


# In[5]:


data = pd.read_csv('C:/python/Covid_Latest/allcovid19India.csv')


# In[6]:


data.shape


# In[7]:


data.info()


# In[8]:


data.head()


# In[9]:


data = data.iloc[:,1:]


# In[10]:


data


# In[14]:


data.isnull().sum(axis=0)


# In[15]:


data.isnull().sum(axis=0).sort_values()


# In[19]:


#percentage of data missing in each column

data.isnull().sum(axis=0).sort_values()/len(data)*100

#rounding to 2 decimal place
# In[21]:


round(data.isnull().sum(axis=0).sort_values()/len(data)*100,2)


# In[22]:


data.groupby('Month')['Num Cases'].sum()


# In[23]:


#This has all the data of hospitalizes and recovered 


# In[27]:


data['Current Status'].values


# In[28]:


data[data['Current Status']=='Hospitalized']


# In[30]:


M= data[data['Current Status']=='Hospitalized'].groupby('Month')['Num Cases'].sum()


# In[31]:


M


# In[32]:


M.plot.bar()


# In[35]:


data.groupby('Gender')['Num Cases'].sum()


# In[36]:


data.groupby('Age Bracket')['Num Cases'].sum()


# In[38]:


data.groupby('Age Bracket')['Num Cases'].sum().sort_values(ascending = False).head(10)


# In[39]:


p =data.groupby('Age Bracket')['Num Cases'].sum().sort_values(ascending = False).head(10)


# In[40]:


p.plot.bar()


# In[41]:


#statewise cases


# In[42]:


data.groupby('Detected State')['Num Cases'].sum().sort_values(ascending = False)


# In[46]:


s = data.groupby('Detected State')['Num Cases'].sum().sort_values(ascending = False)
s.plot.bar()


# In[61]:


data[data['Current Status']=='Hospitalized'].groupby('Detected State')['Num Cases'].sum().sort_values(ascending =False).head(10)


# In[62]:


d =data[data['Current Status']=='Hospitalized'].groupby('Detected State')['Num Cases'].sum().sort_values(ascending =False)


# In[63]:


d


# In[64]:


d.plot.bar(figsize=(15,5))
plt.show()


# In[65]:


data.head()


# In[69]:


data[data['Current Status'] == 'Hospitalized'].groupby(['Month','Day'])[['Num Cases']].sum()


# In[ ]:




