from selenium import webdriver
import time
import os
import argparse
import configparser

# Set up configuration file parsing
config = configparser.ConfigParser()
config.read("config.ini")

# Get the URL and time interval from the config file
url = config["WEBSITE"]["url"]
interval = float(config["REFRESH"]["interval"])

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Set up a flag to indicate whether the refreshing process is paused
paused = False

# Refresh the page continuously
while True:
    if not paused:
        driver.get(url)
        time.sleep(interval)
    else:
        time.sleep(1)  # Wait for 1 second before checking again

    # Check for user input to pause or resume the refreshing process
    if os.name == "nt":  # For Windows OS
        import msvcrt

        if msvcrt.kbhit() and msvcrt.getch() == b" ":
            paused = not paused
            print(f'Refreshing process is {"paused" if paused else "resumed"}')
    else:  # For Unix-like OS
        import select
        import sys

        if select.select(
            [
                sys.stdin,
            ],
            [],
            [],
            0.0,
        )[0]:
            if sys.stdin.readline().strip() == " ":
                paused = not paused
                print(f'Refreshing process is {"paused" if paused else "resumed"}')
