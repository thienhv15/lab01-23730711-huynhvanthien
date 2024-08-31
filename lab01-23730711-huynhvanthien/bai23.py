# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:37:13 2024

@author: Admin bài 23
"""

import math
print("Giải phương trình bậc 2: ax^2 + bx + c = 0 (a khác 0)")
a = float(input("Nhập hệ số a: "))
if a == 0:
    print("Số a phải khác 0")     
b = float(input("Nhập hệ số b: "))        
c = float(input("Nhập hệ số c: "))
delta = b**2 - 4 * a * c
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    print("Phương trình có nghiệm kép x1 = x2 = ", -(b / (2 * a)) )
else:
    print("Phương trình có hai nghiệm phân biệt:")
    print("x1= ", (-b+math.sqrt(delta))/(2*a)) 
    print("x2= ", (-b-math.sqrt(delta))/(2*a))