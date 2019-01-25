# Exercise 4: Add code to the above program to figure out who has the most messages
# in the file. After all the data has been read and the dictionary has been created,
# look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops)
# to find who has the most messages and print how many messages the person has.

d = {}
d_inv = {}
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

    print(d.items())
    for (k,v) in d.items():
        if v > maxi:
            maxi = v
            person = k

    print(person, v)

except Exception as e:
    print(str(e))
