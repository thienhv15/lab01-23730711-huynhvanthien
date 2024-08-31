# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 22:26:16 2024

@author: Admin
"""
h1 = int(input('Nhập giờ h1='))
p1 = int(input('Nhập phút p1='))
g1 = int(input('Nhập giây g1='))
print(f'Giờ, phút, giây ở phương trình 1 là: {h1}:{p1}:{g1}')
h2 = int(input('Nhập giờ h2='))
p2 = int(input('Nhập phút p2='))
g2 = int(input('Nhập giây g='))
print(f'Giờ, phút, giây ở phương trình 2 là: {h2}:{p2}:{g2}')
tonggiay1=h1*60*60+p1*60+g1
tonggiay2=h2*60*60+p2*60+g2
phepcong=tonggiay1+tonggiay2
pheptru=abs(tonggiay1-tonggiay2)
giocong=phepcong//3600
phutcong=(phepcong%3600)//60
giaycong=phepcong%60
giotru=pheptru//3600
phuttru=(pheptru%3600)//60
giaytru=pheptru//60
print(f'Kết quả phép cộng 2 giờ là: {giocong}:{phutcong}:{giaycong}')
print(f'Kết quả phép trừ là: {giotru}:{phuttru}:{giaytru}')