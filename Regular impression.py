#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)


# In[22]:


import regex as re 
string1="This is Numaan Shaikh from HYD batch DS2306"
N = re.findall("[A-Z]",string1)
print(N)


# In[23]:


R=re.findall("[a-z]",string1)
print(R)


# In[25]:


N=re.findall("[0-9]",string1)
print(N)


# In[26]:


#we can write as below to find all numers


# In[27]:


import regex as re
nun="Abhi got 420 marks in the 5 th sem where in maths he got 98"
pattern="\d"
A = re.findall(pattern,nun)
print(A)


# In[28]:


#Question 2- Create a function in python that matches a string that has an a followed by zero or more b's


# In[57]:


import regex as re 
baller="aaballer aballs on the abat to aaabbbaby boy"
pattern= r'a+b*'
b=re.match(pattern, baller)
print(b)


# In[62]:


#Question 3-  Create a function in python that matches a string that has an a followed by one or more b's


# In[76]:


import regex as re 
baller="abb"
pattern= r'^ab+$'
b=re.match(pattern,baller)
print(b)


# In[ ]:


#Question 4- Create a function in Python and use RegEx that matches a string that has an a followed by zero or one 'b'.


# In[84]:


import regex as re 
baller="ab"
pattern= r'^ab?$'
b=re.match(pattern,baller)
print(b)


# In[ ]:


#Question 5- Write a Python program that matches a string that has an a followed by three 'b'.


# In[85]:


import regex as re 
baller="abbb"
pattern= r'^ab{3}$'
b=re.match(pattern,baller)
print(b)


# In[ ]:


#Question 6- Write a regular expression in Python to split a string into uppercase letters.
#Sample text: “ImportanceOfRegularExpressionsInPython”
#Output: [‘Importance’, ‘Of’, ‘Regular’, ‘Expression’, ‘In’, ‘Python’]


# In[86]:


import regex as re 
string = "ImportanceOfRegularExpressionsInPython"
pattern = r'[A-Z][a-z]*'
result = re.findall(pattern, string)
print(result)


# In[ ]:


#Question 7- Write a Python program that matches a string that has an a followed by two to three 'b'.


# In[88]:


import regex as re 
baller="abbb"
pattern= r'^ab{2,3}$'
b=re.match(pattern,baller)
print(b)


# In[ ]:


#Question 8- Write a Python program to find sequences of lowercase letters joined with a underscore.


# In[87]:


import regex as re
underscores = "hey_buddy how is_ it_going with_lowercase_letters"
pattern = r'[a-z]+_[a-z]+'
ud = re.findall(pattern, underscores)
print(ud)


# In[ ]:


#Question-9- Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.


# In[41]:


import regex as re 
string="acfehdlkb"
pattern = r'^a.*b$'
beb=re.match(pattern, string)
print(beb)


# In[89]:


#Question 10- Write a Python program that matches a word at the beginning of a string.


# In[104]:


import regex as re 
string= "Hey buddy, how are you"
pattern = '^Hey'
b=re.findall(pattern,string)
print(b)


# In[ ]:


#Question 11- Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.


# In[112]:


import regex as re 
string= "Hy_Raftaar-1568__"
pattern = r'^[a-z_A-Z-0-9_]+$'
Rap=re.findall(pattern,string)
print(Rap)


# In[ ]:


#Question 12- Write a Python program where a string will start with a specific number. 


# In[115]:


import regex as re
pattern = "[0-9]+"
find=re.findall(pattern,"123489vjuhdsvkj1698")
print(find)


# In[ ]:


#Question 13- Write a Python program to remove leading zeros from an IP address


# In[30]:





# In[ ]:


#Question 14- Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.
Sample text : ' On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country’.
Output- August 15th 1947
Hint- Use re.match() method here


# In[ ]:


import regex as re
sentence=' On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country’.
pattern = r'\b[A-Z][a-z]+\s\d{1,2}(?:st|nd|rd|th)?\s\d{4}\b'
dates = re.match(pattern, sentence)
print(dates)


# In[3]:


#Question 15- Write a Python program to search some literals strings in a string. Go to the editor
#Sample text : 'The quick brown fox jumps over the lazy dog.'
#Searched words : 'fox', 'dog', 'horse'


# In[21]:


import regex as re
Sample_text = 'The quick brown fox jumps over the lazy dog.'
for text in Sample_text:
    search = re.search('fox', Sample_text)
    print(search)


# In[23]:


import regex as re
Sample_text = 'The quick brown fox jumps over the lazy dog.'
for text in Sample_text:
    search = re.search('dog', Sample_text)
    print(search)


# In[ ]:


import regex as re
Sample_text = 'The quick brown fox jumps over the lazy dog.'
for text in Sample_text:
    search = re.search('horse', Sample_text)
    print(search)


# In[ ]:


