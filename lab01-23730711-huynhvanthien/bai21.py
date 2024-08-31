# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:48:28 2024

@author: Admin bài 21
"""

n = int(input('Nhập 1 số bất kì: '))
s= {0:'Không',
    1:'Một',
    2:'Hai',
    3:'Ba',
    4:'Bốn',
    5:'Năm',
    6:'Sáu',
    7:'Bảy',
    8:'Tám',
    9:'Chín'}
if 0 <= n <= 9:
    print(s[n])
else:
    print('Không đọc được')
 