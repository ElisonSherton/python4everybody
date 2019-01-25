# Exercise 2: Write a program that categorizes each mail message by which day of the
# week the commit was done. To do this look for lines that start with "From", then look for
# the third word and keep a running count of each of the days of the week. At the end of the
# program print out the contents of your dictionary (order does not matter).

# Vinayak Nayak
# 27th December 2018
# 04:40 pm

d = {}
try:
    file_name = input("Enter the name of the file you wanna read from: ")
    file = open(file_name,'r')
    lines = file.read().split('\n')
    for line in lines:
        words = line.split(' ')
        if words[0] == "From":
            day = words[2]
            if day in d:
                d[day] += 1
            else:
                d[day] = 1
    print(d)
except Exception as e:
    print(str(e))
