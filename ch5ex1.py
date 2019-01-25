# Exercise 1: Write a program which repeatedly reads numbers until the user enters "done".
# Once "done" is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number, detect their mistake using
# try and except and print an error message and skip to the next number.

# Vinayak Nayak
# 27th December 2018
# 12:49 pm

prompt = ""
total = 0
count = 0
while not prompt == 'done':
    try:
        prompt = input("Enter a number: ")
        n = float(prompt)
        total += n
        count += 1
    except Exception as e:
        if not prompt == "done":
            print("Invalid Input")

print(total, count, round(total/count, 2))
