
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # Imports keys like "enter" and "shift" etc so we can access them


# Make the path work by changing \ to /  --> This way is globally accepted on Mac and Linux, lets use this way
chrome_driver_path = "C:/Users/lludu/Documents/CodingWork/Portfolio/100DaysOfCode -Python/Day 48 - Selenium and Game Bot/chrome_driver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)  # initialize a new chrome browser object

driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element_by_name("fName")
lname = driver.find_element_by_name("lName")
em = driver.find_element_by_name("email")
button = driver.find_element_by_tag_name("button")

fname.send_keys("Andrew")
lname.send_keys("Ash")
em.send_keys("lludu@live.com")
button.click()