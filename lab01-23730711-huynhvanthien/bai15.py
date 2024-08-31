# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 22:45:11 2024

@author: Admin
"""

a = float(input("Nhập vào a:"))
b = float(input("Nhập vào b:"))
c = ((a + b) / (a ** (1/3) + b ** (1/3))) - (a*b)**(1/3)
d = (a**(1/3) - b**(1/3))**2
s = c / d
print(s)