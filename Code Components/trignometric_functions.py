import math
class trigno():
         def sin(self):
            a = int(input("Enter number 1: "))
            b = int(input("Enter number 2: "))
            print("The sin(a) = :",round(math.degrees((math.sin(a)))))
            print("The sin(b) = :",round(math.degrees((math.sin(a)))))
         def cos(self):
            a = int(input("Enter number 1: "))
            b = int(input("Enter number 2: "))
            print("The cos(a) = :",round(math.degrees((math.cos(a)))))
            print("The cos(b) = :",round(math.degrees((math.cos(b)))))
         def tan(self):
            a = int(input("Enter number 1: "))
            b = int(input("Enter number 2: "))
            print("The tan(a) in degress is = :",round(math.degrees((math.tan(a)))))
            print("The tan(b) in degrees is = :",round(math.degrees((math.tan(b)))))
         def cot(self):
            a = int(input("Enter number 1: "))
            b = int(input("Enter number 2: "))
            print("The cot(a) in degress is = :",round(math.degrees((1/math.atan(a)))))
            print("The cot(b) in degrees is = :",round(math.degrees((1/math.atan(b)))))
         def sec(self):
            a = int(input("Enter number 1: "))
            b = int(input("Enter number 2: "))
            print("The sec(a) in degress is = :",round(math.degrees((1/math.cos(a)))))
            print("The sec(b) in degrees is = :",round(math.degrees((1/math.cos(b)))))
         def cosec(self):
            a = int(input("Enter number 1: "))
            b = int(input("Enter number 2: "))
            print("The cosec(a) in degress is = :",round(math.degrees((1/math.asin(a)))))
            print("The cosec(b) in degrees is = :",round(math.degrees((1/math.asin(b)))))