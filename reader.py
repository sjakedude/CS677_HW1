# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:37:29 2018

@author: epinsky
this scripts reads your ticker file (e.g. MSFT.csv) and
constructs a list of lines
"""
from data_point import DataPoint
import os
import math
import pandas as pd


ticker = "SUN"
input_dir = r"D:\BU\Summer_01_2021\Homework_1\CS677_HW1\data\\"
ticker_file = os.path.join(input_dir, ticker + ".csv")
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


def calculate_table(r_all, year):
    data = {
        "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "µ(R)": [],
        "σ(R)": [],
        "|R−|": [],
        "µ(R−)": [],
        "σ(R−)": [],
        "|R+|": [],
        "µ(R+)": [],
        "σ(R+)": [],
    }

    # Looping through Monday - Friday
    for weekday in weekdays:

        # Splitting R into R, R- and R+
        r_neg = [r for r in r_all[weekday] if r < 0]
        r_pos = [r for r in r_all[weekday] if r > 0]

        # Calculating the Means
        mean_r_all = sum(r_all[weekday]) / len(r_all[weekday])
        mean_r_neg = sum(r_neg) / len(r_neg)
        mean_r_pos = sum(r_pos) / len(r_pos)

        # Calculating the Standard Deviations
        standard_deviation_r_all = math.sqrt(
            sum([(a - mean_r_all)**2 for a in r_all[weekday]]) / len(r_all[weekday])
        )
        standard_deviation_r_neg = math.sqrt(
            sum([(a - mean_r_neg)**2 for a in r_neg]) / len(r_neg)
        )
        standard_deviation_r_all = math.sqrt(
            sum([(a - mean_r_pos)**2 for a in r_pos]) / len(r_pos)
        )
        # Putting the data into the columns for that weekday
        data["µ(R)"].append(mean_r_all)
        data["σ(R)"].append(standard_deviation_r_all)
        data["|R−|"].append(len(r_neg))
        data["µ(R−)"].append(mean_r_neg)
        data["σ(R−)"].append(standard_deviation_r_neg)
        data["|R+|"].append(len(r_pos))
        data["µ(R+)"].append(mean_r_pos)
        data["σ(R+)"].append(standard_deviation_r_all)

    df = pd.DataFrame(
        data,
        columns=[
            "Day",
            "µ(R)",
            "σ(R)",
            "|R−|",
            "µ(R−)",
            "σ(R−)",
            "|R+|",
            "µ(R+)",
            "σ(R+)",
        ],
    )
    print(df)
    df.to_csv(year + ".csv", index=False)


def load_data_from_file(year):
    r = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
    with open(ticker_file) as f:
        lines = f.read().splitlines()
    for line in lines[1::]:
        tokens = line.split(",")
        data_point = DataPoint(
            tokens[0],
            tokens[1],
            tokens[2],
            tokens[3],
            tokens[4],
            tokens[5],
            tokens[6],
            tokens[7],
            tokens[8],
            tokens[9],
            tokens[10],
            tokens[11],
            tokens[12],
            tokens[13],
            tokens[14],
            tokens[15],
        )
        if data_point.year == year:
            r[data_point.weekday].append(data_point.day_return)
    return r


for year in ["2014", "2015", "2016", "2017", "2018"]:
    print("===================== " + year + " =====================")
    r = load_data_from_file(year)
    calculate_table(r, year)
