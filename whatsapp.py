from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Replace with the path to your chromedriver executable
driver = webdriver.Chrome('C:\Users\HP 450 G7\Documents\Selenium\chromedriver-win64\chromedriver-win64')

# Open WhatsApp Web
driver.get('https://web.whatsapp.com')

# Wait for the user to scan the QR code
input('Press Enter after scanning QR code...')

# Replace 'Friend's Name' with the name of your friend or group
friend_name = 'Friend\'s Name'

# Replace 'Message' with the message you want to send
message = 'Message'

# Find the search input field and search for the friend or group
search_input = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
search_input.send_keys(friend_name)
search_input.send_keys(Keys.ENTER)

# Wait for the chat to load
time.sleep(2)

# Find the message input field and send the message
message_input = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]')
message_input.send_keys(message)
message_input.send_keys(Keys.ENTER)

# Close the browser
driver.quit()