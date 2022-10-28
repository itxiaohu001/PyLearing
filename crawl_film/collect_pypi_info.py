import requests
from bs4 import BeautifulSoup


_prefix = "https://mirrors.aliyun.com/pypi/simple/"
_prefix_down = "https://mirrors.aliyun.com/pypi/"
_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
_pypi_file_path = "crawl_film/pypi.txt"


def get_url(path):
    l = []
    with open(path, "r") as fp:
        c = 0
        while c < 5:
            c += 1
            line = fp.readline().replace("\n", "")
            url = _prefix + line
            l.append(url)
            if not line:
                continue
    return l


def analyze_link_pkg(link):
    resp = requests.get(url=link, headers=_headers)
    html_text = resp.text
    soup = BeautifulSoup(html_text, "lxml")
    index_a_list = soup.select("a")
    for index in index_a_list:
        suffix = index["href"].replace("../../","")
        down_addr = _prefix_down + suffix
        pkg_name = index.string
        try:
            resp = requests.get(down_addr)
            pkg = resp.content
            save_adr = "crawl_film/file/" + pkg_name
            with open(save_adr,"wb") as f:
                f.write(pkg)
        except:
            print(suffix)


url_list = get_url(_pypi_file_path)
for ul in url_list:
    analyze_link_pkg(ul)