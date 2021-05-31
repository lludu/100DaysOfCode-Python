#This is day 9, Dictionaries dand Nesting Dictionaries

#Exercise 2 - Countries Visited

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(add_country,add_visits, add_cities):
  new_country = {}

  new_country["country"] = add_country
  new_country["visits"] = add_visits
  new_country["cities"] = add_cities

  travel_log.append(new_country)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


#Link to Exercise
# https://replit.com/@Lludu/day-9-2-exercise#main.py

#link to Exercise Checker
# https://replit.com/@Lludu/day-9-2-test-your-code#main.py
