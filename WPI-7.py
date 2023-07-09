#!/usr/bin/env python
# coding: utf-8

# In[1]:


#7. Write a python program to scrape mentioned details from dineout.co.inand make data frame-
#i) Restaurant name
#ii) Cuisine
#iii) Location
#iv) Ratings
#v) Image URL


# In[3]:


from bs4 import BeautifulSoup
import requests


# In[4]:


dineout = requests.get ('https://www.dineout.co.in/delhi-restaurants/buffet-special')


# In[5]:


soup = BeautifulSoup(dineout.content)
soup


# In[6]:


r_name = []

for i in soup.find_all('div',class_="restnt-info cursor"):
    r_name.append(i.text)
    
    
r_name


# In[11]:


cuisine = []

for i in soup.find_all('span',class_="double-line-ellipsis"):
    cuisine.append(i.text)
    
    
cuisine


# In[12]:


location = []

for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    location.append(i.text)
    
    
location


# In[13]:


ratings = []

for i in soup.find_all('div',class_="restnt-rating rating-4"):
    ratings.append(i.text)
    
    
ratings


# In[15]:


image = []

for i in soup.find_all('img',class_="no-img"):
    image.append(i.get('data-src'))
    
    
image


# In[16]:


print(len(r_name),len(cuisine),len(location),len(ratings),len(image))


# In[27]:


get_ipython().system('pip install pandas')


# In[28]:


import pandas as pd 


# In[35]:


df = pd.DataFrame({'R_name':r_name,'Cuisine':cuisine,'Location':location,'Ratings':ratings,'Image':image})
print(df)

