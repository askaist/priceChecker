

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import load_workbook

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://wassermansupermarket.com/#!_/flushing")

# Find the search bar and enter "milk"
search_bar = driver.find_element(By.ID, 'small-searchterms')
search_bar.send_keys("milk")

# Use an explicit wait for the search results to load
wait = WebDriverWait(driver, 10)
search_bar.send_keys(Keys.RETURN)

# Find the price element using an explicit wait
price_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'prices')))
price_text = price_element.text

# Print the price
print(f"Price: {price_text}")

# Quit the WebDriver
driver.quit()

# Load the existing workbook
workbook = load_workbook('priceCheckerWorkBook.xlsx')

# Select the active sheet
worksheet = workbook.active

# Update cell values
worksheet['A2'] = "milk"
worksheet['B2'] = price_text

# Save the workbook
workbook.save('priceCheckerWorkBook.xlsx')

print("data saved")





