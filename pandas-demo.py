#!/usr/bin/env python
# coding: utf-8
# please note this was written using Jupyter Notebook!

# In[1]:


# importing the Pandas module as simply panda
import pandas as panda


# In[2]:


# loading the stack overflow csv file 
data_frame = panda.read_csv('survey_results_public.csv')


# In[5]:


# invoking the dataframe, tail means only show the top rows, can specify number of rows in parenthesis
data_frame.tail(10)


# In[6]:


# loading the schema csv file, defines the meaning of the field titles
definition_frame = panda.read_csv('survey_results_schema.csv')


# In[7]:


definition_frame.head(10)


# In[9]:


# setting options 
panda.set_option('display.max_columns',70)
panda.set_option('display.max_rows',70)


# In[11]:


# invocation of the dataframe
data_frame


# In[20]:


data_frame.loc[56,['Employment','MainBranch']]


# In[21]:


data_frame.columns


# In[24]:


# specify the columns 
data_frame.columns


# In[28]:


# access an attribute/column and count its values by rows containing that value
data_frame['Employment'].value_counts()


# In[33]:


# loc triggers specific index and/or label and many rows can be accessed by using list
data_frame.loc[[76,54,34,87],['Employment','EdLevel']]


# In[36]:


# iloc only accesses certain row by index
data_frame.iloc[78]


# In[37]:


data_frame.columns


# In[40]:


# can use slicing to access a group of rows and the specified label
data_frame.loc[0:788,'Employment']


# In[41]:


# setting an index: can also use indexcol='name_of_tobe_index' when we first read the csv or invoke dataframe
data_frame.set_index('ResponseId')


# In[42]:


df.head()


# In[43]:


data_frame.head()


# In[44]:


data_frame.head(70).set_index('ResponseId')


# In[45]:


data_frame.set_index('ResponseId',inplace=True)


# In[54]:


panda.set_option('display.max_columns', 4)


# In[55]:


data_frame.head(10)


# In[57]:


# Know about an index
data_frame.index


# In[59]:


data_frame.loc[8,'Employment']


# In[61]:


data_frame.head()


# In[62]:


data_frame.reset_index()


# In[ ]:




