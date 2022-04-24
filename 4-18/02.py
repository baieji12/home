"""
控制台输入任意字符存入集合中直到空字符串停止
"""
set01 = set()
while True:
    item = input("请输入任意字符：")
    if item == "":
        break
    else:
        set01.add(item)
print(f"您往集合中添加了如下数据：{set01}")