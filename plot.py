import csv
import matplotlib.pyplot as plt
import numpy as np
import os

members = dict()  # Dictionary with member_id as the keys and home_ownership as data.
statistics = dict()  # Dictionary with home_ownership as keys and lists [Sum, Number_of_members] as items.
results = dict()  # Dictionary with home_ownership as keys and averages as items.

with open("home_ownership_data.csv", newline="") as member_csv:
    first_loop = True

    for member in csv.reader(member_csv):
        if first_loop:
            member_id_index = member.index("member_id")
            home_ownership_index = member.index("home_ownership")
            first_loop = False

            continue

        member_id = member[member_id_index]
        home_ownership = member[home_ownership_index]

        members[member_id] = home_ownership

        if home_ownership not in statistics.keys():
            statistics[home_ownership] = [float(0), int(0)]

with open("loan_data.csv", newline="") as loan_csv:
    first_loop = True
    for loan in csv.reader(loan_csv):
        if first_loop:
            member_id_index = loan.index("member_id")
            loan_amnt_index = loan.index("loan_amnt")
            first_loop = False

            continue

        member_id = loan[member_id_index]

        try:
            home_ownership = members[member_id]

        except KeyError:
            continue

        sum, number_of_members = statistics[home_ownership]

        loan_amount = float(loan[1])

        sum += loan_amount
        number_of_members += 1

        statistics[home_ownership] = [sum, number_of_members]

ticks = list()
heights = list()

for home_ownership_type in statistics.keys():
    if statistics[home_ownership_type] != 0:
        sum, number_of_members = statistics[home_ownership_type]
        average = sum/number_of_members
        results[home_ownership_type] = average

        ticks.append(home_ownership_type)
        heights.append(average)


plt.bar(np.arange(len(ticks)), height=heights, tick_label=ticks)

plt.title("Average Loan amounts per Home Ownership")
plt.ylabel("Average loan amount ($)")
plt.xlabel("Home Ownership")

if not os.path.exists("output"):
    os.mkdir("output")

plt.draw()
plt.savefig("output/output.png")

