listNum = [1, 2, 3, 5]
listStr = ['h', 'i', 'j']
listMix = [1, 2, 3, 'k']

# 正向索引
print(listStr[0])
# 反向索引
print(listMix[-1])
# 列表截取(左闭右开)
print(listMix[0:3])

# 更新列表
listNum.append(6)
print(listNum)
# 删除元素
del listNum[0]
print(listNum)

# 嵌套列表
listInsert = [1, [2, 3], 4]
print(listInsert)
