# Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:
#
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart the line to extract the floating-point number on the line.
# Count these lines and then compute the total of the spam confidence values from these lines.
# When you reach the end of the file, print out the average spam confidence.

# Vinayak Nayak
# 27th December 2018
# 3:24 pm

name = input('Enter the file name: ')
file = open(name, 'r')
lines = file.read().split('\n')
s = 'X-DSPAM-Confidence:'
total = 0
count = 0
for line in lines:
    if line[0:len(s)] == s:
        total += float(line[len(s) + 1 : ])
        count += 1
print('Average of ' + s + str(total/count))
