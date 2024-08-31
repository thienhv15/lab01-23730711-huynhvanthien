# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 21:36:51 2024

@author: Admin
"""

ngay = int(input("Nhập ngày sinh: "))
thang = int(input("Nhập tháng sinh: "))
nam = int(input("Nhập năm sinh: "))
if 0 < ngay <= 31 and  0 < thang <= 12 and nam > 0:
 print('{0}/{1}/{2}'.format(ngay, thang, nam))
 print(f"{ngay}/{thang}/{str(nam)[-2:]}")
 print('{0}/{1}/{2}'.format(nam, thang, ngay))
else:
    print('Không hợp lệ hãy nhập lại')