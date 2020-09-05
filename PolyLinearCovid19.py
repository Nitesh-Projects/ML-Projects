#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


data = pd.read_csv('C:/python/Covid_Latest/allcovid19India.csv')


# In[5]:


data.info()


# In[9]:


data.shape


# In[10]:


data.head()


# In[12]:


data = data.iloc[:,1:]


# In[13]:


data


# In[18]:


day = data[data['Current Status'] == 'Hospitalized'].groupby(['Month','Day'])[['Num Cases']].sum()


# In[19]:


day


# In[23]:


x = np.arange(len(day))
x


# In[21]:


y = day.values


# In[22]:


y


# In[24]:


from sklearn.preprocessing import PolynomialFeatures


# In[29]:


poly = PolynomialFeatures(degree=2)


# In[32]:


X = poly.fit_transform(x.reshape(-1,1))


# In[33]:


X


# In[34]:


pd.DataFrame(X)


# In[35]:


pd.DataFrame(y)


# In[ ]:





# In[ ]:





# In[38]:


from sklearn.linear_model import LinearRegression


# In[40]:


reg = LinearRegression()


# In[41]:


reg.fit(X,y)


# In[42]:


reg.coef_


# In[43]:


reg.intercept_


# In[45]:


Yp = reg.predict(X)
Yp


# In[46]:


plt.scatter(x,y)
plt.plot(x,Yp,'K')
plt.show()


# In[47]:


reg.score(X,y)


# In[52]:


poly.transform([[200]])


# In[70]:


reg.predict(poly.transform([[184]]))


# In[51]:


# Making degre 5


# In[54]:


poly5 = PolynomialFeatures(degree=5)


# In[55]:


X = poly5.fit_transform(x.reshape(-1,1))


# In[56]:


X


# In[61]:


reg5 = LinearRegression()


# In[62]:


reg5.fit(X,y)


# In[63]:


Yp5 = reg5.predict(X)
Yp5


# In[64]:


plt.scatter(x,y)
plt.plot(x,Yp5,'K')
plt.show()


# In[67]:


reg5.score(X,y)*100


# In[69]:


reg5.predict(poly5.transform([[184]]))


# In[ ]:




