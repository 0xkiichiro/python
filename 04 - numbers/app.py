# integer => 1,2,3,4,5
# float => 1.5, 2.3, etc.

## Types of numbers

# print(10//3) => returns integer
# print(10/3) => returns float

##Types of operations

# print(10+3) => addition 
# print(10-3) => substraction
# print(10%3) => modulus
# print(10*3) => multiplication
# print(10**3) => power of 10*10*10

import math

x = 10
x = x + 3
print(x)

x += 3 #same as above its called augmentend or enhanced assignment operator like in js

x = 2.9
print(round(x)) # rounds to the closest integer
print(abs(-x)) # returns always positive absolute of something

math.ceil(2.9) # => rounds to the top integer
math.floor(2.9) # => rounds to the bot integer

# for the list of all math modules
# https://docs.python.org/3/library/math.html