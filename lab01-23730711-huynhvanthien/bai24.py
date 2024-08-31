# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:42:10 2024

@author: Abài 24
"""

print('Nhâp vào giờ, phút, giây')
a = float(input('Giờ = '))
b = float(input('Phút = '))
c = float(input('Giây = '))
if  0 <= a <= 23 and 0 <= b <= 59 and 0 <= c <= 59:
  print('Hợp lệ')
else:    
 print('Không hợp lệ')
