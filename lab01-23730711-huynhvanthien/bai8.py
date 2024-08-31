# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:35:40 2024

@author: Admin
"""
a = float(input("Nhập vào cân nặng tính theo kg:"))
b = float(input("Nhập vào chiều cao tính theo m:"))
BMI = a / pow(b,2)
if a > 0 and b > 0:
    print('Số đo kiểm tra sức khỏe BMI là ', BMI)
else:
    print('Cân nặng, chiều cao không hợp lệ') 
    
