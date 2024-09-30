import scrapy
import re

from myspider.items import DoubanItem


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250?start=0&filter="]

    url = "https://movie.douban.com/top250?start=%d&filter="

    page_num = 0

    def parse(self, response):
        res_data = response.xpath("//div[@class='info']")

        item = DoubanItem()

        for ls_data in res_data:
            # 电影名称
            item["film_name"] = ls_data.xpath("./div/a/span[1]/text()").extract_first()

            # 电影导演+主演       注意：电影导演和主演在网页中是放在同一个p标签下，所以要进行特殊处理！
            film_author_actor = ls_data.xpath("./div[2]/p/text()").extract()[0].strip()

            # 电影导演            反复观察可知：if中的为电影导演和主演靠三个\xa0，即空格分开，电影导演在前！    else中的为电影信息只有导演，连主演的主都没的！
            if "主" in film_author_actor:
                film_author_test = re.findall(': (.*)\\xa0', film_author_actor)[0].strip()
                item["film_author"] = re.sub('\\xa0', '', film_author_test)
            else:
                film_author_test = re.findall(': (.*)', film_author_actor)[0]
                item["film_author"] = re.sub('\\xa0', '', film_author_test)

            # 电影主演             注意：有个别电影没有主演信息！（仅有一个主字或者主演两个字的！通过if筛选掉！)
            if "主演" in film_author_actor and len(re.findall('\\xa0主演: (.*)', film_author_actor)) == 1:
                film_actor_test = re.findall('\\xa0主演: (.*)', film_author_actor)[0].strip()
                item["film_actor"] = re.sub('\\xa0', '', film_actor_test)
            else:
                item["film_actor"] = "空"

            # 电影分类             注意：分类信息中有些不必要的空格，通过re中的sub方法删除！
            film_category_test = ls_data.xpath("./div[2]/p/text()").extract()[1].strip()
            item["film_category"] = re.sub('\\xa0', '', film_category_test)

            # 电影评分
            item["film_score"] = ls_data.xpath("./div[2]/div/span[2]/text()").extract_first()
            yield item

        if self.page_num < 225:  # 发起请求的条件
            self.page_num += 25
            url = (self.url % self.page_num)
            # 手动发起请求,调用parse再去解析
            yield scrapy.Request(url=url, callback=self.parse)
