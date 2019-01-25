# Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt
#
# Write a program that reads the words in words.txt and stores them as keys in a
# dictionary. It doesn't matter what the values are. Then you can use the in
# operator as a fast way to check whether a string is in the dictionary.

# Vinayak Nayak
# 27th December 2018
# 04:35 pm

d = {}
file = open('words.txt', 'r')
lines = file.read().split('\n')

for line in lines:
    words = line.split(' ')
    for word in words:
        if not word in d:
            d[word] = 1
        else:
            d[word] = d[word] + 1

for (k,v) in d.items():
    print (k + ":" + str(v))
