# Exercise 6: Rewrite the program that prompts the user for a list of numbers and
# prints out the maximum and minimum of the numbers at the end when the user enters
# "done". Write the program to store the numbers the user enters in a list and use the
# max() and min() functions to compute the maximum and minimum numbers after the loop completes.

# Vinayak Nayak
# 27th December 2018
# 04:30 pm

prompt = ''
number_list = []

while not prompt == 'done':
    try:
        prompt = input('Enter a number ')
        number = float(prompt)
        if not prompt == "done":
            number_list.append(number)
    except Exception as e:
        if not prompt == "done":
            print("Invalid Input")

maxNum = max(number_list)
minNum = min(number_list)
print(maxNum, minNum)
