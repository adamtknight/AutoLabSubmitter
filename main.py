import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from latestFileFinder import findLatestFile
import autoit as auto





#driver to control chrome
driver = webdriver.Chrome('C:/Users/adamk/Documents/ChromeDriverApp/chromedriver.exe')  # Optional argument, if not specified will search path.

#get to my course on gradescope
driver.get('https://www.gradescope.com');
time.sleep(5) # Let the user actually see something!

#my username and password
email = 'USERNAME'
password = 'PASSWORD'

#sign into gradescope
driver.implicitly_wait(20) 
driver.find_element_by_id("session_email").send_keys(email)
driver.find_element_by_id ("session_password").send_keys(password)
driver.find_element_by_name('commit').click()

# time.sleep(5) # Let the user actually see something!

#method that finds latest file in my lab submit directory
latestFile = findLatestFile()

#A few button clicks to find the right place to submit the file
driver.implicitly_wait(20) 
driver.find_element_by_xpath("//*[@id='assignments-student-table']/tbody/tr[1]/th/a").click()

driver.implicitly_wait(20) 
driver.find_element_by_xpath("//*[@id='actionBar']/ul/li[5]/button").click()

driver.implicitly_wait(20) 
driver.find_element_by_xpath("//*[@id='submit-variable-length-pdf']/i").click()


#click to submit file
driver.implicitly_wait(20) 
driver.find_element_by_xpath("//*[@id='submit-fixed-length-form']/div[1]/label/span[2]/span").click()

#more direct non-browser controller to sumit correct file
auto.win_wait_active("Open")
auto.send("C:\\Users\\adamk\\Documents\\Chem269\\submitLab\\" + latestFile)
auto.send("{ENTER}")

#submit the file sucessfully, USER can review
driver.implicitly_wait(20) 
driver.find_element_by_xpath("//*[@id='submit']").click()








