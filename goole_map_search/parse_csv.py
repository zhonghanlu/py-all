import random

import pandas as pd
import requests as req
from bs4 import BeautifulSoup
import xlwings as xw

from excel_pic import add_center

# 创建一个新的Excel工作簿

data = ["店名", "地址", "营业电话", "店铺首页图片地址", "主页地址"]

# 给请求指定一个请求头来模拟chrome浏览器
agents = [
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5',
    'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
    'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1'
]


def parse_csv(read_file, write_file):
    df = pd.read_csv(read_file)
    df.columns.values[1] = "店名"
    df.columns.values[6] = "地址"
    df.columns.values[10] = "营业电话"
    df.columns.values[11] = "店铺首页图片地址"
    df.columns.values[0] = "主页地址"

    data_to_write = df[data]
    data_to_write.to_csv(write_file + ".csv")

    # 处理首页图片
    handler_pic(write_file)


def handler_pic(handler_file):
    df = pd.read_csv(handler_file + ".csv")

    with pd.ExcelWriter(handler_file + ".xlsx", engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Sheet1', index=False)
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    worksheet.set_column('A:G', 5000)  # 设置列宽为20个字符宽度   未生效

    for index, row in df.iterrows():
        wb = xw.Book(handler_file + ".xlsx")
        sht = wb.sheets['Sheet1']
        header = {"User-Agent": random.choice(agents)}

        # 插入图片
        shop_url = row[5]
        if str(shop_url).startswith("http"):
            r = req.get(shop_url, headers=header)
            r.raise_for_status()

            soup = BeautifulSoup(r.text, features="html.parser")
            res = soup.find("meta", property="og:image")
            pic_url = res.get("content")

            # 处理网页图片路径
            if str(pic_url).startswith("http"):
                pic_response = req.get(pic_url, headers=header)
                pic_response.raise_for_status()

                # 保存图片到本地
                try:
                    with open("./img/" + pic_url.split('/')[-1] + ".PNG", 'wb') as file:
                        file.write(pic_response.content)

                    filePath = "D:\py_project\goole-shop-etl\goole-shop-etl" + "./img/" + pic_url.split('/')[
                        -1] + ".PNG"
                    add_center(sht, 'H' + str(index + 2), filePath)  # 默认值
                    print("已经完成：" + str(index) + "个")
                except Exception as e:
                    print(e)
                    continue


if __name__ == '__main__':
    parse_csv("D:\py_project\goole-shop-etl\goole-shop-etl\google.csv",
              "D:\py_project\goole-shop-etl\goole-shop-etl\google_handler")
