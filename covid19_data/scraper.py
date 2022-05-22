"""
This script scraps only the important stats from the covid-19 India 
website. 
"""

from selenium import *
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait

options = Options()

options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path='G:\Machine_Learning_Projects\CloudyML course\Learning\projects\web_scraping\chromedriver.exe', options=options)

driver.get('https://www.covid19india.org/')

driver.maximize_window() # it maximizes window so that it can find all the html elements

# program waits for 15 second until it finds class name "level-vaccinated" in the html

timeout = 15 # driver quits the if it doesn't find below class name within 15 seconds
try:
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, 'Table')))
except TimeoutException:
    driver.quit()
    
# we will get class Level which has data about active, confirmed, recovered and deceased numbers

cases_current_data = driver.find_element(By.CLASS_NAME, "Level").text # getting only the text part(header)
#print(cases_current_data)
cases = cases_current_data.split('\n')
print("Today confirmed cases: ", cases[1])
print("Total confirmed cases: ", cases[2])
print("Total Active cases: ", cases[4])
print("Today recovered cases: ", cases[6])
print("Total recovered cases: ", cases[7])
print("Today deceased members: ", cases[9])
print("Total deceased members: ", cases[10])

# to get count of total tested members
tested_stats = driver.find_element(By.CLASS_NAME, "header-right")
print("Total tested: ",tested_stats.text.split('\n')[1])

# vaccinaction current stats
vaccination_stats = driver.find_element(By.CLASS_NAME, "level-vaccinated")
print("Total Vaccinated doses: ",vaccination_stats.text.split('\n')[0])

# extracting details from vaccination header bar
vaccine_pg_bar = driver.find_element(By.CLASS_NAME, "progress-bar")
print("Atleast one dose: ", vaccine_pg_bar.text)

full_vacc_bar = driver.find_elements(By.CLASS_NAME, "label")
print("Fully vaccinated: ", full_vacc_bar[1].text)
