#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
arr = np.array([[-1,2,0,4],[4,-0.5,6,0],[2.6,0,7,8],[3,-7,4,2.0]])
print("Original array:\n",arr)


# In[2]:


print("\nEvery other rows:\n",arr[0:3:2])


# In[5]:


arr1=np.array([1,2,3,4,5,6,7])
print("\nOriginal array:",arr1)
print("\nReturns every other elements in the array:arr[::2]:",arr1[::2])


# In[8]:


import numpy as np
arr = np.array([[-1,2,0,4],[4,-0.5,6,0],[2.6,0,7,8],[3,-7,4,2.0]])
temp=arr[:2,:3]
print("\nArray with first 2 rows and 3 columns:\n",temp)


# In[ ]:




