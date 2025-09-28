"""
Web Scraping Project
Author: Imran (BSCS Student)
Description:
    This script uses Selenium and BeautifulSoup (bs4) to scrape the latest news headlines
    from the BBC News website and save them into a CSV file.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time


def scrape_bbc_headlines():
    # Launch Chrome browser (make sure you have ChromeDriver installed)
    driver = webdriver.Chrome()
    driver.get("https://www.bbc.com/news")
    time.sleep(5)  # wait for page to load

    # Get page source
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    # Extract headlines
    headlines = [h.text.strip() for h in soup.find_all("h2") if h.text.strip()]

    # Save to CSV
    df = pd.DataFrame(headlines, columns=["Headline"])
    df.to_csv("headlines.csv", index=False)

    print(f"{len(headlines)} headlines scraped and saved to headlines.csv")


if __name__ == "__main__":
    scrape_bbc_headlines()
