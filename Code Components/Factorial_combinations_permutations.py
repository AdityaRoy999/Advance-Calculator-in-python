import math
from itertools import *
class fa:
         def factorial():
             a = int(input("Enter the first number: "))
             b = int(input("Enter the first number: "))
             if a>0 and b>0:
                 print("The factorial of the first number is :",math.factorial(a)) 
                 print("The factorial of second number is :",math.factorial(b))
             else:
                 print("Please enter a positive value")     
         def permutations():
             a = list(map(int, input("Enter the numbers you wish to find the permtations for: ")))
             list_ab = a
             perm = permutations(list_ab)
             print("Your permutations are: ")
             for i in list(perm):
                 print(i)
         def combinations():
             a = list(map(int, input("Enter the numbers you wish to find the combintions for: ")))
             r = int(input("Enter the length: "))
             list_ab = a
             comb = combinations(list_ab,r)
             print("Your combinations are: ")
             for i in list(comb):
                 print(i)