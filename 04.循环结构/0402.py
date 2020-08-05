"""
用for循环实现1~100求和

Version: 0.1
Author: usrpi
"""
sum = 0
#for x in range(100,0,-2): #从100开始，步长为-2，递减到2
for x in range(2,101,2): #从2开始，步长为2，递增到100
    sum += x
print(sum)
