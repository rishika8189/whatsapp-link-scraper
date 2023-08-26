#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Python program to demonstrate
# selenium

# import webdriver
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import requests
from selenium.webdriver.common.by import By
import os


chat_name=input("please enter the name of the chat you want to find the links from")
# create webdriver object
driver = webdriver.Chrome()

# get google.co.in
driver.get("https://web.whatsapp.com/")
time.sleep(35)
search_box = driver.find_element(By.XPATH,'//div[@contenteditable="true"]')
search_box.send_keys(chat_name)
time.sleep(2)
search_box.send_keys(Keys.ENTER)
time.sleep(60) 

for i in range(30):
    driver.execute_script("document.body.scrollTop += 500;") 
    time.sleep(20)

message_bubbles = driver.find_elements(By.XPATH, '//div[contains(@class, "message-in") or contains(@class, "message-out")]')
import re
# Extract and filter HTTPS links using regular expressions
https_links = []
for bubble in message_bubbles:
    message = bubble.text
    links = re.findall(r'https://[^\s]+', message)
    https_links.extend(links)

# Print the extracted links
for link in https_links:
    print(link)
    
driver.quit()


# In[ ]:




