# Exercise 5: Write a program to read through the mail box data and when you find
# line that starts with "From", you will split the line into words using the split
# function. We are interested in who sent the message, which is the second word on the From line.
#
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# You will parse the From line and print out the second word for each From line,
# then you will also count the number of From (not From:) lines and print out a
# count at the end.

# Vinayak Nayak
# 27th December 2018
# 4:05 pm
count = 0
try:
    file_name = input('Enter the name of the file from which you wanna read: ')
    file = open(file_name, 'r')
    lines = file.read().split('\n')
    for line in lines:
        if line[0:4] == "From" and not line[0:5] == "From:":
            print(line.split(' ')[1])
            count = count + 1
    print("There were "+ str(count) +" lines in the file with From as the first word.")
except Exception as e:
    print(str(e))
