from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # Imports keys like "enter" and "shift" etc so we can access them

# Todo Use Selenium to print the total number of articles from the wiki homepage to the console

# Make the path work by changing \ to /  --> This way is globally accepted on Mac and Linux, lets use this way
chrome_driver_path = "C:/Users/lludu/Documents/CodingWork/Portfolio/100DaysOfCode -Python/Day 48 - Selenium and Game Bot/chrome_driver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)  # initialize a new chrome browser object

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count =driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
print(article_count.text)
# article_count.click()

portals = driver.find_element_by_link_text("All portals")
# portals.click()

search = driver.find_element_by_name("search")
search.send_keys("Python")  # Types "Python" in the search box
search.send_keys(Keys.ENTER)


# driver.quit()