from statistics import mean

# # # --------------------------------CONVERTING DATA INTO TEMPERATURE LIST------------------ # # #
# ---- Normal Python Method--- #
# open weather_data.csv and store each line in a list
# weather_days_list = []
# with open("weather_data.csv") as weather_data_file:
#     weather_data = weather_data_file.readlines()
#     for day in weather_data:
#         stripped_day = day.strip()
#         weather_days_list.append(stripped_day)
# print(weather_days_list)

# ---- Python's CSV Module Method --- #
# open weather_data.csv and store each line in a list using import CSV Module
# import csv
# with open("weather_data.csv") as weather_data_file:
#     weather_data = csv.reader(weather_data_file)
#     # print(weather_data) # returns a csv object that can be looped through
#     temperatures = []
#     # for row in weather_data:
#     #     print(row) # prints each row as type=list
#     next(weather_data) # Skips the first line of the file
#     for row in weather_data:
#         # instead of next(weather_data) can also use -> if row[1] != "temp":
#         temperatures.append(int(row[1]))
#     print(temperatures)

# ---- PANDA's MODULE METHOD --- #
import pandas  # this has to be installed
# API reference --- https://pandas.pydata.org/docs/reference/index.html A
# pandas documentation --- https://pandas.pydata.org/docs/

data = pandas.read_csv("weather_data.csv") #Pandas store data in table format
# print(data["temp"]) # prints the temp row in the data table that pandas made

# temp_list = list(data["temp"]) # converts to list using python's list method
temp_list = data["temp"].to_list()
temp_list2 = data.temp.to_list()  # you can also use attribute dot notation instead of brackets
# print(temp_list)



# # # --------------------------------AVERAGE TEMPERATURE ------------------ # # #
# average_temp_2 = sum(temp_list) / len(temp_list)  #python's built in module
# average_temp_3 = mean(temp_list) # using imported statistics module
# average_temp = data["temp"].mean() # panda's built in module
# print(average_temp, average_temp_2, average_temp_3)

# # # --------------------------------MAX TEMPERATURE ------------------ # # #
# max_temp = data.temp.max()
# print(max_temp)

# # # --------------------------------Get Data in Row in Pandas ------------------ # # #
# monday_data = data[data.day == "Monday"]  #pulls out the row that equals to monday
# print(monday_data)


# # # # --------------------------------Get Data Row from when temp was max ------------------ # # #
# highest_temp_day = data[data.temp == data.temp.max()]
# print(highest_temp_day)

# # # # --------------------------------Get single value from data row  ------------------ # # #
# print(data[data.day == "Monday"].condition)
# or
# monday = data[data.day == "Monday"]
# print(monday.condition)

# # # # --------------------------------Convert temp from data to fahrenheit  ------------------ # # #
# fahrenheit = (celsius * 9/5) + 32
# monday = data[data.day == "Monday"]
# cel = int(monday.temp) # convert the panda data into a normal int
# fah = (cel * 9/5) + 32
# print(f"Monday's Temperature was {cel} degrees celsius, that is {fah} degrees Fahrenheit")


# # # # --------------------------------Create a dataframe from scratch  ------------------ # # #
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)

# # # # --------------------------------Create a dataframe from scratch and save a CSV  ------------------ # # #
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")