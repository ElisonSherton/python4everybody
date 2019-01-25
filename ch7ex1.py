# Exercise 1: Write a program to read through a file and print the contents of the file (line by line)
# all in upper case. Executing the program will look as follows:
# You can download the file from www.py4e.com/code3/mbox-short.txt

# Vinayak Nayak
# 27th December 2018
# 2:59 pm

file = open('mbox-short.txt','r')
text = file.read().split('\n')

for i in text:
    print(i.upper())
