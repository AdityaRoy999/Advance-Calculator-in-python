from arithmetic import Calculator
from trignometric_functions import trigno
from Inverse_trignometric_functions import inv_tri_func
from Root_operations import rootop
from Factorial_combinations_permutations import fa
from Log_operations import logop
from calculus import deffandintandlim,serandfindef
from matrix import matrix

try:
    while True:
        print("---------------O-P-T-I-O-N-S---------------")
        print("1. Basic Arithmetic Operations\n2. Sin,Cosine,Tan,Cot,Sec,Cosec\n3. Inverse Trigno functions\n4. Root Operations\n5. factorial,permutations,combinations\n6. Log Operations\n7. Limit,Derivation and Integration\n8. Series Expansion and Finite differences\n9. Matrix Operations")
        print("-------------------------------------------")
        calculator = Calculator()   
        calculator11 = trigno()
        deffandintlim1 = deffandintandlim()
        matrix1 = matrix()
        serandfindef1 = serandfindef()
        inv_tri_f = inv_tri_func()
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
            print("1. Sin\n2. Cos\n3. Tan\n.4. cot\n5. sec\n6. cosec")
            choice = int(input("Enter Your choice: "))
            if choice == 1:
                calculator11.sin()
            elif choice == 2:
                calculator11.cos()
            elif choice == 3:
                calculator11.tan()
            elif choice == 4:
                calculator11.cot()
            elif choice == 5:
                calculator11.sec()
            elif choice == 6:
                calculator11.cosec()
            else:
                print("Please enter a valid choice next time") 
        elif choice == 3:
            print("1.Sin Inverse\n2.Cos Inverse\n3.Tan Inverse")
            choice = int(input("Enter the choice: "))
            if choice == 1:
                inv_tri_f.sin_inverse()
            elif choice == 2:
                inv_tri_f.cos_inverse()
            elif choice == 3:
                inv_tri_f.tan_inverse()
            else:
                print("Please Enter a valid choice")
        elif choice == 4:
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
        elif choice == 5:
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
        elif choice == 6:
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
        elif choice == 7:
            print("--------")
            print("1. Limit\n2. Differentiation\n3. Indefinite Integration\n4. Definite Integration")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                deffandintlim1.limit()       
            elif choice == 2:
                deffandintlim1.derivative()
            elif choice == 3:
                deffandintlim1.indefinite_integration()
            elif choice == 4:
                deffandintlim1.definite_integration()
            else:
                print("Please enter a valid option next time")
        elif choice == 8:
            print("1. Series Expansion\n2. Finite difference")
            choice = int(input("Enter a choice: "))
            if choice == 1:
                serandfindef1.series_expansion()
            elif choice == 2:
                serandfindef1.finite_difference()
            else:
                print("Please enter a valid choice")
        elif choice == 9:
            print("--------")
            print("1. Matrix Addition\n2. Matrix Subtraction\n3. Matrix Multiplication")
            choice = int(input("Enter your choice: ")) 
            if choice == 1:
                matrix1.addition()
            elif choice == 2:
                matrix1.substraction()
            elif choice == 3:
                matrix1.multiply()
            else:
                print("Please Enter a valid choice: ")
        retry = input("Do you want to try again: ").lower()
        retry = retry = input("Do you want to try again: ").lower()
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