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

ticker = "SUN"
input_dir = r"D:\BU\Summer_01_2021\Homework_1\CS677_HW1\data\\"
ticker_file = os.path.join(input_dir, ticker + ".csv")
ticker_file_spy = os.path.join(input_dir, "SPY.csv")
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
full_dataset = []


def calculate_data(r_all):
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
            sum([(a - mean_r_all) ** 2 for a in r_all[weekday]]) / len(r_all[weekday])
        )
        standard_deviation_r_neg = math.sqrt(
            sum([(a - mean_r_neg) ** 2 for a in r_neg]) / len(r_neg)
        )
        standard_deviation_r_all = math.sqrt(
            sum([(a - mean_r_pos) ** 2 for a in r_pos]) / len(r_pos)
        )
        # Putting the data into the columns for that weekday
        data["µ(R)"].append(round(mean_r_all, 4))
        data["σ(R)"].append(round(standard_deviation_r_all, 4))
        data["|R−|"].append(len(r_neg))
        data["µ(R−)"].append(round(mean_r_neg, 4))
        data["σ(R−)"].append(round(standard_deviation_r_neg, 4))
        data["|R+|"].append(len(r_pos))
        data["µ(R+)"].append(round(mean_r_pos, 4))
        data["σ(R+)"].append(round(standard_deviation_r_all, 4))
    return data


def load_data_from_file(year, file):
    r = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
    r_basic = []
    with open(file) as f:
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
        full_dataset.append(data_point)
        if data_point.year == year:
            r[data_point.weekday].append(data_point.day_return)
        if year == "ALL":
            r[data_point.weekday].append(data_point.day_return)
        if year == "ALL-NOWEEKDAY":
            r_basic.append(data_point.day_return)
    if len(r_basic) > 0:
        return r_basic
    return r


# Prints table in comma separated format to port to CSV
def print_table(data):
    for i in data:
        print(i, end=",")
    print()
    for i in range(5):
        for key in data.keys():
            print(data[key][i], end=",")
        print()


# ======================
# Main program execution
# ======================
print("=======================")
print("QUESTION 1")
print("=======================")
print("SUN TABLES")

# Calculating and printing out the 5 tables
for year in ["2016", "2017", "2018", "2019", "2020"]:
    print("===================== " + year + " =====================")
    r = load_data_from_file(year, ticker_file)
    data = calculate_data(r)
    print_table(data)

# Total Gains and Losses
total_loss = 0
total_gain = 0

print("=======================")
print("Total Gains")

for day in full_dataset:
    if day.day_return > 0:
        total_gain = total_gain + day.day_return
    else:
        total_loss = total_loss + day.day_return

print("Total gains: " + str(total_gain))
print("Total losses: " + str(abs(total_loss)))

print("=======================")
print("Total Gains (Per Weekday)")
print("=======================")

weekday_gain = {
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": [],
}
weekday_loss = {
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": [],
}

for day in full_dataset:
    if day.day_return > 0:
        weekday_gain[day.weekday].append(day.day_return)
    else:
        weekday_loss[day.weekday].append(day.day_return)

for weekday in weekdays:
    print(
        weekday
        + " Gains / Losses: "
        + str(sum(weekday_gain[weekday]))
        + "\t"
        + str(abs(sum(weekday_loss[weekday])))
    )
    print()
print("================================")

# Best / Worst Days to be invested for each year
print("QUESTION 2")
print("================================")
print("Best / Worst days to be invested")
print("================================")

best_days = {}
worst_days = {}

dataset_by_year = {
    "2016": {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
    },
    "2017": {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
    },
    "2018": {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
    },
    "2019": {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
    },
    "2020": {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
    },
}

for day in full_dataset:
    dataset_by_year[day.year][day.weekday].append(day.day_return)

for year in dataset_by_year.keys():
    for weekday in weekdays:
        dataset_by_year[year][weekday] = sum(dataset_by_year[year][weekday])

for year in dataset_by_year.keys():
    best_day = ["Monday", 0]
    worst_day = ["Monday", 0]
    for weekday in weekdays:
        if (
            dataset_by_year[year][weekday] > 0
            and dataset_by_year[year][weekday] > best_day[1]
        ):
            best_day[0] = weekday
        elif (
            dataset_by_year[year][weekday] < 0
            and dataset_by_year[year][weekday] < worst_day[1]
        ):
            worst_day[0] = weekday
    print("Year: " + year)
    print("\tBest day: " + best_day[0])
    print("\tWorst day: " + worst_day[0])
print("=============================")

# Best / Worst Days to be invested for each year
print("QUESTION 3")
print("=============================")
print("Aggregate Tables from 5 years")
print("=============================")

print("SUN")
print("============================")
r = load_data_from_file("ALL", ticker_file)
data = calculate_data(r)
print_table(data)

print("============================")
print("SUN")
best_day = ["Monday", 0]
worst_day = ["Monday", 0]
index = 0
for weekday in weekdays:
    if data["µ(R)"][index] > 0 and data["µ(R)"][index] > best_day[1]:
        best_day[0] = weekday
        best_day[1] = data["µ(R)"][index]
    elif data["µ(R)"][index] < 0 and data["µ(R)"][index] < worst_day[1]:
        worst_day[0] = weekday
        worst_day[1] = data["µ(R)"][index]
    index = index + 1
