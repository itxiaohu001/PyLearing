import sys

list1 = [8, 3, 5, 5]
# 迭代器
t = iter(list1)
while True:
    try:
        print(next(t))
    except StopIteration:
        sys.exit()

