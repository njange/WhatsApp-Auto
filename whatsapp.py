from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium import webdriver

# Specify the path to the chromedriver.exe
chrome_driver_path = "C:\Users\HP 450 G7\Documents\Selenium\chromedriver-win64\chromedriver-win64\chromedriver.exe"  # replace with the actual path
chrome_driver_path = "C:\\Users\\HP 450 G7\\Documents\\Selenium\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

# Create the webdriver instance
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Replace with the path to your chromedriver executable
# Replace with the path to your chromedriver executable
driver_path = r'C:\Users\HP 450 G7\Documents\Selenium\chromedriver-win64\chromedriver.exe'

# Create an instance of Service
service = Service(driver_path)

# Create an instance of Options
options = Options()

# Set the path to the chromedriver executable
options.binary_location = driver_path

# Create the webdriver instance
driver = webdriver.Chrome(service=service, options=options)

# Open WhatsApp Web
driver.get('https://web.whatsapp.com')

# Wait for the user to scan the QR code
# Find the message input field and send the message
message_input = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]')

# Send the message
message_input.send_keys(message)
message_input.send_keys(Keys.ENTER)

# Close the browser
driver.quit()