print("\tBest day: " + best_day[0])
print("\tWorst day: " + worst_day[0])

print("============================")
print("SPY")
print("============================")
r = load_data_from_file("ALL", ticker_file_spy)
data = calculate_data(r)
print_table(data)

best_day = ["Monday", 0]
worst_day = ["Monday", 0]
index = 0
for weekday in weekdays:
    if data["µ(R)"][index] > 0 and data["µ(R)"][index] > best_day[1]:
        best_day[0] = weekday
        best_day[1] = data["µ(R)"][index]
    elif data["µ(R)"][index] < 0 and data["µ(R)"][index] < worst_day[1]:
        worst_day[0] = weekday
        worst_day[1] = data["µ(R)"][index]
    index = index + 1
print("============================")
print("SPY")
print("\tBest day: " + best_day[0])
print("\tWorst day: " + worst_day[0])
print("============================")

# Question 4
# Oracle - Day Trading
# ======================
print("QUESTION 4")
r = load_data_from_file("ALL-NOWEEKDAY", ticker_file)
print("============================")
money = 100.00

for day in r:
    if day > 0:
        money = money * (1 + day)

print(
    "After 5 years of trading with SUN, starting with $100.00, we have: $"
    + str(round(money, 2))
)
r = load_data_from_file("ALL-NOWEEKDAY", ticker_file_spy)
print("============================")
money = 100.00

for day in r:
    if day > 0:
        money = money * (1 + day)

print(
    "After 5 years of trading with SPY, starting with $100.00, we have: $"
    + str(round(money, 2))
)
print("============================")

# Question 5
# Oracle - Buy and Hold
# ======================
print("QUESTION 5")
r = load_data_from_file("ALL-NOWEEKDAY", ticker_file)
print("============================")
money = 100.00
multiplier = 0

for day in r:
    if day > 0:
        multiplier = multiplier + day

money = money * multiplier

print(
    "After 5 years of holding with SUN, starting with $100.00, we have: $"
    + str(round(money, 2))
)
r = load_data_from_file("ALL-NOWEEKDAY", ticker_file_spy)
print("============================")
money = 100.00
multiplier = 0

for day in r:
    if day > 0:
        multiplier = multiplier + day

money = money * multiplier

print(
    "After 5 years of holding with SPY, starting with $100.00, we have: $"
    + str(round(money, 2))
)
print("============================")


# Question 6
# Oracle - Taking Revenge
# =======================
print("QUESTION 6")

def remove_ten_best(r):
    a = r[:]
    for i in range(10):
        a.remove(max(a))
    return a

def remove_ten_worst(r):
    b = r[:]
    for i in range(10):
        b.remove(min(b))
    return b

def remove_five_best_and_worst(r):
    c = r[:]
    for i in range(5):
        c.remove(max(c))
    for i in range(5):
        c.remove(min(c))
    return c


r_sun = load_data_from_file("ALL-NOWEEKDAY", ticker_file)
print("============================")
print("SUN")
print("============================")

sun_a = remove_ten_best(r_sun)
sun_b = remove_ten_worst(r_sun)
sun_c = remove_five_best_and_worst(r_sun)

# Q1 for SUN
money = 100

for day in sun_a:
    if day > 0:
        money = money * (1 + day)
    elif day < 0:
        money = money * (1 + day)

print("Starting with $100, having removed the 10 best days: $" + str(round(money, 2)))

# Q2 for SUN
money = 100

for day in sun_b:
    if day > 0:
        money = money * (1 + day)
    elif day < 0:
        money = money * (1 + day)

print("Starting with $100, having removed the 10 worst days: $" + str(round(money, 2)))

# Q3 for SUN
money = 100

for day in sun_c:
    if day > 0:
        money = money * (1 + day)
    elif day < 0:
        money = money * (1 + day)

print("Starting with $100, having removed the 5 best and 5 worst days: $" + str(round(money, 2)))

r_spy = load_data_from_file("ALL-NOWEEKDAY", ticker_file_spy)
print("============================")
print("SPY")
print("============================")

spy_a = remove_ten_best(r_spy)
spy_b = remove_ten_worst(r_spy)
spy_c = remove_five_best_and_worst(r_spy)

# Q1 for SUN
money = 100

for day in spy_a:
    if day > 0:
        money = money * (1 + day)
    elif day < 0:
        money = money * (1 + day)

print("Starting with $100, having removed the 10 best days: $" + str(round(money, 2)))

# Q2 for SUN
money = 100

for day in spy_b:
    if day > 0:
        money = money * (1 + day)
    elif day < 0:
        money = money * (1 + day)

print("Starting with $100, having removed the 10 worst days: $" + str(round(money, 2)))

# Q3 for SUN
money = 100

for day in spy_c:
    if day > 0:
        money = money * (1 + day)
    elif day < 0:
        money = money * (1 + day)

print("Starting with $100, having removed the 5 best and 5 worst days: $" + str(round(money, 2)))
