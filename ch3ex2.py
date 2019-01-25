# Rewrite your pay program (ch2 ex1) using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program.
# The following shows two executions of the program:

# Vinayak Nayak
# 27th December 2018
# 12:10 pm

flag = True

try:
    hrs = float(input("Enter employee's worked hours: "))
except Exception as e:
    print("Enter valid number of hours")
    flag = False

if flag:
    try:
        rate = float(input("Hourly rate of employee: "))
    except:
        print("Enter valid rate for the work of employee")
        flag = False

if flag:
    if hrs <= 40:
        amount = hrs * rate
    else:
        amount = 40 * rate + (hrs - 40) * rate * 1.5

    print("The Employee is eligible a sum of " + str(amount) + " units for his work.")
