"""
判断输入的正整数是不是回文素数
Version: 0.1
Author: usrpi
date: 2020-08-07
"""
from m0602 import is_palindrome
from m0603 import is_prime
if __name__ == '__main__':
    num = int(input('请输入正整数：'))
    if is_palindrome(num) and is_prime(num):
        print('%d是回文数' % num)