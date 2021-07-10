from selenium import webdriver

#This causes an error using a normal string as a path:
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
# chrome_driver_path = "C:\Users\lludu\Documents\CodingWork\Portfolio\100DaysOfCode -Python\Day 48 - Selenium and Game Bot\chrome_driver\chromedriver.exe"

#Make the path work by making it a raw string
# chrome_driver_path = r"C:\Users\lludu\Documents\CodingWork\Portfolio\100DaysOfCode -Python\Day 48 - Selenium and Game Bot\chrome_driver\chromedriver.exe"

#Make the path work by using double \\ to fix the "escaped characters" in the string
# chrome_driver_path = "C:\\Users\\lludu\\Documents\\CodingWork\\Portfolio\\100DaysOfCode -Python\\Day 48 - Selenium and Game Bot\\chrome_driver\\chromedriver.exe"

# Make the path work by changing \ to /  --> This way is globally accepted on Mac and Linux, lets use this way
chrome_driver_path = "C:/Users/lludu/Documents/CodingWork/Portfolio/100DaysOfCode -Python/Day 48 - Selenium and Game Bot/chrome_driver/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)  # initialize a new chrome browser object
driver.get("https://www.python.org")  # opens new browser window with the url specified

# --- Find element by ID --- #
# price = driver.find_element_by_id("priceblock-ourprice")
# print(price.text)

# --- Find element by name --- #
# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# --- Find element by class name --- #
# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# --- Find element by css selector --- #
# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

# --- Find element by xPath --- #
# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# Todo Extract the upcoming event data from the python.org website. Use selenium to
#  scrape all upcoming event dates and event names and store them in a nested Python
#  dictionary. Print the dictionary to the console. The event data from python.org
#  should be stored under the keys "time" and "name".


# --- Get Event Times by css selector --- #
event_times = driver.find_elements_by_css_selector(".event-widget time") #returns selenium objects
# print(event_times)
# times = []
# for time in event_times:
#     times.append(time.text)
# print(times)

# --- Get Event Names by css selector --- #
event_links = driver.find_elements_by_css_selector(".event-widget li a") #returns selenium objects
# print(event_times)
# links = []
# for link in event_links:
#     links.append(link.text)
# print(links)

# new_dictionary = {new_key:new_value for (key,value) in dictionary_name.items() if test}
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_links[n].text,
    }

print(events)













# driver.close()  # closes the active tab (single tab)
driver.quit()   # completely quits Chrome