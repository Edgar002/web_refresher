from selenium import webdriver
import time
import os

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# URL of the web page you want to refresh
url = 'https://thanosvibs.money/tierlist'

# Refresh the page continuously
while True:
    driver.get(url)
    time.sleep(0.5)  # Wait for 5 seconds before refreshing again

