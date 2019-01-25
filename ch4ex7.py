# Exercise 7: Rewrite the grade program from the previous chapter using a function called
# computegrade that takes a score as its parameter and returns a grade as a string.
#  Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
#  < 0.6     F

# Vinayak Nayak
# 27th December 2018
# 12:40 pm

def computeGrade(i):
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

try:
    i = float(input("Enter the score : "))
    computeGrade(i)
except Exception as e:
    print("Invalid input.")
