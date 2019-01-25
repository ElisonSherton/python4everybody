# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and
# create a function called computepay which takes two parameters (hours and rate).

# Vinayak Nayak
# 27th December 2018
# 12:36 pm
def computePay(hours, rate):
    amt = 0
    if hours >= 40:
        amt = 40 * rate + (hours - 40) * 1.5 * rate
    else:
        amt = hours * rate
    print("The Employee is eligible a sum of " + str(amt) + " units for his work.")

try:
    hrs = float(input("Enter employee's worked hours: "))
    rate = float(input("Hourly rate of employee: "))
    computePay(hrs, rate)
except Exception as e:
    print("Invalid Input")
