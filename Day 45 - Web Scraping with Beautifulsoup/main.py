# Import the 100 Greatest Movies from empireonline.com and scrape the data
    # Due to changes on the website, the web page has been downloaded
    # Use the try, except, finally, function to import the file as Soup
# Scrape the title and number in numerical order, not listed order
# Write the data to a text file called "movies.txt"
# Data should look like the following:
# 1) The Godfather
# 2) The Empire Strikes Back
# 3) The Dark Knight
# etc.


# Beautiful Soup Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup
WEB_FILE = "./data/100_best_movies.html"


def read_web_file():
    try:
        open(WEB_FILE)
    except FileNotFoundError:
        print(f"You need to save the rendered HTML to {WEB_FILE}")
        exit()
    finally:
        # Read the web page from file
        with open(WEB_FILE, mode="r", encoding="utf-8") as file:
            contents = file.read()
        return BeautifulSoup(contents, "html.parser")

soup = read_web_file()


soup.find_all(name="h3", class_="jsx-4245974604")
# --- Inspect webpage for Title and number of movie ----#
# --- Using inspect on a title of a movie on the website, they appear to be inside of h3 tags --- #
# --- Lets create a list of all the h3 tags with a jsx-4245974604 class --- #
all_movies = soup.find_all(name="h3", class_="jsx-4245974604")
# print(movies)

movie_list = []
for movie in all_movies:
    # title = movie.getText().split(" ",1)  # splits the string 100) Stand by me into two parts, the number and then the rest of the title
    title = movie.getText()
    movie_list.append(title)

# --- movie titles are sorted in reverse numerical which is wrong, lets change that ----#
# ---use splice reverse method ----#
movies = movie_list[::-1]
print(movies)


# # --- Write List into a text file ----#
# with open("data/movies.txt", mode="w") as file:
#     for movie in movies:
#         file.write(f"{movie}\n")