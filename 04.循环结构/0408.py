"""
打印如下所示的三角形图案
Version: 0.1
Author: usrpi
Date: 2020-08-06
"""
row = int(input('请输入行数：'))
for i in range(row):
    for x in range(i + 1):
        print('*',end='')
    print()


for i in range(row):
    for j in range(row):
        if j < row - i -  1:
            print(' ', end='')
        else:
            print('*', end='')
    print()


for i in range(row):
    for x in range(row - i - 1):
        print(' ', end='')
    for x in range(2 * i +1):
        print('*', end='')
    print()