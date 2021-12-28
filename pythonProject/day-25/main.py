#with open("weather_data.csv") as data_file:
#    data = data_file.readlines()

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)


import pandas

data_2 = pandas.read_csv("weather_data.csv")
print(data_2)
print(data_2["temp"])

data_dict = data_2.to_dict()
print(data_dict)

temp_list = data_2["temp"].to_list()
print(temp_list)

print(data_2["temp"].mean())
print(data_2["temp"].max())

# Get data in colums
print(data_2["condition"])
print(data_2.condition)

# Get Data in row
print(data_2[data_2.day == "Monday"])
print(data_2.temp == data_2.temp.max())

monday = data_2[data_2.day == "Monday"]
monday_temp = int(monday.temp)

print(monday, monday_temp)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data_3 = pandas.DataFrame(data_dict)
print(data_3)
data_3.to_csv("new_data.csv")