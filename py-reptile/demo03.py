html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup

# 第一个参数：上述HTML字符串；第二个参数：解析器的类型（使用lxml）——完成BeautifulSoup对象的初始化！
soup = BeautifulSoup(html_doc, "lxml")  # 将html转化为可操作的对象
# print(type(soup))
#
# # print(soup.prettify())
#
# print(soup.title)  # 获取title标签
# print(soup.title.name)  # 获取title标签的标签名         获取节点名称，调用name属性即可！
# print(soup.title.string)  # 获取title标签的文本内容
# print(soup.title.parent)  # 获取title标签的父标签
# print(soup.find(id="link2"))  # 找到id=link2的标签
#
# print("我是Tag对象：", type(soup.a))
#
# # 1.获取标签             仅获取第一个符合条件的标签，其他后面的节点都会忽略！
# print(soup.a)  # 输出为：<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
#
# # 2.获取属性             仅获取第一个符合条件的标签的属性值
# print(soup.a["href"])  # 输出为：http://example.com/elsie
#
# print(soup.p.attrs)
# print(soup.p.attrs['name'])
#
# # 第一种方法：
# print(soup.a.text)
# print(soup.a.get_text())
#
# # 第二种方法：
# print(soup.body.get_text())  # 注意：这个方法会获取选中标签下的所有文本内容
#
body = soup.body
# print(body)
#
# print(body.contents)
#
# print()
#
# tags = soup.children
# print(list(tags))
#
# print('='*20)
#
# tags_des = body.descendants  # 打印body.descendants可知这是个生成器。获取的是后代（子孙）标签
# print(list(tags_des))


# p = body.p  # 可以一层层获取指定标签,但是也只可以获取第一个符合条件的标签
# print(p)
#
# print(p.next_sibling.next_sibling)
#
# print(body.previous_sibling.previous_sibling)
#
# print(p.parent)
#
# print('='*20)
#
# print(list(p.parents))


# p = body.p
# print(p.string)
#
# gg = body.strings  # 返回的是一个generator（生成器）
# print(type(gg))
# print(list(gg))
#
# print('*' * 40)
#
# print(list(body.stripped_strings))  # 会发现这个返回的相比上面直接用strings的区别：没有了空白行


print(soup.find_all("p"))

print(soup.find_all(["p", "a"]))

print('*' * 40)

print(soup.find_all(attrs='story'))

print(soup.find_all(string="Elsie"))

print(soup.find_all("a", string="Elsie"))

print(soup.find_all("a", text="Elsie")[0]["href"])




