from sympy import *
init_printing(use_unicode=True)
x, y, z = symbols('x y z')
class ssimplify:
    def simplify(self):
        exp = input("Enter the expression to simplify: ")
        print("Your answer is: ")
        pprint(simplify(exp))
        


