from bs4 import BeautifulSoup

path = "/Users/itxiaohu/Desktop/test.html"

fp = open(path, "r", encoding="utf-8")
soup = BeautifulSoup(fp, "lxml")
# 第一个p标签
print(soup.p)
# 返回class属性值为nav的第一个标签
print(soup.find(class_="nav"))
# 返回class属性值为nav的所有标签
print(soup.find_all(class_="nav"))
