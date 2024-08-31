# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 17:04:35 2024

@author: Admin
"""

chon = input("Nhập hình (v cho hình vuông, n cho hình chữ nhật, t cho hình tròn): ")
if chon == 'v':
  print("Tính P và S của hình vuông")
  canh = int(input('Nhập cạnh của hình vuông: '))
  if canh > 0:
   P = canh * 4
   S = canh * canh
   print('P =',P, 'S=',S )
  else:
    print('Kích thước không hợp lệ')
elif chon == 'n':
  print("Tính P và S của hình chữ nhật")
  dai = int(input('Nhập chiều dài '))
  rong = int(input('Nhập chiều rộng '))
  if dai > 0 and rong > 0:
   P = (dai + rong)*2
   S = dai * rong
   print('S =',S,'P =', P)
  else:
       print('Kích thước không hợp lệ')
elif chon == 't':
  print("Tính P và S của hình tròn")
  pi = 3.14
  r = int(input('Nhập vào bán kính của hình tròn:'))
  if r > 0:
   S = pi * r**2
   P =  2 * pi * r
   print('S= ',S,'P= ',P)
  else:
      print('Bán kính không hợp lệ')
else:
  print("Hình không hợp lệ. Vui lòng nhập v, n, hoặc t.") 
