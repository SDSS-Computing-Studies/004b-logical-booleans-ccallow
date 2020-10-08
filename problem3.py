#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""
print("================================")
import math
a = input("Enter an integer:  ")
fa=float(a)
aa=str(a)
b = input("Enter an integer:  ")
fb=float(b)
bb=str(b)
c = input("Enter an integer:  ")
fc=float(c)
cc=str(c)

if fa>fb>fc or fa>fc>fb:
    if fa**2 == fb**2 + fc**2:
        print(a+"," +b +","+ c +" form a Pythagorean triple")
    else:
        print(a+b+c +"do not form a Pythagorean triple")
elif fb>fa>fc or fb>fc>fa:
    if fa**2 + fc**2 == fb**2:
        print(a+"," +b +","+ c +" form a Pythagorean triple")
    else:
        print(a+b+c +"do not form a Pythagorean triple")
elif fc>fa>fb or fc>fb>fa:
    if fc**2 == fa**2 + fb**2:
        print(a+"," +b +","+ c +" form a Pythagorean triple")
    else:
        print(a+","+b+","+c +"do not form a Pythagorean triple")