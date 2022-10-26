from ast import With
from encodings import utf_8
from sqlite3 import paramstyle
import requests

import json

# 请求地址
url = "https://movie.douban.com/j/chart/top_list"
# 需要携带的动态参数
params = {
    "type": "25",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "139",
}
# 模拟浏览器的身份验证信息
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

response = requests.get(url=url, params=params, headers=headers)
content = response.json()

# 文件位置，读写权限，编码类型
with open("crawl_film/movie.txt", "w", encoding="utf-8") as fp:
    for i in content:
        title = i["title"]
        score = i["score"]
        fp.write(title + " " + score + "\n")
