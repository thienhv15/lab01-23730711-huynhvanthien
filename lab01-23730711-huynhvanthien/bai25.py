# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 16:04:39 2024

@author: Admin b25
"""

s = input('Nhập vào 1 chữ cái:')
if s.islower() and len(s) == 1:
    print('Kí tự hoa là', s.upper()) 
elif s.isupper() and len(s) == 1:
    print('Kí tự thường là', s.lower())
else:
    print('Không hợp lệ')
    

