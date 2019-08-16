import os
from selenium import webdriver

import unittest

from selenium.webdriver.common.keys import Keys

# get the path of ChromeDriverServer
dir = os.path.dirname(__file__)
chrome_driver_path =dir + "/Drivers/chromedriver.exe"

# create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(30)
driver.maximize_window()
# Navigate to the application home page
driver.get("https://outlook.office365.com/mail/inbox")

''''
sign_in_button = driver.find_element_by_link_text("https://outlook.live.com/owa/#")
sign_in_button.click()
'''
# get the search textbox
search_field = driver.find_element_by_name("loginfmt")
# enter search keyword and submit
search_field.send_keys("jose.rivera7@ramajudicial.pr")
#search_field.submit()
next_button = driver.find_element_by_id("idSIButton9")
next_button.click()
#login_button = driver.find_element_by_id("idp_submit")
new_message_button = driver.find_element_by_id("id__3")
new_message_button.click()
recipient_field = driver.find_element_by_class_name("ms-BasePicker-input")
recipient_field.send_keys("jose.rivera7@ramajudicial.pr")
subject_field = driver.find_element_by_id("subjectLine0")
subject_field.send_keys( "Email escrito desde Selenium")
send_button = driver.find_element_by_id("id__267")
send_button.click()

# get the list of elements which are displayed after the search
# currently on result page using find_elements_by_class_name method
'''
lists= driver.find_elements_by_class_name("r")
'''
# get the number of elements found
'''
print ("Found " + str(len(lists)) + " searches:")
'''
# iterate through each element and print the text that is
# name of the search
'''i=0
for listitem in lists:
   print (listitem.get_attribute("innerHTML"))
   i=i+1
   if(i>10):
      break
'''


# close the browser window
driver.quit()

