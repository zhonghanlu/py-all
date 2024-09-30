# 窗口切换：
# 首先要获取所有标签页的窗口句柄；
# 然后利用窗口句柄切换到句柄指向的标签页。
# 窗口句柄：指的是指向标签页对象的标识！
# 解析：
# # 1.获取当前所有的标签页的句柄构成的列表
# current_windows = driver.window_handles
#
# # 2.根据标签页句柄列表索引下标进行切换
# driver.switch_to.window(windows[0])

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.baidu.com/')

time.sleep(1)
driver.find_element(By.ID, 'kw').send_keys('python')
time.sleep(1)
driver.find_element(By.ID, 'su').click()
time.sleep(1)

# 通过执行js来新开一个标签页
js = "window.open('https://www.sougou.com');"
driver.execute_script(js)
time.sleep(1)

# 1.获取当前所有的窗口
windows = driver.window_handles

time.sleep(2)
# 2.根据窗口索引进行切换
driver.switch_to.window(windows[0])
time.sleep(2)
driver.switch_to.window(windows[1])

time.sleep(6)
driver.quit()
