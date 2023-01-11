# 元组与列表很相似，不同在于元组的元素不能修改
# 元组使用()，列表使用[]

tuple1 = (1, 3, 4, 5, 'google')
print(tuple1)
# 元组可以转换为列表
print(list(tuple1))

# 正向索引
print(tuple1[0])
# 反向索引
print(tuple1[-1])

# 截取
print(tuple1[1:3])

# 元组拼接
tup1 = (1, 3)
tup2 = (5, 6)
tup3 = tup1 + tup2
print(tup3)

# 删除元组
del tup3

# 元组地址
print(id(tup1))
