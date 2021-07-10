from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # Imports keys like "enter" and "shift" etc so we can access them
import time



# Make the path work by changing \ to /  --> This way is globally accepted on Mac and Linux, lets use this way
chrome_driver_path = "C:/Users/lludu/Documents/CodingWork/Portfolio/100DaysOfCode -Python/Day 48 - Selenium and Game Bot/chrome_driver/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)  # initialize a new chrome browser object
driver.get("http://orteil.dashnet.org/experiments/cookie/")  # opens new browser window with the url specified

cookie = driver.find_element_by_id("cookie")


timeout = time.time() + 5
five_min = time.time() + 300

while True:
    cookie.click()

    if time.time() > timeout:
        price = driver.find_elements_by_css_selector("div b")
        list1 = [item.text for item in price]
        products = [item.split("-") for item in list1[10:17]]
        prices = [item[-1].strip().replace(",", "") for item in products]
        money = driver.find_element_by_id("money")
        for item in prices[::-1]:
            if money.text.replace(",", "") > item:
                index = prices.index(item)
                if index == 7:
                    price[17].click()
                elif index == 6:
                    price[16].click()
                elif index == 5:
                    price[15].click()
                elif index == 4:
                    price[14].click()
                elif index == 3:
                    price[13].click()
                elif index == 2:
                    price[12].click()
                else:
                    pass
        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break



# driver.close()  # closes the active tab (single tab)
# driver.quit()   # completely quits Chrome