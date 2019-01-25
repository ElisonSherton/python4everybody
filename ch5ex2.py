# Exercise 2: Write another program that prompts for a list of numbers as ex1 and
# at the end prints out both the maximum and minimum of the numbers instead of the average.

# Vinayak Nayak
# 27th December 2018
# 12:57 pm

prompt = ""
total = 0
count = 0
max = 0
min = 0
while not prompt == 'done':
    try:
        prompt = input("Enter a number: ")
        n = float(prompt)

        if count == 0:
            max = n
            min = n
        elif n > max:
            max = n
        elif n < min:
            min = n

        count += 1

    except Exception as e:
        if not prompt == "done":
            print("Invalid Input")

print(max, min)
