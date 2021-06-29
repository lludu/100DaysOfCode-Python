# --- Resources & Modules --- #
from p_data import *  # --- Sensitive Data Hidden
import requests
from datetime import datetime
#Datetime Documentation: https://docs.python.org/3/library/datetime.html

#Nutrition API by Nutritionix
##https://www.nutritionix.com/business/api
#Documentation:
#https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/preview

#Sheety # Connect Google Sheets
#https://sheety.co/


# TODO 1. Using the Nutritionix "Natural Language for Exercise" API Documentation,
#  figure out how to print the exercise stats for a plain text input.
# -- Connect with requests

exercise = {
 "query": input("Tell me what exercises you did: "),
 # "query": "cycled 5 miles and walked 20 minutes",
 "gender":"male",
 "weight_kg":106.594,  # 235
 "height_cm":190.5,  # 6f3
 "age":34
}


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise/"

exercise_response = requests.post(exercise_endpoint, json=exercise, headers=HEADERS_NUTRITIONIX)
# print(exercise_response.status_code)
data = exercise_response.json()  # all the exercises in the query
# print(data["exercises"])


#TODO 2.  Using the Sheety Documentation, write some code to use the Sheety API
# to generate a new row of data in your Google Sheet for each of the exercises
# that you get back from the Nutritionix API. The date and time columns should
# contain the current date and time from the Python datetime module.

# ---
today_date = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%X")

# --- Getting the sheety document
sheety_endpoint = "https://api.sheety.co/d3a9ec0c60e3a5627aec14151dc035d3/workoutTracking/workouts"
sheety_response = requests.get(sheety_endpoint)
# print(sheety_response.json())

for exercise in data["exercises"]:
 # print(exercise["name"])
 sheet_input = {
  "workout": {
    "date": today_date,
    "time": time_now,
    "exercise": exercise["name"].title(),
    "duration": exercise["duration_min"],
    "calories": exercise["nf_calories"],
  }
 }
 # print(sheet_input)
 sheety_response = requests.post(sheety_endpoint, json=sheet_input, headers=HEADERS_SHEETY)
 print(sheety_response.text)