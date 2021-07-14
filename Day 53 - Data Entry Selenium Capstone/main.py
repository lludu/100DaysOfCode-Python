from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from p_data import *

URL = ZILLOW_LINK

FORM = FORM_ADDRESS

header = {
    "User-Agent": "Defined",
    "Accept-Language": "en-US,en;q=0.9,fr-CA;q=0.8,fr;q=0.7"

}
response = requests.get(URL, headers=header)  # using headers is important,otherwise the GET request won't work
data = response.text

soup = BeautifulSoup(data, "html.parser")  # creates BeautifulSoup object
all_prices_elements = soup.select(".list-card-price")  # scrapes all the elements containing the prices
all_address_elements = soup.select(".list-card-info address")  # scrapes all the elements containing the addresses
all_links_elements = soup.select(".list-card-top a")  # # scrapes all the elements containing the links to the listings

print(len(all_prices_elements))
print(len(all_address_elements))
print(len(all_links_elements))

prices_list = []
address_list = []
links_list = []

for price_tag in all_prices_elements:
    price = price_tag.getText()
    if "/" in price:
        price = price.split("/")[0]
        prices_list.append(price)
    elif "+" in price:
        price = price.split("+")[0]
        prices_list.append(price)

address_list = [address.getText().split(" | ")[-1] for address in all_address_elements]

for url in all_links_elements:
    card_link = str(url.get("href"))  # get the content inside the href attribute
    if not card_link.startswith("https"):  # if the url scrapped is incomplete
        link = 'https://www.zillow.com' + card_link
        links_list.append(link)
    else:
        links_list.append(card_link)

chrome_driver = CHROME_DRIVER_PATH

driver = webdriver.Chrome(executable_path=chrome_driver)

for n in range(len(all_links_elements)):
    driver.get(FORM)
    time.sleep(5)
    address_field = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div["
                                                 "1]/div/div[ "
                                                 "1]/input")
    address_field.send_keys(address_list[n])

    price_field = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div["
                                               "1]/div/div[1]/input")
    price_field.send_keys(prices_list[n])

    link_field = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div["
                                              "1]/div/div[1]/input")
    link_field.send_keys(links_list[n])

    submit_button = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div/div/span")
    submit_button.click()