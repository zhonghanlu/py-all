import os

import requests


class TiebaSpider:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = "https://tieba.baidu.com/f?kw=" + tieba_name + "&ie=utf-8&pn={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

    # 构造url 列表
    def get_url_list(self):
        return [self.url_temp.format(i * 50) for i in range(5)]

    # 发送请求，获取响应
    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    # 保存
    def save_html_str(self, html_str, page_num):
        file_path = "{}_第{}页.html".format(self.tieba_name, page_num)
        dir = "ceshi"
        if not os.path.exists(dir):
            os.mkdir(dir)
        file_path = dir + '/' + file_path
        with open(file_path, "w", encoding='utf-8') as f:
            f.write(html_str)
        print("保存成功")

    # 实现主要逻辑
    def run(self):
        # 构造url列表
        url_list = self.get_url_list()
        # 发送请求获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            # 保存
            page_num = url_list.index(url) + 1
            self.save_html_str(html_str, page_num)


if __name__ == '__main__':
    name_data = input("请输入你想知道的内容：")
    tieba_spider = TiebaSpider(name_data)
    tieba_spider.run()
