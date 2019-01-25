# Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
# Vinayak Nayak
# 27/12/2018
# IST 11:37 am

hrs = float(input("Number of hours: "))
rate = float(input("What's the rate per hour? "))
print("Total price is " + str(round(rate*hrs,2)))
