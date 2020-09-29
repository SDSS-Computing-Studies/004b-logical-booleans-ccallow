#! python3
"""
Ask the user to enter a number. 
Tell them if the number is a positive integer
(2 points) 

inputs:
a number of any type

outputs:
xx is a positive integer.
xx is not a positive integer

example:
Enter a number: -3
-3 is not a positive integer
"""
print("=============================")
a=input("Choose a number: ")
print("=============================")
a=float(a)
b=str(a)
if a>0 and a==int(a):
  print(b+" is a positive number.")
else:
  print(b +" is not a positive integer")
print("=============================\n\n\n")