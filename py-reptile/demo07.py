import requests
import os
from bs4 import BeautifulSoup

# 爬取csdn 文章

url = ("https://blog.csdn.net/qq_44907926/article/details/120377769?ops_request_misc=%257B%2522request%255Fid%2522"
       "%253A%2522169674531916800186544078%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D"
       "&request_id=169674531916800186544078&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~blog"
       "~first_rank_ecpm_v1~hot_rank-2-120377769-null-null.nonecase&utm_term=python%20%E5%8F%8D%E7%88%AC&spm=1018"
       ".2226.3001.4450")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 "
                  "Safari/537.36"}

response = requests.get(url, headers=headers)

# 获取html文件
soup = BeautifulSoup(response.content, "lxml")

# 获取文档标签
html_str = soup.find(id='article_content')

with open("cs.html", "w", encoding='utf-8') as f:
    f.write(str(html_str))

# print(list(soup.find(id='content_views').children))
