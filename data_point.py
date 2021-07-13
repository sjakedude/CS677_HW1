"""
Jake Stephens
Class: CS 677 - Summer 2
Date: 7/13/2021
Homework #1
Description: This class is the model for 
each row in the table of the raw csv data 
from the yahoo finance API.
"""


class DataPoint:
    def __init__(
        self,
        date,
        year,
        month,
        day,
        weekday,
        week_number,
        year_week,
        open,
        high,
        low,
        close,
        volume,
        adj_close,
        day_return,
        short_ma,
        long_ma,
    ):
        self.date = date
        self.year = year
        self.month = month
        self.day = day
        self.weekday = weekday
        self.week_number = week_number
        self.year_week = year_week
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.adj_close = adj_close
        self.day_return = float(day_return)
        self.short_ma = short_ma
        self.long_ma = long_ma
