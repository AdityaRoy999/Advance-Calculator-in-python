import numpy as np
from sympy import *
class matrix():
         def addition(self):
            print("Input for matix1: ")
            rows = int(input("Enter the Rows of the Matrix: "))
            column = int(input("Enter the Column of the matrix: "))

            print("Plese enter the elements of the matrix in a single line and seperate by space: ")

            elements = list(map(int, input().split()))
            print("Your matrix 1 is:\n")

            matrix1 = np.array(elements).reshape(rows, column)

            pprint(matrix1)
            print(" \n ")

            print("Input for matix2: ")
            rows = int(input("Enter the Rows of the Matrix: "))
            column = int(input("Enter the Column of the matrix: "))

            print("Plese enter the elements of the matrix in a singl line and seperate by space: ")

            elements = list(map(int, input().split()))
            print("Your matrix 2 is:\n")

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