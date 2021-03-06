from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # Imports keys like "enter" and "shift" etc so we can access them
import time
from p_data import *

# Make the path work by changing \ to /  --> This way is globally accepted on Mac and Linux, lets use this way
chrome_driver_path = "C:/Users/lludu/Documents/CodingWork/Portfolio/100DaysOfCode -Python/Day 48 - Selenium and Game Bot/chrome_driver/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)  # initialize a new chrome browser object
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=105608603&keywords=python%20developer&location=Lancaster%2C%20Pennsylvania%2C%20United%20States")  # opens new browser window with the url specified


ACCOUNT_EMAIL = MY_EMAIL
ACCOUNT_PASSWORD = MY_PASSWORD
PHONE = MY_PHONE

time.sleep(2)
sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

time.sleep(5)
email_field = driver.find_element_by_id("username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(5)

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()

        time.sleep(5)
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element_by_css_selector("footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()

            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()

