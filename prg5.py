#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
marks=[10,12,14,16,18,20,22,24,26,100]
df=pd.DataFrame({"Marks":marks})
Q1=df["Marks"].quantile(0.25)
Q2=df["Marks"].quantile(0.50)
Q3=df["Marks"].quantile(0.75)
IQR=Q3-Q1
lowest_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR
print("Q1:",Q1)
print("Q2:",Q2)
print("Q3:",Q3)
print("IQR:",IQR)
print("Lowest bound:",lowest_bound)
print("Upper bound:",upper_bound)


# In[ ]:





# In[7]:


import pandas as pd
values=[48,49,50,50,50,51,51,51,52,52,52,53,53,53,54,54,55,55,100]
#calculate mean and satndard deviation
mean=sum(values)/len(values)
std=pd.Series(values).std(ddof=0)
print("Mean:",round(mean,2))
print("Standard Deviation:",round(std,2))
#Detect outliers
for x in values:
    z=(x-mean)/std
    if abs(z)>3:
        print("Outlies:",x)
        print("Z-scores:",round(z,2))
        


# In[ ]:





# In[ ]:




