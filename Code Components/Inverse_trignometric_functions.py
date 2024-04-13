import math
class inv_tri_func():
         def sin_inverse(self):
             a = int(input("Enter number 1: "))
             b = int(input("Enter number 2: "))
             print("The  sin-1(a) in degress is = :",round(math.degrees((math.asin(a)))))
             print("The  sin-1(b) in degrees is = :",round(math.degrees((math.asin(b)))))
         def cos_inverse(self):
             a = int(input("Enter number 1: "))
             b = int(input("Enter number 2: "))
             print("The cos-1(a) in degress is = :",round(math.degrees((math.acos(a)))))
             print("The cos-1(b) in degrees is = :",round(math.degrees((math.acos(b)))))
         def tan_inverse(self):
             a = int(input("Enter number 1: "))
             b = int(input("Enter number 2: "))
             print("The tan-1(a) in degress is = :",round(math.degrees((math.atan(a)))))
             print("The tan-1(b) in degrees is = :",round(math.degrees((math.atan(b)))))