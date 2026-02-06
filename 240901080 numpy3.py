#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
arr=np.array([1,2,3,4,5,4,4])
print("Original array:",arr)
x=np.where(arr==4)
print("\nIndexes where the value is 4:\n",x)


# In[2]:


arr=np.array([1,2,3,4,5,6,7,8])
x=np.where(arr%2==0)
print("\nOriginal array:",arr)
print("\nIndexes where the values are even:",x)


# In[3]:


x=np.searchsorted(arr,3,side='left')
print("\nindexes where the value 3 should be inserted,starting from the right:",x)


# In[4]:


arr=np.array([3,2,0,1])
print("\nOriginal array:",arr)
print("\nSorted array:",np.sort(arr))
arr=np.array([[3,2,4],[5,0,1]])
print("\nOriginal array:",arr)
print("\nSorted array:",np.sort(arr))


# In[6]:


arr=np.array([41,42,43,44])
x=[True,False,True,False]
newarr=arr[x]
print("\nOriginal array:",arr)
print("\nFilter index:",x)
print("\nFilter array:",newarr)


# In[10]:


arr=np.array([41,42,43,44])
filter_arr = arr > 42
newarr=arr[filter_arr]
print("\nOriginal array:",arr)
print("\nFilter array:condition->42:",filter_arr)
print("\nNew array:",newarr)


# In[ ]:




