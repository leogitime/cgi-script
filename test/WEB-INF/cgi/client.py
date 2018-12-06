#coding:utf8
import psutil
import urllib.parse
import urllib.request
test_data = {'mem':psutil.virtual_memory().percent,'cpu':psutil.cpu_percent()}
test_data_urlencode = urllib.parse.urlencode(test_data).encode('utf8')#把字典转为urlencode格式并解码为字节流
requrl = "http://127.0.0.1:8080/cgi-bin/updata.py"
req = urllib.request.Request(url=requrl,data=test_data_urlencode)#url带参数去请求服务器
res_data = urllib.request.urlopen(req)#提交请求
