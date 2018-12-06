#coding:utf8
import cgi
c = cgi.FieldStorage()#获取表单参数
try:
   data1 =  c['mem'].value#获取表单中mem的值
   data2 =  c['cpu'].value#获取表单中cpu的值
except KeyError:#如果没获取到数据，就把数据设置为空
    data1 = ''
    data2 = ''
if data1 or data2:#判断是否获取到数据
    f = open('cgi-bin/1.txt','w',encoding='utf8')#创建文件
    f.write(data1 +'%' + '\n')#写入mem的值
    f.write(data2 +'%' + '\n')#写入cpu的值
    f.close()#关闭文件