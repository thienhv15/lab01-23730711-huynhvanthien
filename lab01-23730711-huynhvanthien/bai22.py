# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:58:59 2024

@author: Admin bài 22
"""

print("Giải phương trình bậc nhất ax+b=0")
a = float(input("Nhap a:"))
b = float(input("Nhap b:"))
if a!= 0:
    print("Phương trình có nghiệm x=",-b/a)
if a == 0 and b!= 0:
    print('Phương trình vô nghiệm')
if a == 0 and b == 0:
    print("Phương trình vô số nghiệm")
      