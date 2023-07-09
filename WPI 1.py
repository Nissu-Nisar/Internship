#!/usr/bin/env python
# coding: utf-8

# In[63]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


response = requests.get('https://en.wikipedia.org/wiki/Main_Page')


# In[3]:


response.status_code


# In[ ]:


#Write a python program to display all the header tags from wikipedia.org and make data frame.


# In[11]:


from bs4 import BeautifulSoup
import requests

wiki = requests.get('https://en.wikipedia.org/wiki/Main_Page')


# In[12]:


soup = BeautifulSoup(wiki.content )
soup


# In[13]:


headers = []

for i in soup.find_all('span',class_="mw-headline"):
    headers.append(i.text)
    
    
headers


# In[14]:


import pandas as pd 


# In[15]:


df = pd.DataFrame(headers, columns=["Header"])
print (df)

