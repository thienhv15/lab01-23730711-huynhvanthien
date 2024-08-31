# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 20:14:32 2024

@author:  Huỳnh Văn Thiên 23730711
"""

print('Nhập năm sinh của bạn')
a = int(input('Năm sinh '))
if 0 < a <= 2024:
 print('Bạn sinh năm',a,'vậy bạn', 2024 - a,'tuổi')
else:
 print('Năm sinh không phù hợp ')