#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a python program to scrape the details of most downloaded articles from AI in last 90 days.https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles
#Scrape below mentioned details and make data frame-
#i) Paper Title

#ii) Authors
#iii) Published Date
#iv) Paper URL


# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


article = requests.get ('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')


# In[4]:


soup = BeautifulSoup(article.content)
soup


# In[6]:


paper_title = []

for i in soup.find_all('h2',class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg"):
    paper_title.append(i.text)
    
    
paper_title


# In[7]:


authors = []

for i in soup.find_all('span',class_="sc-1w3fpd7-0 dnCnAO"):
    authors.append(i.text)
    
    
authors


# In[8]:


pdates = []

for i in soup.find_all('span',class_="sc-1thf9ly-2 dvggWt"):
    pdates.append(i.text)
    
    
pdates


# In[13]:


links = []

for i in soup.find_all('a',class_="sc-5smygv-0 fIXTHm"):
    links.append(i.get('href'))
    
    
links


# In[14]:


print (len(paper_title), len(authors),len(pdates),len(links))


# In[16]:


import pandas as pd 
df = pd.DataFrame({'Paper_Title': paper_title,'Authors': authors,'Published dates': pdates,'URL': links}) 
df


# In[ ]:




