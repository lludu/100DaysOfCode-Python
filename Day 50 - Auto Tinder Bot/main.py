from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep
from p_data import *

# Make the path work by changing \ to /  --> This way is globally accepted on Mac and Linux, lets use this way
chrome_driver_path = CHROME_DRIVER_PATH

driver = webdriver.Chrome(executable_path=chrome_driver_path)  # initialize a new chrome browser object
driver.get(TINDER)





LOGIN_XPATH = driver.find_element_by_xpath('//*[@id="t-828363795"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
LOGIN_XPATH.click()
sleep(5)

LOGIN_FB_XPATH = driver.find_element_by_xpath('//*[@id="t1738222425"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
LOGIN_FB_XPATH.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

sleep(5)
FB_EMAIL_XPATH = driver.find_element_by_name('email')
FB_PASS_XPATH = driver.find_element_by_name('pass')
FB_LOGIN_BTN = driver.find_element_by_name('login')

FB_EMAIL_XPATH.send_keys(EMAIL)
FB_PASS_XPATH.send_keys(PASS)
FB_LOGIN_BTN.click()

sleep(5)
driver.switch_to.window(base_window)
print(driver.title)

TINDER_ALLOW_BTN = driver.find_element_by_xpath('//*[@id="t1738222425"]/div/div/div/div/div[3]/button[1]/span') # Allow Button
TINDER_ALLOW_BTN.click()
sleep(2)
TINDER_NOTIFICATION_BTN = driver.find_element_by_xpath('//*[@id="t1738222425"]/div/div/div/div/div[3]/button[2]/span')  #Not Interested Button
TINDER_NOTIFICATION_BTN.click()
sleep(2)
TINDER_ACCEPT_COOKIE = driver.find_element_by_xpath('//*[@id="t-828363795"]/div/div[2]/div/div/div[1]/button/span') # Accept Cookies
TINDER_ACCEPT_COOKIE.click()
sleep(2)

# TINDER_LIKE_BTN = driver.find_element_by_xpath('//*[@id="t-828363795"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button/span/span')



# buttons = driver.find_elements_by_tag_name('button')
# button_list = []
# for button in buttons:
#     button_list.append(button.text)
#
# print(button_list)
# Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    #Add a 1 second delay between likes.
    sleep(1)

    try:
        print("called")
        # # like_button = driver.find_element_by_xpath(
        # #     '//*[@id="t-828363795"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button/span/span/svg/path    ')
        # like_button.click()
        body = driver.find_element_by_css_selector('body')
        body.send_keys(Keys.RIGHT)

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

