"""
用形参和实参的方式来做加法的函数运算
"""


def add(arg01, arg02):
    return arg01 + arg02


num01 = int(input("请输入第一个数："))
num02 = int(input("请输入第二个数："))
print(add(num01, num02))