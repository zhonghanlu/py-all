import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://baike.baidu.com/item/%E7%99%BE%E5%BA%A6%E6%96%87%E5%BA%93/4928294?fr=aladdin')

# 执行JS代码，滑动网页至最底部！
js = 'window.scrollTo(0, document.body.scrollHeight)'
browser.execute_script(js)

# 执行JS代码，弹窗提示文字！
browser.execute_script('alert("到达最底部啦！")')

time.sleep(3)
