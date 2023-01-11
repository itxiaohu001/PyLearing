set1 = {'a', 'b', 'r'}
print('a' in set1)

set2 = {'b', 'c'}
set3 = set1 - set2
print(set3)

# 两个集合的并集
set4 = set1 | set2
print(set4)

# 两个集合的交集
set5 = set1 & set2
print(set5)

# 两个集合的差集
set6 = set1 ^ set2
print(set6)

# 添加元素
set1.add('i')
print(set1)

# 删除元素
set1.discard('i')
# 此方法如果元素不存在会报错
set1.remove('a')
print(set1)
