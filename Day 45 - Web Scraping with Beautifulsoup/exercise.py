# Beautiful Soup Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup
import requests

# with open("website.html" , encoding="utf8") as file:
#     contents = file.read()
#     # print(contents)
#
# soup = BeautifulSoup(contents, "html.parser") # Change the website into a class/object
#
# # print(soup.prettify()) # prints the html code
# # print(soup.title) # Prints the title of the website
# # print(soup.title.string) #Prints the string that is inside the title tag
#
# # all_anchor_tags = soup.find_all(name="a") # Returns a list of all anchor tags
# # # print(all_anchor_tags[1]) # you can specify which anchor tag using list placement []
# # for tag in all_anchor_tags:
# #     # print(tag.string) # Prints out all of the Link Names
# #     # print(tag.getText()) # Prints out all of the Link Names
# #     print(tag.get("href")) # Prints out all of the Link References
#
# # name_tag = soup.find(name="h1", id="name") # Prints out the tag with the id of name
# # print(name_tag)
#
# # section_heading = soup.find(name="h3", class_="heading") # Prints out the tag with the class of heading
# # # Use class_ instead of class because class is a reserved python word for making class objects
# # print(section_heading)
# # print(section_heading.getText())
# # print(section_heading.get("class"))
#
#
# # company_url = soup.select_one(selector="p a") # selects the first link inside of a paragraph
# # using css selectors
# # print(company_url)
#
# # name = soup.select_one(selector="#name") # selects the 1st tag with the id of name
# # print(name)
#
# heading = soup.select_one(selector=".heading") # selects the 1st tag with the class of heading
# print(heading)
#
# # second_list_item = soup.select(selector="li")[1] # selects all the li items and makes a list
# # # then using list notation selects the 2nd item in the list
# # print(second_list_item)


# ---------------- BeautifulSoup to grab a live website ----------------------- #

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

# if you right click on the points and on the title on hackernews you can get the following:
# the title is in a class called "storylink"
# the points are in a class called "score"

soup = BeautifulSoup(yc_web_page, "html.parser")

# print(soup.select_one(selector=".storylink").text)  # prints the title of the FIRST anchortag/article on hackernews
articles = soup.find_all(name="a", class_="storylink") # or use this way to print the title of the FIRST anchortag/article on hackernews
# print(article_tag.text)
# print(article_tag.getText()) # or this way

article_texts = []
article_links = []

# upvotes = soup.find_all(name="span", class_="score") # This will not work if there are no upvotes (a new article was just posted for example).
# So, you need to go to the higher level and pull a bigger section then test for the "score" field in that section.

article_upvotes = []
upvotes = soup.find_all(name="td", class_="subtext")
for article in upvotes:
    is_votes = article.find(name="span", class_="score")
    if is_votes is None:
        article_upvotes.append(0)
    else:
        article_upvotes.append(int(is_votes.string.split()[0]))

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)

    link = article_tag.get("href")
    article_links.append(link)




# print(article_texts)
# print(article_links)
# print(article_upvotes)

max_value = max(article_upvotes) # finds the highest upvoted
# print(max_value)
max_index = article_upvotes.index(max_value)
# print(max_index)


print(article_texts[max_index])
print(article_links[max_index])
print(f'{max_value} upvotes')
