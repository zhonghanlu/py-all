# -*- coding: utf-8 -*-
import scrapy
from ..items import UbuntuItem


class ItcastSpider(scrapy.Spider):
    # 爬虫运行时的参数
    name = 'itcast'
    # 检查允许爬的域名
    allowed_domains = ['itcast.cn']
    # 1.修改设置起始的url
    start_urls = ["https://www.itcast.cn/channel/teacher.shtml#ajacaee"]

    # 数据提取的方法：接收下载中间件传过来的response，定义对于网站相关的操作
    def parse(self, response):
        # 获取所有的教师节点
        t_list = response.xpath('//div[@class="li_txt"]')
        print(t_list)
        # 遍历教师节点列表
        item = UbuntuItem()
        for teacher in t_list:
            # xpath方法返回的是选择器对象列表     extract()方法可以提取到selector对象中data对应的数据。
            item['name'] = teacher.xpath('./h3/text()').extract_first()
            item['title'] = teacher.xpath('./h4/text()').extract_first()
            item['desc'] = teacher.xpath('./p/text()').extract_first()
            yield item
