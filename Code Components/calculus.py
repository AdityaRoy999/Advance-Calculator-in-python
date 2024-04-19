from sympy import *
x = symbols('x')
class deffandintandlim():
         def limit(self):
             print("1.Limit(Normal)\n2.Postive Limit\n3.Negative Limit")
             choice = int(input("Enter a choice: "))
             if choice == 1:
                 expr = input("Enter the expression: ")
                 value = input("Enter the value: ")
                 print("The answer to {} is".format(expr))
                 limit1 = limit(expr,x,value)
                 pprint(limit1)
             elif choice == 2:
                 expr = input("Enter the expression: ")
                 value = input("Enter the value: ")
                 print("The answer to {} is".format(expr))
                 limit1 = limit(expr,x,value,'+')
                 pprint(limit1)
             elif choice == 3:
                 expr = input("Enter the expression: ")
                 value = input("Enter the value: ")
                 print("The answer to {} is".format(expr))
                 limit1 = limit(expr,x,value,'-')
                 pprint(limit1)
             else:
                 print("Please choose a valid option")     
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
class serandfindef():
         def series_expansion(self):
             exp = sympify(input("Enter the expression: "))
             n = int(input("Enter the point you want to compute the series to: "))
             pprint(exp.series(x, 0, n).removeO())
         def finite_difference(self):
             order = int(input("Enter the order: "))  
             x_list = sympify(list(map(int, input("Enter the integers with space: ").split())))
             y_list = sympify(list(map(str,input("Enter the parameters you want to use with space: ").split())))
             print("Your answer is: ")
             pprint(apply_finite_diff(order,x_list,y_list,0))