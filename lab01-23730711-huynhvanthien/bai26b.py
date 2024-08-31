# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 13:08:48 2024

@author: Admin
"""

N = int(input("Nhập vào số nguyên N: "))
chuoi_so = str(N)
if len(chuoi_so) == 1:
    ket_qua = chuoi_so
elif len(chuoi_so) == 2:
    if chuoi_so[0] > chuoi_so[1]:
        ket_qua = chuoi_so[1] + chuoi_so[0]
    else:
        ket_qua = chuoi_so[0] + chuoi_so[1]
elif len(chuoi_so) == 3:
    a, b, c = chuoi_so[0], chuoi_so[1], chuoi_so[2]
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    ket_qua = a + b + c
elif len(chuoi_so) == 4:
    a, b, c, d = chuoi_so[0], chuoi_so[1], chuoi_so[2], chuoi_so[3]
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if c > d:
        c, d = d, c
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    ket_qua = a + b + c + d
print("Số sau khi sắp xếp các chữ số theo thứ tự tăng dần là:", int(ket_qua))
