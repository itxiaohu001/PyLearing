import sys


def intNum():
    for i in range(5):
        yield i


y = intNum()
while True:
    try:
        print(next(y))
    except StopIteration:
        sys.exit()

