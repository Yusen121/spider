import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

df = pd.read_csv('output.csv')

driver_path = '/usr/local/bin/chromedriver'
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

url = 'https://app.snov.io/search/single-email'
driver.get(url)

input("Press Enter to close the browser...")
driver.quit()


# for index, row in df.iterrows():
#     first_name = row['First Name']
#     last_name = row['Last Name']
#     company_name = row['Company']
#
#     # Fill in the first name
#     first_name_input = driver.find_element(By.ID, 'first_name')
#     first_name_input.clear()
#     first_name_input.send_keys(first_name)
#
#     # Fill in the last name
#     last_name_input = driver.find_element(By.ID, 'last_name')
#     last_name_input.clear()
#     last_name_input.send_keys(last_name)
#
#     # Fill in the company name
#     company_input = driver.find_element(By.ID, 'companyWebsite-id')
#     company_input.clear()
#     company_input.send_keys(company_name)
#     time.sleep(2)  # Wait for suggestions to appear
#
#     # Select the first suggestion for the company domain
#     try:
#         first_suggestion = WebDriverWait(driver, 10).until(
#             EC.visibility_of_element_located((By.CLASS_NAME, 'prospect-form__companies-item'))
#         )
#         first_suggestion.click()
#     except Exception as e:
#         print(f"Error selecting domain for {company_name}: {e}")
#         continue
#
#     # Click the "Find email" button
#     search_button = driver.find_element(By.CLASS_NAME, 'prospect-form__item--button')
#     search_button.click()
#
#     # Optional: Wait for the result to load or capture the output
#     time.sleep(5)
#
# # Close the browser when done
# driver.quit()