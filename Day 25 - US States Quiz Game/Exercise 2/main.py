# fur, color, count
# 0,grey,2400
# 1,red,2450
# 2,black,300

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# color = data["Primary Fur Color"]
#
# color_list = color.to_list()
# gray =0
# black = 0
# cinn = 0
# red = 0
# nan = 0
# error = 0
# error_list = []
# for color in color_list:
#     if color == "Gray":
#         gray += 1
#     elif color == "Black":
#         black += 1
#     elif color == "Cinnamon":
#         cinn += 1
#     else:
#         error += 1
#         error_list.append(color)
# # print(error_list)
#
# data_dict = {
#     "color": ["Gray", "Cinnamon", "Black"],
#     "count": [gray, cinn, black],
# }
#
# # print(data_dict)
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("squirrel_count.csv")

gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "color": ["Gray", "Cinnamon", "Black"],
    "count": [gray_squirrels, cinnamon_squirrels, black_squirrels],
}

# print(data_dict)
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("squirrel_count.csv")