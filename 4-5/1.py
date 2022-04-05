list01 = ["谢谢惠顾", "一等奖", "谢谢回顾", "三等奖", "谢谢回顾", "二等奖"]
res = int(input("输入中奖号码："))
if 0 < res < len(list01):
    info = list01[res - 1]
    print(f"{info}")
else:
    print('请选择正确中将区域')
