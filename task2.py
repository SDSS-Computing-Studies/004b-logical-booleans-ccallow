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

x = num**(1/3)
x = round(x,10)
y= num**(1/2)
y= round(y,10)
if x == int(x):
  if y==int(y):
    print(a + " is both a perfect square and a perfect cube.")
  else:
    print(a +" is ony a perfect cube.")
elif y==int(y):
  print(a +" is only a perfect square.")
else:
  print("This is neither")