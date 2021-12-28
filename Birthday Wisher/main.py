
"""
import smtplib

my_email = "testcodepythonemail@gmail.com"
password = "testCode1234++"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="testcodepythonemail@gmail.com",
                        msg="Subject:Email from python code\n\nHello to myself")

"""
"""
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(f"Day of week number from 0 to 6 which mean Monday[0],Tuesday[1].. etc.. {day_of_week}")
if year == 2021:
    print("YEAR 2021")
print(now)

date_of_birth = dt.datetime(year=1999, month=12, day=1)
print(date_of_birth)

"""

import smtplib
import datetime as dt
import random

my_email = "testcodepythonemail@gmail.com"
password = "testCode1234++"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="testcodepythonemail@gmail.com",
                            msg=f"Subject:Monday Motivation\n\n{quote}")

