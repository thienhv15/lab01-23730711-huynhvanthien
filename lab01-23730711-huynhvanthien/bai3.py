# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:12:47 2024

@author: Admin
"""
a = int(input("Nhập vào a:"))
b = int(input("Nhập vào b:"))
c = a // b
d = a % b
if a > 0 and b > 0:
    print('Kết quả là chia lấy phần nguyên là', c)
    print('Kết quả chia lấy phần dư là', d) 
else:
    print('Nhập lại a,b')
    

