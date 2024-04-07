from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

import pandas as pd
from bs4 import BeautifulSoup
import requests
import html

import pandas as pd

path = "D:/chromedriver.exe"
s = Service(path)

driver = webdriver.Chrome(service=s)
url = "https://www.shaadi.com/shaadi-info/matrimonial-success-stories/featured"
driver.get(url)
# time.sleep(2)


# Array for all data
couple_names = []
wedding_dates = []
couple_desc = []

# Going TO NEXT PAGE ================
# loop_time = how many pages you want to scrape
loop_time = 20
while loop_time:

    soup = BeautifulSoup(driver.page_source,"html.parser")
    # getting all couple_page links
    couple_Links = []
    couples = soup.findAll("div",{"class":"listing"})
    for i in couples:
        couple_link = i.find("a",{"class":"read_more"})['href']
        couple_Links.append("https://www.shaadi.com"+couple_link)


    # Getting data from each pages
    for page in couple_Links:
        f = requests.get(page)
        soup = BeautifulSoup(f.text,'html.parser')
        # getting couple name
        couple_names.append(soup.find("div",{"class":"ss_title"}).text)
        # getting couple wedding date
        wedding_dates.append(soup.find("div",{"class":"ss_wdate"}).text)
        # Couple Description
        first_div = soup.find('div', class_='ss_copy')
        ss_carousel_div = first_div.find('div', class_='ss_carousel')
        text_after_ss_carousel = ss_carousel_div.next_sibling.strip()
        decoded_text = html.unescape(text_after_ss_carousel)
        couple_desc.append(decoded_text)


    # getting to next page
    next_button = driver.find_element_by_class_name("ss_next_btm")
    next_button.click() #click load more button
    # waiting for 1 sec incase loading takes time
    time.sleep(1)
    loop_time-=1

# Saving the data in csv using Pandas
data_frame = pd.DataFrame({"COUPLE_NAMES":couple_names,"WEDDING_DATE":wedding_dates,"THEIR STORY":couple_desc})
data_frame.to_csv("Shaadi_Success_Story_Web_Scrapper.csv")
print("Web Scraping Done! .csv file has been created!")