#Question 16- Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
#Sample text : 'The quick brown fox jumps over the lazy dog.'
#Searched words : 'fox'


# In[24]:


import regex as re
Sample_text = 'The quick brown fox jumps over the lazy dog.'
for text in Sample_text:
    search = re.search('fox', Sample_text)
    print(search)


# In[ ]:


#Question 17- Write a Python program to find the substrings within a string.
#Sample text : 'Python exercises, PHP exercises, C# exercises'
#Pattern : 'exercises'.


# In[26]:


import regex as re 
input_string = 'Python exercises, PHP exercises, C# exercises'
search_pattern = 'exercises'
output = re.findall(search_pattern, input_string)
print(output)


# In[ ]:


#Question 18- Write a Python program to find the occurrence and position of the substrings within a string.


# In[ ]:





# In[ ]:


#Question 19- Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.


# In[ ]:


import regex as re 
date= "year-month-day"
dates=date.split("-")
new_dates=f"{day}-{month}-{year}"
print (new_dates)


# In[ ]:


#Question 20- Write a Python program to find all words starting with 'a' or 'e' in a given string.


# In[42]:


import regex as re 
string = "an elephant always eats apples and drinks water"
pattern=r'\b[ae]\w+\b'
output=re.findall(pattern,string)
print(output)


# In[ ]:


#Question 21- Write a Python program to separate and print the numbers and their position of a given string


# In[45]:


import regex as re 
string = "Hey guys 123"
pattern=r'\d+'
output=re.search(pattern,string)
print(output)


# In[ ]:


#Question 22- Write a regular expression in python program to extract maximum numeric value from a string


# In[53]:


import regex as re 
line="I've 10 circket kits and friends are 7 but we need 11 players to play"
pattern=r'\d+'
friends = re.findall(pattern,line)
print(friends)


# In[ ]:


#Question 23- Write a Regex in Python to put spaces between words starting with capital letters


# In[ ]:


import regex as re 
line="I'veCircketKits andFriends are 7 butWe need 11PlayersToplay"
friends = re.sub(r'(\w)([A-Z])',' ',line)
print(friends)


# In[ ]:


#Question 24- Python regex to find sequences of one upper case letter followed by lower case letters


# In[81]:


import regex as re 
line="I've 10 Circket kits and Friends are 7 But we need 11 Players To play"
pattern=r'[A-z][a-z]+'
friends = re.findall(pattern,line)
print(friends)


# In[32]:


#Question 25- Write a Python program to remove duplicate words from Sentence using Regular Expression


# In[33]:


import regex as re 
string= "I went to to shop to get milk milk packets and and biscuit boxes boxes"
regex= r'\b(\w+)(?:\W+\1\b)+'

n=re.sub(regex, r'\1', string)
print(n)


# In[ ]:


#Question 26-  Write a python program using RegEx to accept string ending with alphanumeric character.


# In[83]:


import regex as re 
string="Hey sick-bay102"
pattern=r'\w$'
timepass=re.search(pattern,string)
print(timepass)


# In[ ]:


#Question 27-Write a python program using RegEx to extract the hashtags.
Sample Text: text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
Output: ['#Doltiwal', '#xyzabc', '#Demonetization']


# In[97]:


import regex as re 
Sample = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
#Output: ['#Doltiwal', '#xyzabc', '#Demonetization']
pattern= r'#\w+'
output= re.findall(pattern, Sample)
print(output)


# In[ ]:


#Question 28- Write a python program using RegEx to remove <U+..> like symbols
#Check the below sample text, there are strange symbols something of the sort <U+..> all over the place. You need to come up with a general Regex expression that will cover all such symbols.
#Sample Text: "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
#Output: @Jags123456 Bharat band on 28??<ed><ed>Those who  are protesting #demonetization  are all different party leaders


# In[ ]:


import regex as re 
Text= "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
#Output: @Jags123456 Bharat band on 28??<ed><ed>
output= re.sub(r"<U\+[A-Fa-f0-9]+\>","",Text) 
print(output)


# In[ ]:


#Question 29- Write a python program to extract dates from the text stored in the text file.
#Sample Text: Ron was born on 12-09-1992 and he was admitted to school 15-12-1999.
#Store this sample text in the file and then extract dates.


# In[ ]:


import regex as re 
Date_pattern = "Ron was born on 12-09-1992 and he was admitted to school 15-12-1999."
final = re.findall(r'\d{2}-\d{2}-{4}', Date_pattern)
print(final)


# In[34]:


#Question 30- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
#Sample Text- 'Python Exercises, PHP exercises.'
#Output: Python:Exercises::PHP:exercises:


# In[35]:


import regex as re
sample_text = 'Python Exercises, PHP exercises.'

def replace_characters(text):
    replacements = [' ', ',', '.']
    for char in replacements:
        text = text.replace(char, ':')
    return text
output_text = replace_characters(sample_text)
print(output_text)


# In[ ]:




