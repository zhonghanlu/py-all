import requests

# 1.实例化session
session = requests.Session()

# 2.使用session发送post请求，对方服务器会把cookie设置在session中
headers = {}
post_url = ""
post_data = ""

session.post(post_url, data=post_data, headers=headers)

# 3.请求个人主页，会带上之前的cookie，能够请求成功
profile_url = ""
response = session.get(profile_url, headers=headers)

with open("renren.html","w",encoding="utf-8") as f:
    f.write(response.content.decode())
