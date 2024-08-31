# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 13:43:49 2024

@author: Admin bài 20
"""

a = float(input("Nhập vào a:"))
b = float(input("Nhập vào b:"))
c = float(input("Nhập vào c:"))
if a > b and b > c:
    print('Số lớn nhất là',a)
if a > c and c > b:
    print('Số lớn nhất là',a)
if b > a and a > c:
    print('Số lớn nhất là',b)
if b > c and c > a:
    print('Số lớn nhất là',b)
if c > a and a > b:
    print('Số lớn nhất là',c)
if c > b and b > a:
    print('Số lớn nhất là',c)