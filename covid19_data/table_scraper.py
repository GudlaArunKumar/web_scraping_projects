"""
This scripts scraps the tabular data about state wise covid-19 stats
from India website
"""

from selenium import *
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait
import pandas 

options = Options()

options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path='G:\Machine_Learning_Projects\CloudyML course\Learning\projects\web_scraping\chromedriver.exe', options=options)

driver.get('https://www.covid19india.org/')

driver.maximize_window() # it maximizes window so that it can find all the html elements

# program waits for 15 second until it finds class name "Table" in the html

timeout = 15 # driver quits the if it doesn't find below class name within 10 seconds
try:
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, 'Table')))
except TimeoutException:
    driver.quit()
    
table_elements = driver.find_element(By.CLASS_NAME, "Table") # this extracts all the content present under class 'Table'
#print(table_elements.text)

elements_list = table_elements.text.split('\n')
up_arrow = chr(8593) # saving the up arrow char to a variable
down_arrow = chr(8595)

# to remove numbers with up and down arrow
for x in elements_list:
    for y in range(len(x)):
        if up_arrow == x[y] or down_arrow == x[y]:
            elements_list.remove(x)
            break
        
#print(elements_list)
total_rows = (len(elements_list) - 2) // 7
print("total_rows: ", total_rows)


# Making a dataframe for the covid-19 stats state-wise table
state_wise_table = []

i = 2
j = 9
count = 9
num_row = 0

while num_row < total_rows:
    temp_list = []
    
    while i < j:
        temp_list.append(elements_list[i])
        i = i + 1
        count = count + 1
        
    state_wise_table.append(temp_list)
    j = count
    num_row = num_row + 1
    
#print(state_wise_table)

column_names = state_wise_table[0]
state_wise_table.pop(0)

covid19_stats = pandas.DataFrame(state_wise_table, columns=column_names)

# converting data frame into csv file
covid19_stats.to_csv('covid19_stats.csv', index=False)

