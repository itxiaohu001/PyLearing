from bs4 import BeautifulSoup

path = "/Users/itxiaohu/Desktop/test.html"

path2 = "C:/Users/Xmirror/Desktop/test.html"

fp = open(path2, "r", encoding="utf-8")
soup = BeautifulSoup(fp, "lxml")
# 第一个p标签
# print(soup.p)

# 返回class属性值为nav的第一个标签
# print(soup.find(class_="nav"))
# 返回class属性值为nav的所有标签
# print(soup.find_all(class_="nav"))

# 返回所有class属性值为top-nav-info的div标签
# print(soup.findAll("div",class_="top-nav-info"))

# id选择器,返回id值进行定位
# print(soup.select("#inp-query"))

# class选择器，根据class标签进行定位
# print(soup.select(".top-nav-info"))

# 标签选择器,返回所有的li标签
# print(soup.select("li"))

# 层级选择器,返回div下的所有ul标签中class值为on的标签
# print(soup.select("div>ul>.on"))

# 从标签中提取文本内容
# string属性返回的是指定标签的直系文本，即直接存在于该标签中的文本，而不是存在于该标签下的其他标签中的文本。text属性返回的则是指定标签下的所有文本。
# print(soup.select(".top-nav-info")[0].string)
# print(soup.select(".top-nav-info")[0].text)

# 从标签中提取属性,返回第一个class值为nav的标签的id属性值
print(soup.find(class_="nav")["id"])