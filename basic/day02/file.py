def main():
    # 一次性读取整个文件内容
    try:
        with open('../day01/class.py', 'r', encoding='utf-8') as f:
            for line in f:
                print(line, end='')
    except FileNotFoundError:
        print('无法打开指定的文件')
    except LookupError:
        print('指定了未知的编码')
    except UnicodeDecodeError:
        print('解码错误')


if __name__ == '__main__':
    main()
