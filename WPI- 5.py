#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#5. Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world and make data frame-
#i) Headline

#ii) Time
#iii) News Link


# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[17]:


from bs4 import BeautifulSoup
import pandas as pd
import requests


# In[4]:


news = requests.get ('https://www.cnbc.com/world/?region=world')


# In[5]:


soup = BeautifulSoup(news.content)
soup


# In[9]:


latest_news = []

for i in soup.find_all('a',class_="LatestNews-headline"):
    latest_news.append(i.text)
    
    
latest_news


# In[10]:


time = []

for i in soup.find_all('time',class_="LatestNews-timestamp"):
    time.append(i.text)
    
    
time


# In[15]:


links = []

for i in soup.find_all('a',class_="LatestNews-headline"):
    links.append(i.get('href'))
    
    
links


# In[16]:


print(len(latest_news), len(time), len (links))


# In[33]:


import pandas as pd 
df = pd.DataFrame({'Headline':latest_news,'Time':time,'News_Links':links})
df


# In[ ]:





# In[ ]:





# In[ ]:




