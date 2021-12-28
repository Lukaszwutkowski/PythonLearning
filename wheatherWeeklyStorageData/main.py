def add_new_wheather_info():
    # chose = input("Which day of week you want to chose?").lower()
    if chose == "monday":
        precipitation = input("Precipitation rate in mm: ")
        wind_gust = input("Wind gust in m/s: ")
        temperature_now = input("Temperature in Celcius grade: ")
        week_days["Monday"].update({"rain": precipitation, "wind": wind_gust, "temperature": temperature_now})
    elif chose == "tuesday":
        precipitation = input("Precipitation rate in mm: ")
        wind_gust = input("Wind gust in m/s: ")
        temperature_now = input("Temperature in Celcius grade: ")
        week_days["Tuesday"].update({"rain": precipitation, "wind": wind_gust, "temperature": temperature_now})
    elif chose == "wednesday":
        precipitation = input("Precipitation rate in mm: ")
        wind_gust = input("Wind gust in m/s: ")
        temperature_now = input("Temperature in Celcius grade: ")
        week_days["Wednesday"].update({"rain": precipitation, "wind": wind_gust, "temperature": temperature_now})
    elif chose == "thursday":
        precipitation = input("Precipitation rate in mm: ")
        wind_gust = input("Wind gust in m/s: ")
        temperature_now = input("Temperature in Celcius grade: ")
        week_days["Thursday"].update({"rain": precipitation, "wind": wind_gust, "temperature": temperature_now})
    elif chose == "friday":
        precipitation = input("Precipitation rate in mm: ")
        wind_gust = input("Wind gust in m/s: ")
        temperature_now = input("Temperature in Celcius grade: ")
        week_days["Friday"].update({"rain": precipitation, "wind": wind_gust, "temperature": temperature_now})
    elif chose == "saturday":
        precipitation = input("Precipitation rate in mm: ")
        wind_gust = input("Wind gust in m/s: ")
        temperature_now = input("Temperature in Celcius grade: ")
        week_days["Saturday"].update({"rain": precipitation, "wind": wind_gust, "temperature": temperature_now})
    elif chose == "sunday":
        precipitation = input("Precipitation rate in mm: ")
        wind_gust = input("Wind gust in m/s: ")
        temperature_now = input("Temperature in Celcius grade: ")
        week_days["Sunday"].update({"rain": precipitation, "wind": wind_gust, "temperature": temperature_now})


week_days = {
    "Monday": {"rain": 0.0, "wind": 0.0, "temperature": 0.0},
    "Tuesday": {"rain": 0.0, "wind": 0.0, "temperature": 0.0},
    "Wednesday": {"rain": 0.0, "wind": 0.0, "temperature": 0.0},
    "Thursday": {"rain": 0.0, "wind": 0.0, "temperature": 0.0},
    "Friday": {"rain": 0.0, "wind": 0.0, "temperature": 0.0},
    "Saturday": {"rain": 0.0, "wind": 0.0, "temperature": 0.0},
    "Sunday": {"rain": 0.0, "wind": 0.0, "temperature": 0.0}
}

name_of_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
num = 0

for num in range(0, 7):
    print(name_of_days[num])
    chose = name_of_days[num].lower()
    add_new_wheather_info()
    num += 1

print(week_days)

# 2.2 b svar
rain = []
wind = []
temperature = []

for rain_data in week_days:
    rain.append(week_days[rain_data]["rain"])

for wind_data in week_days:
    wind.append(week_days[wind_data]["wind"])

for temperature_data in week_days:
    temperature.append(week_days[temperature_data]["temperature"])

print(rain, wind, temperature)

float_rain_map = map(float, rain)
float_rain_list = list(float_rain_map)

float_wind_map = map(float, wind)
float_wind_list = list(float_wind_map)

float_temp_map = map(float, temperature)
float_temp_list = list(float_temp_map)


def avg_data():
    avg_rain = sum(float_rain_list) / len(float_rain_list)
    avg_wind = sum(float_wind_list) / len(float_wind_list)
    avg_temp = sum(float_temp_list) / len(float_temp_list)
    print(
        f"The average precipitation rate in mm: {round(avg_rain, 2)}\nThe average wind gust in m/s: {round(avg_wind, 2)}\nThe average temperature in Celcius: {round(avg_temp, 2)}")


# 2.2 b svar
rain = []
wind = []
temperature = []

for rain_data in week_days:
    rain.append(week_days[rain_data]["rain"])

for wind_data in week_days:
    wind.append(week_days[wind_data]["wind"])

for temperature_data in week_days:
    temperature.append(week_days[temperature_data]["temperature"])

print(rain, wind, temperature)

float_rain_map = map(float, rain)
float_rain_list = list(float_rain_map)

float_wind_map = map(float, wind)
float_wind_list = list(float_wind_map)

float_temp_map = map(float, temperature)
float_temp_list = list(float_temp_map)


def avg_data():
    avg_rain = sum(float_rain_list) / len(float_rain_list)
    avg_wind = sum(float_wind_list) / len(float_wind_list)
    avg_temp = sum(float_temp_list) / len(float_temp_list)
    print(
        f"The average precipitation rate in mm: {round(avg_rain, 2)}\nThe average wind gust in m/s: {round(avg_wind, 2)}\nThe average temperature in Celcius: {round(avg_temp, 2)}")

def wind_over_ten_ms():
    wind = []
    for day in week_days:
        if float(week_days[day]["wind"]) > 10:
            wind.append(day)
    return wind

def temperature_lower_then_five_grades():
    temp = []
    for day in week_days:
        if float(week_days[day]["temperature"]) < 5:
            temp.append(day)
    return temp

def rain_over_one_mm():
    rain = []
    for day in week_days:
        if float(week_days[day]["rain"]) > 1:
            rain.append(day)
    return rain

avg_data()
print(f"Days where there was wind over 10 m/s: {wind_over_ten_ms()}")
print(f"Days where there was rain over 1 mm: {rain_over_one_mm()}")
print(f"Days where there was temperature lower then 5 Celcius grades: {temperature_lower_then_five_grades()}")