# Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

# Vinayak Nayak
# 27/12/2018
# IST 11:52 am

Celsius = float(input("Enter the temperature in degrees celsius: "))
Farenheit = Celsius * 1.8 + 32
print(str(Celsius) + " Celsius = " + str(round(Farenheit,2)) + " Farenheit." )
