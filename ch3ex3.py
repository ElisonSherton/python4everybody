# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message.
# If the score is between 0.0 and 1.0, print a grade using the following table:
#  Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
#  < 0.6     F

# Vinayak Nayak
# 27th December 2018
# 12:30 pm

try:
    i = float(input("Enter the score : "))

    if(i > 1 or i < 0):
        print("Entered score isn't valid.")
    else:
        if (i < 0.6):
            print("Grade: F")

        elif (i < 0.7):
            print("Grade: D")

        elif (i < 0.8):
            print("Grade: C")

        elif (i < 0.9):
            print("Grade: B")

        elif (i <= 1.0):
            print("Grade: A")

except Exception as e:
    print(str(e))
