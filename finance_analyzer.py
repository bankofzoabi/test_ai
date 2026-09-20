name = input("enter your name: ")
import math as m 
salary = float(input("enter your salary: "))
food = float(input("enter food expenses: "))
smoking = float(input("enter smoking expenses: "))
commitments = float(input("enter commitments: "))
days = int (input("enter number of days: "))
total_expenses = food + smoking + commitments
print (total_expenses)
remaining = salary - total_expenses 
print(remaining)
daily_expenses = total_expenses / days 
print (daily_expenses)
expense_percentage = total_expenses / salary * 100
saving_percentage = remaining / salary * 100
print("expense percentage:",expense_percentage,"%")
print("saving percentage:",saving_percentage,"%")
highest_expense = max(food, smoking, commitments)

lowest_expense = min(food, smoking, commitments)

print(highest_expense)
print(lowest_expense)
daily_up = m.ceil(daily_expenses)

daily_down = m.floor(daily_expenses)

print(daily_up)
print(daily_down)
name = name.strip()

name = name.title()
print(name.upper())

print(name.find("a"))

print(name.count("m"))

print(name.split())
print(name[::-1])
print("Monthly Salary: {:.2f} ILS".format(salary))
print("\n========== PERSONAL FINANCE REPORT ==========\n")

print("Name: {}".format(name))
print("Monthly Salary: {:.2f} ILS".format(salary))

print("\nFood Expenses: {:.2f} ILS".format(food))
print("Smoking Expenses: {:.2f} ILS".format(smoking))
print("Commitments: {:.2f} ILS".format(commitments))

print("\nTotal Expenses: {:.2f} ILS".format(total_expenses))
print("Daily Expenses: {:.2f} ILS".format(daily_expenses))

print("\nRemaining Money: {:.2f} ILS".format(remaining))

print("\nExpense Percentage: {:.2f}%".format(expense_percentage))
print("Saving Percentage: {:.2f}%".format(saving_percentage))

print("\nHighest Expense: {:.2f} ILS".format(highest_expense))
print("Lowest Expense: {:.2f} ILS".format(lowest_expense))

print("\nRounded Daily Expenses (Up): {} ILS".format(daily_up))
print("Rounded Daily Expenses (Down): {} ILS".format(daily_down))

print("\n=============================================")
