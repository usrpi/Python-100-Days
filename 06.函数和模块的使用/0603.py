"""
判断一个数是否为素数
Version: 0.1
Author: usrpi
date: 2020-08-07
"""

def is_prime(num):
    """判断一个数是否为素数"""
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    return True if num != 1 else False

x = int(input('x:'))
if is_prime(x) == True:
    print('%d是素数' % x)
else:
    print('%d不是素数' % x)

