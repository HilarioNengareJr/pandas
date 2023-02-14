#!/usr/bin/env python
# coding: utf-8

# In[10]:


people = {
    "first" : ['John','Jack','James'],
    "last" : ['Doe','Chan','Bond'],
    "email" : ['jd@email.com','chan@email.com','bond@email.com']
}


# In[11]:


from pandas import DataFrame


# In[12]:


ppl_df = DataFrame(people)


# In[6]:


ppl_df


# In[14]:


ppl_df['last']


# In[15]:


ppl_df[['last','email']]


# In[16]:


type(ppl_df[['last','email']])


# In[29]:


n = input("Enter index ")
try:
    if n:
        print(ppl_df.iloc[int(n)])
    else:
        print('you entered nothing!')
        
except:
    print(f'No such index {n}!')


# In[30]:


# check the dimensions of the dataframe, 3 rows and 3 columns in this case!
ppl_df.shape


# In[ ]:




