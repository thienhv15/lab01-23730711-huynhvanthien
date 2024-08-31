# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:15:05 2024

@author: Admin
"""

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
t = 0
if a > b:
    t = a
    a = b
    b = t
if a > c:
    t = a
    a = c
    c = t
if b > c:
    t = b
    b = c
    c = t
print("Thứ tự tăng dần của ba số là: {0}, {1}, {2}".format(a, b, c))
