# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 21:18:27 2024

@author: Admin
"""

print('Nhâp vào giờ, phút, giây')
a = int(input('Giờ = '))
b = int(input('Phút = '))
c = int(input('Giây = '))
print('{0}:{1}:{2}'.format(a,b,c))
if  0 <=a <= 23 and 0 <= b <= 59  and 0 <= c <= 59:
    s = a * 3600 + b * 60 + c 
    print('Số giây được đổi là',s,'giây' )
else:  
    print('Không hợp lệ')  