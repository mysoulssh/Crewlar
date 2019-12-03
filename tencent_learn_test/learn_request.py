import urllib.request
import urllib.parse

# 获取html文件并保存在文件中
# url = "http://www.baidu.com"

# response = urllib.request.urlopen(url=url)

# print(response.read().decode())

# with open('baidu.html', 'w', encoding='utf8') as fp:
#     fp.write(response.read().decode())

# 下载图片
# image_url = "http://b-ssl.duitang.com/uploads/item/201807/15/20180715120609_bnioy.png"
#
# response = urllib.request.urlopen(image_url)
#
# with open("images/bizi.png", 'wb') as fp:
#     fp.write(response.read())

# 代理及错误处理
url = "http://www.baidu.com/"

# 异常处理
# try:
#     response = urllib.request.urlopen(url)
#     print(response.read())
# except Exception as e:
#     print(e)

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

# 创建一个handle
url_handle = urllib.request.HTTPHandler()
# 创建一个opener
url_opener = urllib.request.build_opener(url_handle)

# 创建请求对象
request = urllib.request.Request(url=url, headers=headers)
# 使用opener来发起请求，而不是使用urlopen发起请求
response = url_opener.open(url)

print(response.read().decode())


