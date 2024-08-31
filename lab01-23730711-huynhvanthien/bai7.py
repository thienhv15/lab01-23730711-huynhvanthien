# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:24:33 2024

@author: Adminbai7
"""

r = float(input("Nhập vào r:"))
pi = 3.14
s =  pi * r**2
c = 2 * pi * r
if r >= 0:
    print('Diện tích của hình tròn là', s)
    print('Chu vi của hình tròn là', c)
else:
    print('r không hợp lệ')
    
