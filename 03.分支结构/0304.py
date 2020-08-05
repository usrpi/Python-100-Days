"""
判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积

Version: 0.1
Author: usrpi
"""
import cmath
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and b + c > a and a + c > b:
    l = a + b + c
    p = l/2
    #s =cmath.sqrt(p*(p - a)*(p - b)*(p - c))
    s =(p*(p - a)*(p - b)*(p - c))**0.5  #用三边使用海伦公式求三角形面积
    print('周长：',l)
    print('面积：',s)
else:
    print('不能构成三角形')