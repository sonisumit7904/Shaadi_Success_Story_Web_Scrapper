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