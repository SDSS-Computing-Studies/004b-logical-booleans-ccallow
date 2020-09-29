"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is frue.
"""

#! python3
print("=======================================")
num = input("Enter a number:  ")
num=float(num)
g=str(num)

if num/6 == int(num/6) and (num/8 is not int(num/8)):
    print(g+ " is frue.")
else:
    print(g +" is not frue.")
print("=======================================")