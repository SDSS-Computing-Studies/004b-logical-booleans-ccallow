#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""
print("===========")
num = input("Enter a number: ")
num = float(num)
if num/2.0 == int(num/2.0) and num>0:
    a=str(num)
    print(a +" is an even integer")
else:
    a=str(num)
    print(a + " is not an even integer")
