list01 = ['C', 'C++', 'C#', 'Java', 'Python', 'PHP', 'Ruby', 'GoLand', 'Object-C']
print(list01)
# 增
print('========增========')
list01.append('lua')
print(f'append()：{list01}')
listAdd = ['JS', 'HTML5', 'CSS']
list01.extend(listAdd)
print(f'extend()：{list01}')
list01.insert(8, 'VB')
print(f'insert()：{list01}')
# 删
print('========删========')
del list01[-1]
print(f'del：{list01}')
list01.remove('lua')
print(f'remove()：{list01}')
list01.pop(-1)
print(f'pop()：{list01}')
list01.clear()
print(f'clear()：{list01}')
print('=================')
list01 = ['C', 'C++', 'C#', 'Java', 'Python', 'PHP', 'Ruby', 'GoLand', 'VB', 'Object-C', 'lua', 'JS', 'HTML5', 'CSS']
print(f'已重新添加：{list01}')
# 改
print('========改========')
list01[-4] = 'TypeScrip'
print(f'直接赋值：{list01}')
list01[-3::] = ['-3', '-2', '-1']
print(f'以切片：{list01}')
# 查
print('========查========')
print(f'根据下标索引：{list01[0]}')
print(f'切片-正序：{list01[0:5:1]}')
print(f'切片-倒序：{list01[-14:-9:1]}')
print(f'”Java“的下标：{list01.index("Java")}')
print(f'是否存在：{"Java" in list01}')
print(f'是不否存在：{"Java" not in list01}')
print('遍历')
for item in list01:
    print(item, end=" ")