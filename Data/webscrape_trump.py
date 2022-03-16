# importing libraries:
from re import A
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd
import requests
import bs4
from bs4 import BeautifulSoup


# Setting up the chrome driver:
from selenium.webdriver.chrome.service import Service
ser = Service("/Users/AnaPSilva/Documents/Ana/Ironhack/Bootcamp/Final_Project/Data_Speeches/chromedriver 3")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

# Scraping the website:
website = "https://millercenter.org/the-presidency/presidential-speeches?field_president_target_id[8396]=8396"
driver.get(website)


all_speeches = driver.page_source
time.sleep(10)

all_speeches = driver.page_source


###### make request WEB SCRAPING NORMAL
soup_trump = BeautifulSoup(all_speeches,features="lxml")

######getting an uncleaned list of hrefs
result = soup_trump.find_all('span',attrs={'class':'field-content'})
speech_list = []
for speech in result:
    speech_list.append(speech.a)

print(speech_list)

## exporting to clean in a notebook file
speech_list = pd.Series(speech_list,copy=False)
speech_list.to_csv('uncleaned_trump_list.csv')