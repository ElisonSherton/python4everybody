# Exercise 3: Sometimes when programmers get bored or want to have a bit of fun, they add
# a harmless Easter Egg to their program Modify the program that prompts the user for the
# file name so that it prints a funny message when the user types in the exact file name "na na boo boo".
# The program should behave normally for all other files which exist and don't exist.

# Vinayak Nayak
# 27th December 2018
# 3:30 pm

name = input('Enter the file name: ')
try:
    if not name.lower() == "na na boo boo":
        file = open(name, 'r')
        lines = file.read().split('\n')
        s = 'X-DSPAM-Confidence:'
        total = 0
        count = 0
        for line in lines:
            if line[0:len(s)] == s:
                total += float(line[len(s) + 1 : ])
                count += 1
        print('Average of ' + s + + " " + str(total/count))
    else:
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
except Exception as e:
    print(str(e))
