import urllib.request

# 获取html文件并保存在文件中
# url = "http://www.baidu.com"

# response = urllib.request.urlopen(url=url)

# print(response.read().decode())

# with open('baidu.html', 'w', encoding='utf8') as fp:
#     fp.write(response.read().decode())

# 下载图片
image_url = "http://b-ssl.duitang.com/uploads/item/201807/15/20180715120609_bnioy.png"

response = urllib.request.urlopen(image_url)

with open("images/bizi.png", 'wb') as fp:
    fp.write(response.read())

