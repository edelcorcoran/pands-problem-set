
# Edel Corcoran Question 8 Problem Set 2019

# Write a program that outputs today's date.

# References: Week 6 lecture videos, https://docs.python.org/3/library/datetime.html?highlight=datetime

import datetime as dt
dt.datetime.now()

dt.datetime.strftime(dt.datetime.now(), "%A  %B %d %Y at %H:%M %p")

