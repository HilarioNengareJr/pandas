#!/usr/bin/env python
# coding: utf-8

# In[1]:


# practical usage of loc[]


# In[2]:


import pandas as panda


# In[4]:


df = panda.read_csv('survey_results_public.csv')
# we are going to be using this schema csv file to utilize loc[]
schema_df = panda.read_csv('survey_results_schema.csv')


# In[6]:


df.head()


# In[12]:


# invoke the schema, ignore the metadata and start from 3, using loc to retrieve this info
schema_df.loc[3:]


# In[18]:


"""want to access the full sentence of index 74, which is by default ended with ellipsis. use loc with both index and label """ 
schema_df.loc[74, 'question']


# In[ ]:




