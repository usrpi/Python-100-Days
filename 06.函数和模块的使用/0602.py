"""
判断一个数是不是回文数

Version: 0.1
Author: usrpi
date: 2020-08-07
"""
def is_palindrome(num):
    """判断一个数是不是回文数"""
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num
x = int(input("x:"))
print(is_palindrome(x))