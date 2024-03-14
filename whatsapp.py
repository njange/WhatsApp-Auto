from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

# Replace with the path to your chromedriver executable
driver = webdriver.Chrome(r'C:\Users\HP 450 G7\Documents\Selenium\chromedriver-win64\chromedriver-win64')
driver = webdriver.Chrome(r'C:\Users\HP 450 G7\Documents\Selenium\chromedriver-win64\chromedriver.exe')

# Open WhatsApp Web
driver.get('https://web.whatsapp.com')

# Wait for the user to scan the QR code
# Create an instance of Options
options = Options()

# Replace with the path to your chromedriver executable
driver = webdriver.Chrome(r'C:\Users\HP 450 G7\Documents\Selenium\chromedriver-win64\chromedriver-win64', options=options)

# Find the message input field and send the message
message_input = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]')
message_input.send_keys(message)
message_input.send_keys(Keys.ENTER)

# Close the browser
driver.quit()