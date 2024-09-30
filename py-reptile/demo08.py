html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story" id="66">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">999</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
from lxml import etree  # 原理和beautiful一样，都是将html字符串转换为我们易于处理的标签对象

page = etree.HTML(html_doc)  # 返回了html节点
print(type(page))  # 输出为：<class 'lxml.etree._Element'>

# 1.     根据nodename(标签名字)选取标签的时候，只会选择子标签；比如：如果是儿子的儿子则选取不到。
print(page.xpath("body"))

# 2.     /从根节点选取  一级一级筛选（不能跳）
gen = page.xpath("/html")
print(gen)

# 3.     从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。     注意：是所有符合条件的
a = page.xpath("//a")
print(a)

# 4.    .选取当前标签
p = page.xpath("//p")[0]  # 先选择p标签的第一个
print(p.xpath("."))
print(p.xpath("./b"))  # 选取当前标签下的b标签

# 5.   ..选取当前标签的父节点
a = page.xpath("//a")[0]
print(a.xpath(".."))  # a.xpath("parent::")也可获取父节点！

# 6.获取标签的属性值
bb = page.xpath('//p[@class="story"]/@id')  # 获取标签的id属性值
print(bb)

# 1.选取所有拥有属性class的p标签
j = page.xpath('//p[@class]')
print("j:", j)

# 选取所有p标签，且拥有属性class同时值为story的标签
b = page.xpath('//p[@class="story"]')
print("b", b)

# 2.选取所有的p标签，且其中a标签的文本值大于889。
print(page.xpath('//p[a>889]'))

# 3.选取属于class为story的p标签 子元素的第一个a元素。
dd = page.xpath('//p[@class="story"]/a[1]')  # 如果是在xpath里进行索引选择，是从1开始
ee = page.xpath('//p[@class="story"]/a')[0]  # 如果是从列表里进行索引选择，是从0开始
print("dd:", dd)
print("ee", ee)

# 选取属于class为story的p标签 子元素的最后一个a元素。
ss = page.xpath('//p[@class="story"]/a[last()]')
print("ss:", ss)

# 选取属于class为story的p标签 子元素的倒数第二个a元素。
rr = page.xpath('//p[@class="story"]/a[last()-1]')
print("rr", rr)

# 选取最前面的两个属于class为story的p标签的子元素的a元素。
gg = page.xpath('//p[@class="story"]/a[position()<3]')
print("gg:", gg)

# 1.用text()获取某个节点下的文本
contents = page.xpath("//p/a/text()")  # 获取文本数据  放在列表里
print(contents)

# 2.用string()获取某个节点下所有的文本
con = page.xpath("string(//p)")  # 只拿到第一个标签下的所有文本
print(con)

# 1.* 匹配任何元素节点
s = page.xpath("//p/*")  # 选择p标签的所有子元素
print(s)

# 2.@* 匹配任何属性节点
ss = page.xpath("//p/@*")  # 选取选中标签(所有p标签)的所有的属性值
print(ss)

# 选取p元素的所有a和b元素
print(page.xpath('//p/a|//p/b'))

# 选取文档中的所有a和b元素
print(page.xpath('//a|//b'))
