#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.decomposition import PCA
data={
    'Study_Hours':[2,4,6,8,10],
    'Attendance':[50,60,70,80,90],
    'Mraks':[40,50,60,70,80]
}
df=pd.DataFrame(data)
print("1.Original Data:")
print(df)

normalizer=MinMaxScaler()
normalized_data=normalizer.fit_transform(df)
normalized_df=pd.DataFrame(
normalized_data,
columns=df.columns
)
print("\n2.Normalized Data:")
print(normalized_df.round(2))

standardizer=StandardScaler()
standardized_data=standardizer.fit_transform(df)
standardized_df=pd.DataFrame(
standardized_data,
columns=df.columns)
print("\n3.Standardized data:")
print(standardized_df.round(2))

pca=PCA(n_components=2)
pca_data=pca.fit_transform(standardized_data)

pca_df=pd.DataFrame(
pca_data,
columns=['PC1','PC2'])
print("\n4.Data after PCA:")
print(pca_df.round(2))


# In[ ]:




