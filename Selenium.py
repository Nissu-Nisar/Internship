#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You
#have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10
#jobs data.
#This task will be done in following steps:
#1. First get the webpage https://www.naukri.com/
#2. Enter “Data Analyst” in “Skill, Designations, Companies” field and enter “Bangalore” in “enter the
#location” field.
#3. Then click the searchbutton.
#4. Then scrape the data for the first 10 jobs results youget.
#5. Finally create a dataframe of the scraped data.
#Note: All of the above steps have to be done in code. No step is to be done manually


# In[1]:


get_ipython().system('pip install selenium')
get_ipython().system('pip install webdriver-manager')


# In[11]:


import selenium                                  #library that is used to work with selenium

from selenium import webdriver                   #importing webdriver module from selenium to open automated chrome window

import pandas as pd                              #to create DataFrame

from selenium.webdriver.common.by import By      #importing inbuilt class By 

import warnings                                  #to ignore any sort of warning

warnings.filterwarnings("ignore")

import time                                      #use to stop search engine for few seconds

driver = webdriver.Chrome()

driver.get("https://www.naukri.com/")


# In[12]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input ")
designation.send_keys('Data Analyst')


# In[13]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys('Bangalore')


# In[14]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[15]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[16]:


title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    titles_tags=i.text
    job_title.append(title_tags)

location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location_tags=i.text
    job_location.append(location_tags)
    
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company_tags=i.text
    company_name.append(company_tags)
    
experience_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience_tags[0:10]:
    experience_tags=i.text
    experience_required.append(experience_tags)
    


# In[17]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[18]:


import pandas as pd 
df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company':company_name,'EXP':experience_required})
df


# In[ ]:





# In[19]:


#Q2:Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You
#have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.
#This task will be done in following steps:
#1. First get the webpage https://www.naukri.com/
#2. Enter “Data Scientist” in “Skill, Designations, Companies” field and enter “Bangalore” in “enter the
#location” field.
#3. Then click the searchbutton.
#4. Then scrape the data for the first 10 jobs results youget.
#5. Finally create a dataframe of the scraped data.
#Note: All of the above steps have to be done in code. No step is to be done manually.


# In[20]:


import selenium                                  #library that is used to work with selenium

from selenium import webdriver                   #importing webdriver module from selenium to open automated chrome window

import pandas as pd                              #to create DataFrame

from selenium.webdriver.common.by import By      #importing inbuilt class By 

import warnings                                  #to ignore any sort of warning

warnings.filterwarnings("ignore")

import time                                      #use to stop search engine for few seconds

driver = webdriver.Chrome()

driver.get("https://www.naukri.com/")


# In[21]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input ")
designation.send_keys('Data Scientist')


# In[22]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys('Bangalore')


# In[23]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[24]:


job_title=[]
job_location=[]
company_name=[]


# In[25]:


title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    titles_tags=i.text
    job_title.append(title_tags)

location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location_tags=i.text
    job_location.append(location_tags)
    
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company_tags=i.text
    company_name.append(company_tags)


# In[26]:


print(len(job_title),len(job_location),len(company_name))


# In[27]:


import pandas as pd 
df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company':company_name,})
df


# In[28]:


#Q3: In this question you have to scrape data using the filters available on the webpage as shown below:
 #       You have to use the location and salary filter.
#You have to scrape data for “Data Scientist” designation for first 10 job results.
#You have to scrape the job-title, job-location, company name, experience required.
#The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs
#The task will be done as shown in the below steps:
#1. first get thewebpage https://www.naukri.com/
#2. Enter “Data Scientist” in “Skill, Designations, and Companies” field.
#3. Then click the searchbutton.
#4. Then apply the location filter and salary filter by checking the respectiveboxes
#5. Then scrape the data for the first 10 jobs results youget.
#6. Finally create a dataframe of the scrapeddata.
#Note: All of the above steps have to be done in code. No step is to be done manually


# In[157]:


import selenium                                  #library that is used to work with selenium

from selenium import webdriver                   #importing webdriver module from selenium to open automated chrome window

import pandas as pd                              #to create DataFrame

from selenium.webdriver.common.by import By      #importing inbuilt class By 

import warnings                                  #to ignore any sort of warning

warnings.filterwarnings("ignore")

import time                                      #use to stop search engine for few seconds

driver = webdriver.Chrome()

driver.get("https://www.naukri.com/")


# In[158]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input ")
designation.send_keys('Data Scientist')


# In[159]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[160]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[5]/div[2]/div[2]/label/i")
location.click()


# In[161]:


salary=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[6]/div[2]/div[2]/label/i")
salary.click()


# In[164]:


job_title=[]
job_location=[]
company_name=[]
experience=[]


# In[168]:


title=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title[0:10]:
    title=i.text
    job_title.append(title)

location=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location[0:10]:
    location=i.text
    job_location.append(location)
    
company=driver.find_elements(By.XPATH,'//div[@class="companyInfo subheading"]')
for i in company[0:10]:
    company=i.text
    company_name.append(company)
    
experiences=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experiences[0:10]:
    experiences=i.text
    experience.append(experiences)


# In[169]:


print(len(job_title),len(job_location),len(company_name),len(experience))


# In[170]:


import pandas as pd 
df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company':company_name,'Exp':experience})
df


# In[ ]:





# In[ ]:





# In[64]:


#Q4: Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
#1. Brand
#2. ProductDescription
#3. Price
#The attributes which you have to scrape is ticked marked in the below image.


# In[134]:


import selenium                                  #library that is used to work with selenium

from selenium import webdriver                   #importing webdriver module from selenium to open automated chrome window

import pandas as pd                              #to create DataFrame

from selenium.webdriver.common.by import By      #importing inbuilt class By 

import warnings                                  #to ignore any sort of warning

warnings.filterwarnings("ignore")

import time                                      #use to stop search engine for few seconds

driver = webdriver.Chrome()

driver.get("https://www.flipkart.com/")


# In[135]:


designation=driver.find_element(By.CLASS_NAME,"_3704LK")
designation.send_keys('sunglasses')


# In[137]:


search=driver.find_element(By.CLASS_NAME,"L0Z3Pu")
search.click()


# In[138]:


brands=[]
products=[]
price=[]


# In[139]:


brand_glasses=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in brand_glasses[0:35]:
    brand_glasses=i.text
    brands.append(brand_glasses)

product_desc=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in product_desc[0:35]:
    product_desc=i.text
    products.append(product_desc)
    
price_discounts=driver.find_elements(By.XPATH,'//a[@class="_3bPFwb"]')
for i in price_discounts[0:35]:
    price_discounts=i.text
    price.append(price_discounts)
    
    


# In[140]:


print(len(brands),len(products),len(price))


# In[141]:


import pandas as pd 
df=pd.DataFrame({'Brand':brands,'Product':products,'Price&Disc.':price,})
df


# In[142]:


search=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[2]")
search.click()


# In[148]:


brands=[]
products=[]
price=[]


# In[149]:


brand_glasses=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in brand_glasses[0:35]:
    brand_glasses=i.text
    brands.append(brand_glasses)

product_desc=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in product_desc[0:35]:
    product_desc=i.text
    products.append(product_desc)
    
price_discounts=driver.find_elements(By.XPATH,'//a[@class="_3bPFwb"]')
for i in price_discounts[0:35]:
    price_discounts=i.text
    price.append(price_discounts)
    


# In[150]:


print(len(brands),len(products),len(price))


# In[151]:


import pandas as pd 
df=pd.DataFrame({'Brand':brands,'Product':products,'Price&Disc.':price,})
df


# In[152]:


search=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[4]")
search.click()


# In[153]:


brands=[]
products=[]
price=[]


# In[154]:


brand_glasses=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in brand_glasses[0:30]:
    brand_glasses=i.text
    brands.append(brand_glasses)

product_desc=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in product_desc[0:30]:
    product_desc=i.text
    products.append(product_desc)
    
price_discounts=driver.find_elements(By.XPATH,'//a[@class="_3bPFwb"]')
for i in price_discounts[0:30]:
    price_discounts=i.text
    price.append(price_discounts)


# In[155]:


print(len(brands),len(products),len(price))


# In[156]:


import pandas as pd 
df=pd.DataFrame({'Brand':brands,'Product':products,'Price&Disc.':price,})
df


# In[177]:


#Q5: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link:
#https://www.flipkart.com/apple-iphone-11-black-64-gb/productreviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market
#place=FLIPKART

#As shown in the above page you have to scrape the tick marked attributes. These are:
#1. Rating
#2. Review summary
#3. Full review
#4. You have to scrape this data for first 100reviews.
#Note: All the steps required during scraping should be done through code only and not manually


# In[36]:


import selenium                                  #library that is used to work with selenium

from selenium import webdriver                   #importing webdriver module from selenium to open automated chrome window

import pandas as pd                              #to create DataFrame

from selenium.webdriver.common.by import By      #importing inbuilt class By 

import warnings                                  #to ignore any sort of warning

warnings.filterwarnings("ignore")

import time                                      #use to stop search engine for few seconds

driver = webdriver.Chrome()

driver.get("https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZE3ENS&marketplace=FLIPKART")


# In[38]:


ratings=[]
reviews=[]
full_reviews=[]


# In[42]:


rating_star=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
for i in rating_star[0:10]:
    rating_star=i.text
    ratings.append(rating_star)

review_tags=driver.find_elements(By.XPATH,'/html/body/div/div/div[3]/div/div/div[2]/div[12]/div/div/div/div[1]/p')
for i in review_tags[0:10]:
    review_tags=i.text
    reviews.append(review_tags)
    
fullreview_tags=driver.find_elements(By.XPATH,'/html/body/div/div/div[3]/div/div/div[2]/div[12]/div/div/div/div[2]/div/div/div')
for i in fullreview_tags[0:10]:
    fullreview_tags=i.text
    full_reviews.append(fullreview_tags)
    


# In[ ]:


print(len(ratings),len(reviews),len(full_reviews))


# In[228]:


#Q7: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then
#set CPU Type filter to “Intel Core i7” as shown in the below image:
#After setting the filters scrape first 10 laptops data. You have to scrape 3 attributes for each laptop:
#1. Title
#2. Ratings
#3. Price


# In[44]:


import selenium                                  #library that is used to work with selenium

from selenium import webdriver                   #importing webdriver module from selenium to open automated chrome window

import pandas as pd                              #to create DataFrame

from selenium.webdriver.common.by import By      #importing inbuilt class By 

import warnings                                  #to ignore any sort of warning

warnings.filterwarnings("ignore")

import time                                      #use to stop search engine for few seconds

driver = webdriver.Chrome()

driver.get("https://www.amazon.in/")


# In[45]:


designation=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
designation.send_keys('laptop')


# In[46]:


search=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input")
search.click()


# In[47]:


intel=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[7]/span[11]/li/span/a/div/label/i")
intel.click()


# In[48]:


title=[]
ratings=[]
price=[]


# In[49]:


title_tags=driver.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-normal"]')
for i in title_tags[:10]:
    title_tags=i.text
    title.append(title_tags)

ratings_tags=driver.find_elements(By.XPATH,'//i[@class="a-icon a-icon-star-small a-star-small-3-5 aok-align-bottom"]')
for i in ratings_tags[:10]:
    ratings_tags=i.text
    ratings.append(ratings_tags)
    
price_tags=driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
for i in price_tags[:10]:
    price_tags=i.text
    price.append(price_tags)
    


# In[50]:


print(len(title),len(ratings),len(price))


# In[ ]:


#Q8: Write a python program to scrape data for Top 1000 Quotes of All Time.
#The above task will be done in following steps:
#1. First get the webpagehttps://www.azquotes.com/
#2. Click on TopQuotes
#3. Than scrap a) Quote b) Author c) Type Of Quotes


# In[54]:


import selenium                                  #library that is used to work with selenium

from selenium import webdriver                   #importing webdriver module from selenium to open automated chrome window

import pandas as pd                              #to create DataFrame

from selenium.webdriver.common.by import By      #importing inbuilt class By 

import warnings                                  #to ignore any sort of warning

warnings.filterwarnings("ignore")

import time                                      #use to stop search engine for few seconds

driver = webdriver.Chrome()

driver.get("https://www.azquotes.com/")


# In[55]:


search=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a")
search.click()


# In[56]:


quote=[]
author=[]
q_type=[]


# In[63]:


quote_tags=driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/ul/li[1]/div/p/a[2]')
for i in quote_tags[:10]:
    quote_tags=i.text
    quote.append(quote_tags)

author_tags=driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/ul/li[1]/div/div[1]/a')
for i in author_tags[:10]:
    author_tags=i.text
    author.append(author_tags)
