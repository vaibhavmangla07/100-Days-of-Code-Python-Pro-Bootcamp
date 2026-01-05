# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)
#
# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#          # print(row)
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])

data_to_dict = data.to_dict()
print(data_to_dict)

temp_list = data["temp"].to_list()
print(temp_list)

avg = sum(temp_list) / len(temp_list)
print(avg)

print(data["temp"].mean())  # to find the average or mean of the data
print(data["temp"].max())   # to find the maximum data entry

# To Get the data in column (both are same)
print(data["condition"])
print(data.condition)

# To get the data in row
print(data[data.day == "Monday"])

# To get the data of max temp
print(data[data.temp == data.temp.max()])

# How to convert the Celsius to Fahrenheit
monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Create a dataframe from the scratch
data_dict = {
    "Students" : ["Aman", "Harman", "Aryan"],
    "Scores" : [76, 68, 82]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")



