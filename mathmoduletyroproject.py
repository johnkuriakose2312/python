"""
Author:JOHN KURIAKOSE
Date:18 October
Description:Write a Python program that uses functions from the math module to perform the following operations on a number provided by the user:

    Find the square root.
    Calculate the factorial.
    Raise the number to the power of 2.
Expected Output:Enter a number: 5
Square root of 5: 2.23606797749979
Factorial of 5: 120
5 raised to power 2: 25.0
"""

import math
number=int (input("Enter your number:"))
print("Square root Of",number,":",math.sqrt(number))
print("Factorial of",number,":",math.factorial(number))
print(number,"raised to power 2:",math.pow(number,2))