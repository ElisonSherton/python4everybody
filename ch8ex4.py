# Exercise 4: Download a copy of the file www.py4e.com/code3/romeo.txt.
# Write a program to open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split function.
# For each word, check to see if the word is already in a list.
# If the word is not in the list, add it to the list. When the program completes,
# sort and print the resulting words in alphabetical order.

# Vinayak Nayak
# 27th December 2018
# 3:53 pm

romeo = open('romeo.txt', 'r')
lines = romeo.read().split('\n')
words_list = []

def low(x):
    return x.lower()

for line in lines:
    words = line.split(' ')
    for word in words:
        if not word in words_list:
            words_list.append(word)

print(sorted(words_list, key = low))
