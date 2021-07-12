from p_data import *
from selenium import webdriver
from time import sleep




class InternetSpeedTwitterBot:
    """Goes to Speedtest.net and checks internet speeds"""
    def __init__(self, driver_path):
        self.up = 0
        self.down = 0
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def get_internet_speeds(self):
        speed_website = 'https://www.speedtest.net/'
        self.driver.get(speed_website)

        sleep(3)
        press_go = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        press_go.click()

        sleep(60)
        ping = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        print(f'The Ping Is: {ping}')
        print(f'Download Speeds at: {self.up} Mbps, Upload Speeds at: {self.down} Mbps')

    def tweet_at_provider(self):
        sleep(10)
        twitter = 'https://twitter.com/login'
        self.driver.get(twitter)

        sleep(3)
        email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        pword = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        login = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')

        email.send_keys(EMAIL)
        pword.send_keys(PASS)
        login.click()

        sleep(3)
        tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(f'Amish Internet Stats Today:  Download Speeds at: {self.up} Mbps, Upload Speeds at: {self.down} Mbps')

        tweet_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_btn.click()

        sleep(2)
        self.driver.quit()



bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speeds()
bot.tweet_at_provider()

