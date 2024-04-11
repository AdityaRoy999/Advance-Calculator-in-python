import math
from itertools import permutations,combinations
from sympy import *
from sympy import roots
from sympy.abc import x,a,b,c
import numpy as np
init_printing()
while True:
     print("---------------O-P-T-I-O-N-S---------------")
     print("1. Basic Arithmetic Operations\n2. Sin,Cosine,Tan\n3. Root Operations\n4. factorial,permutations,combinations\n5. Log Operations\n6. Derivation and Integration\n7. matrix")
     print("-------------------------------------------")
     choice = int(input("Enter the operation you want to do: "))
try:
    init_printing()
    while True:
     try:
         print("---------------O-P-T-I-O-N-S---------------")
         print("1. Basic Arithmetic Operations\n2. Sin,Cosine,Tan\n3. Root Operations\n4. factorial,permutations,combinations\n5. Log Operations\n6. Derivation and Integration")
         print("-------------------------------------------")   
     except ZeroDivisionError as e:
        print(e) 
     except ValueError as e:
        print(e)
     except TypeError as e:
        print(e)
     except NameError as e:
        print(e)
     except FileNotFoundError as e:
        print(e)       
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
            print ("The division of two numbers: ",div)
        def exp(exp):
            a = int(input("Enter number 1: "))
            b = int(input("Enter number 2: "))
            exp = a**b
            print("The exponent of the following numbers are: ",exp)
     class trigno():
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
     class deffandint():
         def derivative(self):
             print("-------------------------------------\nPre-defined for evaluating expressions\n1.)exponential(start with) - exp\n2).exponential - **\n3.)For trignometric function - trignometric(variable) Eg:- sin(x)\n4.)Root-Operations = sqrt(x),cbrt(y)\n-------------------------------------------")
             exp = input("Enter the expression: ")
             n = int(input("Enter how many times you want to differentiate with a particular variable: "))
             #pprint(Integral(exp,respect_to),pprint_use_unicode= True)
             for i in range(n):
                 respect_to = input("Enter the variable you wish to find the differentiate with: ")
             #times = int(input("Enter the times you want to different with repect to selected variable: "))             
             times = int(input("Enter the times you want to different with repect to selected variable: "))
             t = diff((exp),(respect_to),(times))
             pprint(t,use_unicode=False)
         def indefinite_integration(self):
             print("-------------------------------------\nPre-defined for evaluating expressions\n1.)exponential(start with) - exp\n2).exponential - **\n3.)For trignometric function - trignometric(variable) Eg:- sin(x)\n4.)Root-Operations = sqrt(x),cbrt(y)\n-------------------------------------------")
             exp = input("Enter the expression: ")
             x = Symbol('x')
             y = Symbol('y')
             z = Symbol('z')
             n = None
             variable = input("Input the variable you wish to integrate with: ")
             if variable == 'x':
                 n = x
             elif variable == 'y':
                 n = y
             else:
                 n = z
             pprint(Integral(exp,n))
             print("The asnwer to your integral is: ")
             intg = integrate(exp,n)
             pprint(intg,use_unicode = False)
         def definite_integration(self):
             print("-------------------------------------\nPre-defined for evaluating expressions\n1.)exponential(start with) - exp\n2).exponential - **\n3.)For trignometric function - trignometric(variable) Eg:- sin(x)\n4.)Root-Operations = sqrt(x),cbrt(y)\n-------------------------------------------")
             print("1. Single Integration\n2. Double Integration\n3. Triple Integration")
             choice = int(input("Enter your choice: "))
             if choice == 1:
                 exp = input("Enter the expression: ")

                 variable = input("Enter the variable: ")
                 start_limit = input("Enter the start limit: ")
                 stop_limit = input("Enter the stop limit: ")
                 pprint(Integral(exp,(variable,stop_limit,start_limit)))
                 pprint((integrate(exp,(variable,stop_limit,start_limit))),use_unicode = False)
             elif choice == 2:
                 exp = input("Enter the expression you wish to integrate for: ")
                 variable = input("Enter the 1st variable you wish to integrate for: ")
                 start_limit = input("Enter the start limit for {}: ".format(variable))
                 stop_limit = input("Enter the stop limit for {}: ".format(variable))
                 print("----------------------------------")
                 variable1 = input("Enter the 2nd variable you wish to integrate for: ")
                 start_limit1 = input("Enter the start limit for {}: ".format(variable1))
                 stop_limit1 = input("Enter the stop limit for {}: ".format(variable1))
                 #print(Integral(exp,(variable,stop_limit,start_limit),(variable1,start_limit1,stop_limit1)))
                 pprint(Integral(exp,(variable,stop_limit,start_limit),(variable1,start_limit1,stop_limit1)))
                 print("The answer to your integral is: ")
                 pprint((integrate(exp,(variable,stop_limit,start_limit),(variable1,stop_limit1,start_limit1))),use_unicode = False) 
             elif choice == 3:
                 exp = input("Enter the expression you wish to integrate for: ")
                 variable = input("Enter the 1st variable you wish to integrate for: ")
                 start_limit = input("Enter the start limit for {}: ".format(variable))
                 stop_limit = input("Enter the stop limit for {}: ".format(variable))
                 print("----------------------------------")
                 variable1 = input("Enter the 2nd variable you wish to integrate for: ")
                 start_limit1 = input("Enter the start limit for {}: ".format(variable1))
                 stop_limit1 = input("Enter the stop limit for {}: ".format(variable1))
                 print("----------------------------------")
                 variable2 = input("Enter the 3rd variable you wish to integrate for: ")
                 start_limit2 = input("Enter the start limit for {}: ".format(variable2))
                 stop_limit2 = input("Enter the stop limit for {}: ".format(variable2))
                 pprint(Integral(exp,(variable,stop_limit,start_limit),(variable1,start_limit1,stop_limit1),(variable2,stop_limit2,start_limit2)))
                 print("-----------------------------------")
                 print("The answer to your integral is: ")
                 #pprint((integrate(exp,(variable,stop_limit,start_limit),(variable1,stop_limit1,start_limit1),(variable3,stop_limit3,start_limit3))),use_unicode = False)
                 pprint((integrate(exp,(variable,stop_limit,start_limit),(variable1,stop_limit1,start_limit1),(variable2,stop_limit2,start_limit2))))
             else:
                 print("Invalid option")

     class Root_Equation():
         def Quadratic():
             pass
     class matrix():
         def addition(self):
            print("Input for matix1: ")
            rows = int(input("Enter the Rows of the Matrix: "))
            column = int(input("Enter the Column of the matrix: "))

            print("Plese enter the elements of the matrix in a singl line and seperate by space: ")

            elements = list(map(int, input().split()))
            print("Your mtrix1 is:\n")

            matrix1 = np.array(elements).reshape(rows, column)

            pprint(matrix1)
            print(" \n ")

            print("Input for matix2: ")
            rows = int(input("Enter the Rows of the Matrix: "))
            column = int(input("Enter the Column of the matrix: "))

            print("Plese enter the elements of the matrix in a singl line and seperate by space: ")

            elements = list(map(int, input().split()))
            print("Your mtrix2 is:\n")

            matrix2 = np.array(elements).reshape(rows, column)

            pprint(matrix2)
            print(" \n ")
    
            add_matrix = np.add(matrix1, matrix2)
            print(f"Your matrix addition is: {add_matrix}")

         def substraction(self):
            print("Input for matix1: ")
            rows = int(input("Enter the Rows of the Matrix: "))
            column = int(input("Enter the Column of the matrix: "))

            print("Plese enter the elements of the matrix in a singl line and seperate by space: ")

            elements = list(map(int, input().split()))
            print("Your mtrix1 is:\n")

            matrix1 = np.array(elements).reshape(rows, column)

            pprint(matrix1)
            print(" \n ")

            print("Input for matix2: ")
            rows = int(input("Enter the Rows of the Matrix: "))
            column = int(input("Enter the Column of the matrix: "))

            print("Plese enter the elements of the matrix in a singl line and seperate by space: ")

            elements = list(map(int, input().split()))
            print("Your mtrix2 is:\n")

            matrix2 = np.array(elements).reshape(rows, column)

            print(matrix2)
            print(" \n ")
            if rows == column:
                    sub_matrix = np.subtract(matrix1, matrix2)
                    print(f"Your matrix substraction is: {sub_matrix}")
            else: 
                    print("Error! Rows and Columns must be same")

         def multiply(self):
            print("Input for matix1: ")
            rows = int(input("Enter the Rows of the Matrix: "))
            column = int(input("Enter the Column of the matrix: "))
            print("Plese enter the elements of the matrix in a singl line and seperate by space: ")
            elements = list(map(int, input().split()))
            print("Your mtrix1 is:\n")
            matrix1 = np.array(elements).reshape(rows, column)
            print(matrix1)
            print(" \n ")
            print("Input for matix2: ")
            rows = int(input("Enter the Rows of the Matrix: "))
            column = int(input("Enter the Column of the matrix: "))
            print("Plese enter the elements of the matrix in a singl line and seperate by space: ")
            elements = list(map(int, input().split()))
            print("Your mtrix2 is:\n")
            matrix2 = np.array(elements).reshape(rows, column)
            print(matrix2)
            print(" \n ")
            if rows == column:
                    mul_matrix = np.multiply(matrix1, matrix2)
                    print(f"Your matrix Multiplication is: {mul_matrix}")
            else:
                    print("Error! Rows and Columns must be same")     
     calculator = Calculator()   
     calculator11 = trigno()
     matrix1 = matrix()
     deffandint1 = deffandint()
     choice = int(input("Enter the operation you want to do: "))
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
     elif choice == 6:
         print("--------")
         print("1. Differentiation\n2. Indefinite Integration\n3. Definite Integration")
         choice = int(input("Enter your choice: "))
         if choice == 1:
             deffandint1.derivative()
         elif choice == 2:
             deffandint1.indefinite_integration()
         elif choice == 3:
             deffandint.definite_integration()
     elif choice == 7:
         print("1.Matrix Adiitiom\n2.Matrix Subtraction\n3. Matrix multiplication")
         choice = int(input("Enter the options: "))
         if choice == 1:
                matrix1.addition()
         elif choice == 2:
                matrix1.substraction()
         elif choice == 3:
                matrix1.multiply()
             deffandint1.definite_integration()
         else:
                print("Invalid option")         
     else:
            print("Please enter a valid option next time")
     
     retry = input("Do you want to try again: ").lower()
     if retry == 'yes':
         continue
     elif retry == 'y':
         continue
     else:
         break
except ZeroDivisionError as e:
    print("The error you are getting is: ")
    print(e) 
except ValueError as e:
    print("The error you are getting is: ")
    print(e)
except TypeError as e:
    print("The error you are getting is: ")
    print(e)
except NameError as e:
    print("The error you are getting is: ")
    print(e)
except FileNotFoundError as e:
    print("The error you are getting is: ")
    print(e)
finally:
    print("please Re-Run the calculator") 
    print("---------Thank you have a great day----------")

     








