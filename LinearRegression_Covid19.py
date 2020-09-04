#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[22]:


import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


data =  pd.read_csv('C:/python/Covid_Latest/allcovid19India.csv')


# In[4]:


data.info()


# In[5]:


data.shape


# In[6]:


data.head()


# In[8]:


data = data.iloc[:,1:]
data


# In[12]:


day =data[data['Current Status']=='Hospitalized'].groupby(['Month','Day'])[['Num Cases']].sum()


# In[13]:


day


# In[14]:


len(day)


# In[15]:


x = np.arange(len(day))
x


# In[17]:


day


# In[18]:


day.values


# In[19]:


y = day.values


# In[23]:


plt.scatter(x,y)
plt.show


# In[24]:


#Model Traning


# In[26]:


x = x.reshape(-1,1)


# In[27]:


x


# In[28]:


from sklearn.linear_model import LinearRegression


# In[29]:


reg = LinearRegression()


# In[30]:


reg.fit(x,y)


# In[31]:


y[182]


# In[33]:


reg.predict([[200]])


# In[34]:


Ypred = reg.predict(x)


# In[35]:


Ypred


# In[37]:


plt.scatter(x,y)
plt.plot(x,Ypred)
plt.show()


# In[ ]:





# In[39]:


reg.predict([[250]])


# In[40]:


reg.predict([[300]])


# In[41]:


#Accuracy


# In[42]:


reg.score(x,y)*100


# In[43]:


reg.intercept_
#w0 value in w0 +w1x1


# In[44]:


reg.coef_
#slope w1 value in w0 +w1x1


# In[ ]:




