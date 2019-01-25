# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

# Vinayak Nayak
# 27th December 2018
# 12:00 pm

hrs = float(input("Enter employee's worked hours: "))
rate = float(input("Hourly rate of employee: "))

if hrs <= 40:
    amount = hrs * rate
else:
    amount = 40 * rate + (hrs - 40) * rate * 1.5

print("The Employee is eligible a sum of " + str(amount) + " units for his work.")
