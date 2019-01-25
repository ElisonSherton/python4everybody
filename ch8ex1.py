# Exercise 1: Write a function called chop that takes a list and modifies it,
# removing the first and last elements, and returns None. Then write a function
# called middle that takes a list and returns a new list that contains all
# but the first and last elements.

# Vinayak Nayak
# 27th December 2018
# 3:40 pm

def modify_list(l):
    del l[0]
    del l[-1]

def middle(l):
    m = l[1:]
    m = m[:-1]
    return m

l = ['Mil', 'Jew', 'Sag', 'Vin', 'Jan']

print(middle(l))
print(l)
modify_list(l)
print(l)
