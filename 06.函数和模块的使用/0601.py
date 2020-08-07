
"""
求最大公约数和最小公倍数

Version: 0.1
Author: usrpi
date: 2020-08-07
"""
def gcd(x, y):
    """求最大公约数"""
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    """求最小公倍数"""
    return x * y // gcd(x, y)

x = int(input('x:'))
y = int(input('y:'))
print('最大公约数为%d' % gcd(x,y))
print('最小公倍数为%d' % lcm(x,y))