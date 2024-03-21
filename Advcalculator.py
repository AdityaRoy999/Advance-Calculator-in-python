import math
from itertools import permutations,combinations
while True:
     print("---------------O-P-T-I-O-N-S---------------")
     print("1. Basic Arithmetic Operations\n2. Sin,Cosine,Tan\n3. Root Operations\n4. factorial,permutations,combinations\n5. Log Operations")
     print("-------------------------------------------")
     choice = int(input("Enter the operation you want to do: "))
     class Calculator:
        def add(sum):
            a = int(input("Enter number 1: "))
            b = int(input("Enter number 2: "))
            sum = a+b
            print("The addition of two numbers:",sum)
        def mul(mul):
            a = int(input("Enter number 1: "))
            b = int(input("Enter number 2: "))
            mul = a*b
            print ("The multiplication of two numbers:",mul)
        def sub(sub):
            a = int(input("Enter number 1: "))
            b = int(input("Enter number 2: "))
            sub = a-b
            print ("The subtraction of two numbers:",sub)
        def div(div):
            a = int(input("Enter number 1: "))
            b = int(input("Enter number 2: "))
            div = a/b
            print ("The division of two numbers:",div)
        def exp(exp):
            a = int(input("Enter number 1: "))
            b = int(input("Enter number 2: "))
            exp = a**b
            print("The exponent of the following numbers are: ",exp)
     class calculator1():
         def sin(a):
            a = int(input("Enter number 1: "))
            b = int(input("Enter number 2: "))
            print("The sin(a) = :",round(math.degrees((math.sin(a)))))
            print("The sin(b) = :",round(math.degrees((math.sin(a)))))
         def cos(a):
            a = int(input("Enter number 1: "))
            b = int(input("Enter number 2: "))
            print("The cos(a) = :",round(math.degrees((math.cos(a)))))
            print("The cos(b) = :",round(math.degrees((math.cos(b)))))
         def tan(a):
            a = int(input("Enter number 1: "))
            b = int(input("Enter number 2: "))
            print("The tan(a) in degress is = :",round(math.degrees((math.tan(a)))))
            print("The tan(b) in degrees is = :",round(math.degrees((math.tan(b)))))  
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
     class logop():
         def loge():
             a = int(input("Enter the number you wish to find the log(base=e) for: "))
             print("The answer is: ",math.log(a))
         def log10():
             a = int(input("Enter the number you wish to find the find the log(base=10) for: "))
             print("The answer is: ",math.log10(a))
         def log2():
             a = int(input("Enter the number you wish to find the log(base=2) for: "))
             print("The answer is:",math.log2(a))                    
     calculator = Calculator()
     calculator11 = calculator1()
     if choice == 1:
         print("---------")
         print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponential (a^b)")
         choice = int(input("Enter your choice: "))
         if choice == 1:
             calculator.add()
         elif choice == 2:
             calculator.sub()
         elif choice == 3:
             calculator.mul()
         elif choice == 4:
             calculator.div()
         elif choice == 5:
             calculator.exp()
         else:
             print("Please enter a valid choice next time")
     elif choice == 2:
         print("---------")
         print("1. Sin\n2. Cos\n3. Tan")
         choice = int(input("Enter Your choice: "))
         if choice == 1:
             calculator11.sin()
         elif choice == 2:
             calculator11.cos()
         elif choice == 3:
             calculator11.tan()
         else:
             print("Please enter a valid choice next time") 
     elif choice == 3:
         print("---------")
         print("1. Square root\n2. Cube root\n3. Random root(Yroot(X))" )  
         choice = int(input("Enter your choice: "))
         if choice == 1:
             rootop.sqrt()
         elif choice == 2:
             rootop.cbrt()
         elif choice == 3:
             rootop.ranroot()
         else:
             print("Please enter a valid choice next time")
     elif choice == 4:
         print("---------")
         print("1. Factorial\n2. Permutations\n3. Combinations")
         choice = int(input("Enter the choice: "))
         if choice == 1:
             fa.factorial()
         elif choice == 2:
             fa.permutations()
         elif choice == 3:
             fa.combinations()
         else:
             print("Please enter a valid choice next time")
     elif choice == 5:
         print("---------")
         print("1. Natural Log\n2. Log with base 10\n3. Log with base 2")
         choice = int(input("Enter your choice: "))
         if choice == 1:
             logop.loge()
         elif choice == 2:
             logop.log10()  
         elif choice == 3:
             logop.log2()         
         else:
             print("Please enter a valid choice next time")
     else:
         print("Please enter a valid input")
     retry = input("Do you want to try again: ").lower()
     if retry == 'yes':
         continue
     elif retry == 'y':
         continue
     else:
         break         
print("---------Thank you have a great day----------")




