# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:42:27 2024

@author: Admin
"""

a = int(input("Nhập vào a:"))
b = int(input("Nhập vào b:"))
c = int(input("Nhập vào c:"))
d = int(input("Nhập vào d:"))
if a <= b and a <= c and a <= d:
    print('Số nhỏ nhất là',a)
if b < a and b <= c and b <= d:
    print('Số nhỏ nhất là',b)
if c < a and c < b and c < d:
    print('Số nhỏ nhất là',c)
if d < a and d < b and d <= c:
    print('Số nhỏ nhất là',d)
