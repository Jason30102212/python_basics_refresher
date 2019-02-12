# 5.WorkingWithNumbers

number = 5.234
print(number) 

number = number + 10
print(number)

# 
print(3 * 4 + 5) # Multiplication then addition
print(3 * (4 + 5)) # Addition then multiplication

# Modular
print(10 % 3) # Remainder of division

# Convert to string
print(str(number))
# print(number + " and String"). # Error. number not a string
print(str(number) + " and String")

# Math functions
negativeNumber = -5
print(abs(negativeNumber)) # Print absolute value
print(pow(3,2)) # 3 to the power of 2
print(max(4,2)) # Returns highest number
print(min(4,2)) # Returns lowest number
print(round(3.7)) # Round number
print(round(3.4)) # Round number

from math import *

print(ceil(3.6)) # Round up
print(sqrt(36)) # Return square root
