#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[4]:


import matplotlib.pyplot as plt


# In[ ]:





# In[5]:


data = pd.read_csv('C://Users/njaiswa2/CovidAnalysis.csv')


# In[89]:


data


# In[90]:


data = data.iloc[:,1:]


# In[91]:


data


# In[92]:


day= data[data['Current Status'] == 'Hospitalized'].groupby(['Month','Day'])[['Num Cases']].sum()


# In[93]:


day


# In[94]:


y=day.values


# In[95]:


y


# In[96]:


len(day)


# In[97]:


x = np.arange(len(day))


# In[98]:


x


# In[99]:


x = x.reshape(-1,1)
x


# In[100]:


from sklearn.preprocessing import PolynomialFeatures


# In[101]:


poly = PolynomialFeatures(degree=2)


# In[102]:


poly


# In[103]:


X = poly.fit_transform(x)


# In[104]:


X


# In[127]:


pd.DataFrame(X)


# In[128]:


from sklearn.linear_model import LinearRegression


# In[129]:


reg = LinearRegression()


# In[130]:


reg.fit(X,y)


# In[131]:


reg.coef_


# In[132]:


reg.intercept_


# In[133]:


plt.scatter(x,y)
plt.show()


# In[134]:


x.shape


# In[135]:


y.shape


# In[136]:


yp =  reg.predict(X)


# In[137]:


yp


# In[139]:



plt.scatter(x,y)
plt.plot(x,yp,color='K')
plt.show()


# In[140]:


reg.score(X,y)*100


# In[ ]:




