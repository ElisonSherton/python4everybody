# Exercise 3: Write a program to read through a mail log, build a histogram using
# a dictionary to count how many messages have come from each email address,
# and print the dictionary.

# Vinayak Nayak
# 27th December 2018
# 04:53 pm

d = {}

try:
    file_Name = input("Enter the name of the file you wanna open: ")
    file = open(file_Name, 'r')
    lines = file.read().split('\n')

    for line in lines:
        words = line.split(' ')
        if words[0] == "From" or words[0] == "From:":
            if words[1] in d:
                d[words[1]] += 1
            else:
                d[words[1]] = 1

    for (k,v) in d.items():
        print (k + ":" + str(v))

except Exception as e:
    print(str(e))
