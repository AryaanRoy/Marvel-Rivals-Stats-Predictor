import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

#Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = 'https://www.marvelrivals.com/heroes_data/'

# Opening the webpage
driver.get(url)

# Wait for the page to load
driver.implicitly_wait(10)

#1. Click the 'COMPETITIVE' button
competitive_button = driver.find_element(By.XPATH, '//div[@class="djms-btn-item" and text()="COMPETITIVE"]')
competitive_button.click()

# Waiting
time.sleep(2)

#2. Wait for the dropdown to turn into 'cur'
dropdown_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//div[@class="dan-con show"]'))
)

#3. Click on the dropdown to open it
ActionChains(driver).move_to_element(dropdown_button).click().perform()

# Waiting
time.sleep(1)

#4. Select 'Grandmaster and Above' option by the span text
grandmaster_option = driver.find_element(By.XPATH, '//span[@class="dan-txt" and text()="Grandmaster and Above"]')
grandmaster_option.click()

# Waiting
time.sleep(2)

# Scraping the data
role_elements1 = driver.find_elements(By.CLASS_NAME, 'role-name-txt')
role_elements2 = driver.find_elements(By.CLASS_NAME, 'role-type-con')
role_elements3 = driver.find_elements(By.CLASS_NAME, 'appearance-rate-num')
role_elements4 = driver.find_elements(By.CLASS_NAME, 'winning-rate-num')

# Creating a CSV file to store the data
with open('heroes_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Header row
    writer.writerow(['Character Name', 'Character Type', 'Pick Rate', 'Win Rate'])
    
    # Writing each line
    for i in range(len(role_elements1)):
        try:
            character_name = role_elements1[i].text
            character_type = role_elements2[i].text
            pick_rate = role_elements3[i].text
            win_rate = role_elements4[i].text
            writer.writerow([character_name, character_type, pick_rate, win_rate])
        except Exception as e:
            print(f"Error extracting data: {e}")

# Closing browser at end
driver.quit()
