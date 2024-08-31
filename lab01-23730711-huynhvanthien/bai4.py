# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:43:16 2024

@author:  Huỳnh Văn Thiên 23730711
"""
print('Nhâp vào số có hai chữ số')
n = int(input('n='))
a = n // 10
b = n % 10
X = a + b
if 10 <= n <= 99: 
 print('Tổng các chữ số của N là', X)
else:
    print('Số không hợp lệ ')