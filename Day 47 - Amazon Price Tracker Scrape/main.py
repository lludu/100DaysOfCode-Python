import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
from p_data import *


# Todo 1. Find a product on Amazon that you want to track and get the product URL
#  Ryobi Chainsaw: https://www.amazon.com/Ryobi-Baretool-Brushless-Lithium-Ion-Cordless/dp/B07P2P49Z1/ref=sr_1_3?dchild=1&keywords=ryobi+40v+chainsaw&qid=1625858983&sr=8-3


# Todo 2. Use the requests library to request the HTML page of the Amazon product using the URL you got from 1.
url = "https://www.amazon.com/Ryobi-Baretool-Brushless-Lithium-Ion-Cordless/dp/B07P2P49Z1/ref=sr_1_3?dchild=1&keywords=ryobi+40v+chainsaw&qid=1625858983&sr=8-3"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=header)
# print(response.status_code)
# print(response.text)

# # Todo 3. Use BeautifulSoup to make soup with the web page HTML you get back. You'll need to use the "lxml" parser instead of the "html.parser" for this to work.
soup = BeautifulSoup(response.content, "lxml")  # cant use html parser on amazon, install lxml parser instead
# print(soup.prettify())



# Todo 4. Use BeautifulSoup to get hold of the price of the item as a floating point number and print it out.
#  HINT: You might need to use the split() method: https://www.w3schools.com/python/ref_string_split.asp
#  <span id="priceblock_ourprice" class="a-size-medium a-color-price priceBlockBuyingPriceString">$178.66</span>
price = soup.find(id="priceblock_ourprice").getText() # Returns the price as a string '$178.66'
price_float = float(price.split("$")[1]) #Removes the "$" and converts digits to float
print(price_float)


# Todo 5. We want to get an email when the price of our product is below a certain value. e.g in the case of the Instant Pot, we'll set the target price as $100.
#    So when the price is below 100 then use the smtp module to send an email to yourself. In the email, include the title of the product, the current price and a link to buy the product.

title = soup.find(id="productTitle").get_text().strip()
print(title)

watch_price = 140

if price_float < watch_price:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=MAIN_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )

    print("There is a deal, but check with Home Depot")

else:
    print("No Deal Currently")