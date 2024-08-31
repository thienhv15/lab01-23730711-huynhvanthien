# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:56:12 2024

@author: Admin
"""

n = int(input('Nhập vào số có 4 chữ số: '))
d = n % 10; n = n // 10
c = n % 10; n = n // 10
b = n % 10; n = n // 10
a = n
SoNut = (a + b + c + d) 
s1 = SoNut // 10
s2 = SoNut % 10
S = s1 + s2
print("Số nút là ", S)

