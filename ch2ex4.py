# Exercise 4: Assume that we execute the following assignment statements:
#
# width = 17
# height = 12.0
# For each of the following expressions, write the value of the expression and the type (of the value of the expression).
# width//2
# width/2.0
# height/3
# 1 + 2 * 5
# Use the Python interpreter to check your answers.

# Vinayak Nayak
# 27/12/2018
# IST 11:41 am

width = 17
height = 12.0

ans1 = width // 2   # Integer division ---> int
ans2 = width / 2.0  # Convert to float and divide ---> float
ans3 = height/3     # Float by int ---> float
ans4 = 1 + 2 * 5    # Integer arithmetic --->int

print("Expression 1 Ans:" + str(ans1) + " & Ans type = " + str(type(ans1)))
print("Expression 2 Ans:" + str(ans2) + " & Ans type = " + str(type(ans2)))
print("Expression 3 Ans:" + str(ans3) + " & Ans type = " + str(type(ans3)))
print("Expression 4 Ans:" + str(ans4) + " & Ans type = " + str(type(ans4)))
