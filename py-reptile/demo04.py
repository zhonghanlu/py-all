from selenium import webdriver  # 控制浏览器的模块
from selenium.webdriver.common.by import By
import time  # 加入睡眠，不然运行的太快了录屏效果不行！
from selenium.webdriver.common.action_chains import ActionChains

# 示例：
#     1. 导包：from selenium.webdriver.common.action_chains import ActionChains
#     2. 实例化ActionChains对象：Action=ActionChains(driver)
#     3. 调用右键方法：element=Action.context_click(username)
#     4. 执行：element.perform()


# 声明浏览器对象——如果是火狐浏览器的话：driver = webdriver.Firefos()
driver = webdriver.Chrome()  # 获取chrome控制对象——webdriver对象

# 1.向一个url发起请求
driver.get('http://www.baidu.com')
time.sleep(1)
# 2.定位到搜索框标签
input_tag = driver.find_element(By.ID, 'kw')
# 3.往搜索框中输入搜索内容
input_tag.send_keys('java')
# 4.定位到百度一下的搜索图标
submit_tag = driver.find_element(By.ID, 'su')
time.sleep(1)
# 5.单击搜索图标
submit_tag.click()
time.sleep(5)
# 6.一定要退出！不退出会有残留进程！！！
driver.quit()
