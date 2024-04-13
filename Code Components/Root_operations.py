import math
class rootop:
         def sqrt():
            a = int(input("Enter number 1: "))
            b = int(input("Enter number 2: "))
            print(math.sqrt(a))
            print(math.sqrt(b))
         def cbrt():
            a = int(input("Enter number 1: "))
            b = int(input("Enter number 2: "))
            print(math.cbrt(a))
            print(math.cbrt(b))
         def ranroot():
            a = int(input("Enter the x: "))
            b = int(input("Enter the y: "))
            b_div = 1/b
            print("Your answer for the random root is: ",a**b_div)