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

try:
    r_all = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
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
        r_all[data_point.weekday].append(data_point.day_return)

    # Splitting R into R, R- and R+
    r_neg = [r for r in r_all["Monday"] if r < 0]
    r_pos = [r for r in r_all["Monday"] if r > 0]

    print("Total days: " + str(len(r_all["Monday"])))
    print("Negative Days: " + str(len(r_neg)))
    print("Positive Days: " + str(len(r_pos)))

    # Calculating the Means
    mean_r_all = sum(r_all["Monday"]) / len(r_all["Monday"])
    mean_r_neg = sum(r_neg) / len(r_neg)
    mean_r_pos = sum(r_pos) / len(r_pos)

    # Calculating the Standard Deviations
    standard_deviation_r_all = math.sqrt(
        sum([a * a for a in r_all["Monday"]]) / len(r_all["Monday"])
    ) - (mean_r_all * mean_r_all)
    standard_deviation_r_all = math.sqrt(
        sum([a * a for a in r_all["Monday"]]) / len(r_all["Monday"])
    ) - (mean_r_all * mean_r_all)
    standard_deviation_r_all = math.sqrt(
        sum([a * a for a in r_all["Monday"]]) / len(r_all["Monday"])
    ) - (mean_r_all * mean_r_all)

    print("Mean of daily returns: " + str(mean_r_all))
    print("Standard deviation: " + str(standard_deviation_r_all))

    data = {
        "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "µ(R)": ["1", "2", "3", "4", "5"],
        "σ(R)": ["1", "2", "3", "4", "5"],
        "|R−|": ["1", "2", "3", "4", "5"],
        "µ(R−)": ["1", "2", "3", "4", "5"],
        "σ(R−)": ["1", "2", "3", "4", "5"],
        "|R+|": ["1", "2", "3", "4", "5"],
        "µ(R+)": ["1", "2", "3", "4", "5"],
        "σ(R+)": ["1", "2", "3", "4", "5"],
    }

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

except Exception as e:
    print(e)
    print("failed to read stock data for ticker: ", ticker)
