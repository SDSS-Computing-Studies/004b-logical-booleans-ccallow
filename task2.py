#! python3
# Task2.py

"""
Ask the user to enter a number.
Tell them if the number is both a perfect square and a perfect cube.
(2 points) 

Inputs:
number

Outputs:
xx is both a perfect square and a perfect cube.
xx is only a perfect square.
xx is only a perfect cube.

Example:
Enter a number: 8
8 is only a perfect cube.
"""
import math

print("=======================================")
num=input("Enter a number:  ")
num=float(num)
a=str(num)
sq=(math.sqrt(num))

if num**(1/3) == int(num**(1/3)):
  print(a +" is ony a perfect cube.")
elif num**(1/3)== int ((num**(1/3))) and (math.sqrt(num)==int(math.sqrt(num))):
  print(a + " is both a perfect square and a perfect cube")
elif math.sqrt(num)==int(sq):
  print(a +" is only a perfect square.")
else:
  print("This is neither")