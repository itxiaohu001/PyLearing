from wsgiref import headers
from bs4 import BeautifulSoup
import requests

url = "https://mirrors.aliyun.com/pypi/simple/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
resp = requests.get(url=url, headers=headers)
resp.encoding = resp.apparent_encoding
html = resp.text

soup = BeautifulSoup(html, "lxml")

list = soup.select("a")

with open("crawl_film\pypi.txt", "w") as fp:
    for l in list:
        fp.write(l["href"]+"\n")
