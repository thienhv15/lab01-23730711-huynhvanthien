# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 22:55:58 2024

@author: Adminbai16
"""

print('Nhâp vào giờ, phút, giây')
a = int(input('Giờ = '))
b = int(input('Phút = '))
c = int(input('Giây = '))
if  0 <=a <= 23 and 0 <= b <= 59  and 0 <= c <= 59:
    print('{0}h{1}p{2}s'.format(a,b,c))
    s = a * 3600 + b * 60 + c 
    print('Số giây được đổi là',s,'giây' )
else:  
    print('Không hợp lệ')  