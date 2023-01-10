import re


def main():
    # 编译正则表达式返回正则表达式对象
    pattern = re.compile(r'\w+')
    # 用正则表达式匹配字符串 成功返回匹配对象 否则返回None
    res = re.match(pattern, 'thisisastring12_-34')
    # 匹配长度
    print(res.span())
    print(len(res.group()))


if __name__ == '__main__':
    main()