quote_type=driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/ul/li[1]/div/div[2]/div[1]')
for i in quote_type[:10]:
    quote_type=i.text
    q_type.append(quote_type)
    


# In[ ]:


print(len(quote),len(author),len(q_type))


# In[ ]:





# In[ ]:





# In[ ]:


Q9: Write a python program to display list of respected former Prime Ministers of India(i.e. Name, Born-Dead, 
Term of office, Remarks) from https://www.jagranjosh.com/.µxa
This task will be done in following steps:
1. First get the webpagehttps://www.jagranjosh.com/
2. Then You have to click on the GK option
3. Then click on the List of all Prime Ministers of India
4. Then scrap the mentioned data and make theDataFrame


# In[81]:


import selenium                                  #library that is used to work with selenium

from selenium import webdriver                   #importing webdriver module from selenium to open automated chrome window

import pandas as pd                              #to create DataFrame

from selenium.webdriver.common.by import By      #importing inbuilt class By 

import warnings                                  #to ignore any sort of warning

warnings.filterwarnings("ignore")

import time                                      #use to stop search engine for few seconds

driver = webdriver.Chrome()

driver.get("https://www.jagranjosh.com/")


# In[82]:


option=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div[1]/div/div[5]/div/div[1]/header/div[3]/ul/li[3]/a")
option.click()


# In[83]:


prime=driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div[10]/div/div/ul/li[2]/a")
prime.click()


# In[84]:


name=[]
dob=[]
term=[]
remarks=[]


# In[88]:


name_tags=driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[3]/table/tbody/tr[2]/td[2]/p/strong/a')
for i in name_tags[0:19]:
    name_tags=i.text
    name.append(name_tags)

date_tags=driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[3]/table/tbody/tr[2]/td[3]/p')
for i in date_tags[0:19]:
    date_tags=i.text
    dob.append(date_tags)
    
term_tags=driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[3]/table/tbody/tr[2]/td[4]/p[1]')
for i in term_tags[0:19]:
    term_tags=i.text
    price.append(term_tags)
    
remarks_tags=driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[3]/table/tbody/tr[2]/td[5]/p')
for i in remarks_tags[0:19]:
    remarks_tags=i.text
    remarks.append(remarks_tags)
    


# In[ ]:


print(len(name_tags),len(date_tags),len(term_tags),len(remarks_tags))


# In[15]:


#Q10: Write a python program to display list of 50 Most expensive cars in the world (i.e. 
#Car name and Price) from https://www.motor1.com/
#This task will be done in following steps:
#1. First get the webpagehttps://www.motor1.com/
#2. Then You have to type in the search bar ’50 most expensive cars’
#3. Then click on 50 most expensive carsin the world..
#4. Then scrap the mentioned data and make the dataframe


# In[16]:


import selenium                                  #library that is used to work with selenium

from selenium import webdriver                   #importing webdriver module from selenium to open automated chrome window

import pandas as pd                              #to create DataFrame

from selenium.webdriver.common.by import By      #importing inbuilt class By 

import warnings                                  #to ignore any sort of warning

warnings.filterwarnings("ignore")

import time                                      #use to stop search engine for few seconds

driver = webdriver.Chrome()

driver.get("https://www.motor1.com/")


# In[19]:


designation=driver.find_element(By.XPATH,"/html/body/div[10]/div[2]/div/div/div[3]/div/div/div/form/input")
designation.send_keys('50 most expensive cars')


# In[22]:


search=driver.find_element(By.XPATH,'/html/body/div[10]/div[2]/div/div/div[3]/div/div/div/form/button[1]')
search.click()


# In[26]:


search=driver.find_element(By.XPATH,'/html/body/div[10]/div[9]/div/div[1]/div/div/div[2]/div/div[1]/h3/a')
search.click()


# In[33]:


cars=[]
prices=[]


# In[34]:


names=driver.find_elements(By.XPATH,'/html/body/div[10]/div[7]/div[2]/div[1]/div[2]/div[1]/h3[1]')
for i in names[0:50]:
    names=i.text
    cars.append(names)

prices_tags=driver.find_elements(By.XPATH,'/html/body/div[10]/div[7]/div[2]/div[1]/div[2]/div[1]/p[4]/strong')
for i in prices_tags[0:50]:
    prices_tags=i.text
    prices.append(prices_tags)


# In[35]:


print(len(cars),len(prices))


# In[ ]:




