#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


import matplotlib.pyplot  as plt


# In[3]:


data = pd.read_csv('C://Users/njaiswa2/CovidAnalysis.csv')


# In[4]:


data


# In[5]:


data = data.iloc[:,1:]


# In[6]:


data


# In[7]:


data.info()


# In[8]:


data.shape


# In[10]:


day = data[data['Current Status']== 'Hospitalized'].groupby(['Month','Day'])[['Num Cases']].sum()
day


# In[14]:


len(day)


# In[19]:


x = np.arange(len(day))


# In[20]:


x


# In[22]:


x = x.reshape(-1,1)


# In[23]:


x


# In[24]:


y = day.values


# In[25]:


y


# In[26]:


plt.scatter(x,y)
plt.show()


# In[28]:


from sklearn.linear_model import LinearRegression


# In[29]:


reg=LinearRegression()


# In[30]:


reg.fit(x,y)


# In[37]:


yp = reg.predict(x)


# In[34]:


yp


# In[44]:


plt.scatter(x,y)
plt.plot(x,yp)
plt.show()


# In[45]:


reg.predict([[160]])


# In[46]:


reg.score(x,y)*100


# In[47]:


reg.intercept_


# In[48]:


reg.coef_


# In[11]:


day.info()


# In[15]:



day.isnull().sum(axis=1).sort_values(ascending=False)


# In[ ]:




