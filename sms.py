#!/bin/python3

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time


chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get("https://mytoolstown.com/smsbomber")
driver.findElement(By.id("mobno")).sendKeys("8872213990")
driver.findElement(By.id("count")).sendKeys("199")
driver.findElement(By.id('startsms')).sendKeys(Key.RETURN)

time.sleep(1000)

#setTimeout(() {
#driver.quit()
#}, 20000)
