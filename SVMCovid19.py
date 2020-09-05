#!/usr/bin/env python
# coding: utf-8

# In[78]:


import numpy as np


# In[79]:


import pandas as pd


# In[80]:


import matplotlib.pyplot as plt


# In[81]:


data = pd.read_csv("C:/python/Covid_Latest/allcovid19India.csv")


# In[82]:


data


# In[83]:


data.info()


# In[84]:


data


# In[85]:


data = data.iloc[:,1:]


# In[86]:


data


# In[87]:


data[data['Current Status']=='Hospitalised']


# In[88]:


data['Current Status']=='Hospitalised'


# In[89]:


data[data['Current Status']== 'Hospitalized']


# In[90]:


data['Current Status'].unique()


# In[91]:


M= data[data['Current Status']== 'Hospitalized'].groupby(['Month', 'Day'])[['Num Cases']].sum()


# In[92]:


M


# In[93]:



x= len(M)


# In[94]:


x


# In[95]:


x = np.arange(len(M))


# In[96]:


x


# In[97]:


x= x.reshape(-1,1)


# In[98]:


x


# In[99]:


y = M.values


# In[100]:


y 


# In[101]:


y= y.reshape(-1,1)


# In[102]:


y


# In[103]:


from sklearn.preprocessing import StandardScaler


# In[104]:


sc_x=StandardScaler()
sc_y=StandardScaler()


# In[105]:


sx = sc_x.fit_transform(x)


# In[106]:


sy = sc_y.fit_transform(y)


# In[107]:


sx


# In[108]:


sy


# In[111]:


from sklearn.svm import SVR


# In[112]:


reg = SVR(kernel ='rbf')


# In[115]:


reg.fit(sx,sy.ravel())


# In[116]:


reg.score(sx,sy)*100


# In[ ]:





# In[ ]:





# In[117]:


plt.scatter(x,y)


# In[118]:


plt.scatter(sx,sy)


# In[122]:


plt.scatter(sx,sy)
plt.plot(sx,reg.predict(sx),'k',linewidth=5)


# In[123]:


reg.score(sx,sy)*100


# In[ ]:




