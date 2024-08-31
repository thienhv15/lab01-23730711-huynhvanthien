# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:29:14 2024

@author: Admin
"""
s = input('Nhập vào kí tự:')
if s.islower() and len(s) == 1:
    S = s.upper()
    print('Kí tự hoa là', S)
else:
    print('Không hợp lệ')