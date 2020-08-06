"""
猜数字游戏的规则是：计算机出一个1到100之间的随机数，玩家输入自己猜的数字，计算机给出对应的提示信息（大一点、小一点或猜对了），
如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续。

Version: 0.1
Author: usrpi
"""
import random
answer = random.randint(1,100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入数字：'))
    if number > answer:
        print('小一点')
    if number < answer:
        print('大一点')
    else:
        print('恭喜你猜对了')
        break
print('你总共踩了 %d 次' % counter)
if counter > 7:
    print('你的智商不够')
