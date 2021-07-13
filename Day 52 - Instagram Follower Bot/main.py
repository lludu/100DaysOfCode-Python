from p_data import *
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep





class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def login(self):
        login_page = 'https://www.instagram.com/accounts/login/'
        self.driver.get(login_page)

        #----- Login -----#
        sleep(3)
        uname = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        pword = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        login_btn = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
        uname.send_keys(USERNAME)
        pword.send_keys(PASSWORD)
        login_btn.click()

        sleep(3)
        not_now_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now_btn.click()

        no_notify = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        no_notify.click()







    def find_followers(self):
        following_page = 'https://www.instagram.com/' + SIMILIAR_ACCOUNT
        self.driver.get(following_page)

        sleep(2)
        followers_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers_btn.click()

        sleep(2)
        # ---- https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
        modal = self.driver.find_element_by_xpath("//div[@Class='isgrP']")
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)


    def follow(self):
        follow = self.driver.find_elements_by_css_selector(".isgrP button")
        for button in follow:
            try:
                button.click()
            except ElementClickInterceptedException:
                cancel_btn = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_btn.click()
            finally:
                sleep(1)




bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
