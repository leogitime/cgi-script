#!C:\Program Files\Python\python.exe
#> python cgi-script.py 
import pymysql
# CGI处理模块
import cgi
import cgitb
cgitb.enable(display=1, logdir="/path/to/logdir")

db = pymysql.connect(host='127.0.0.1', port='3306', user='testuser', password='123456', db='test',charset='utf8')  # 连接数据库编码注意是utf8，不然中文结果输出会乱码
cursor = db.cursor()
#select * from econews;
sql = "select * from econews;"

#for i in cursor.execute(sql):
	#colum = i.text
db.commit()


# 创建 FieldStorage 的实例化
form = cgi.FieldStorage() 

# 获取数据
site_name = form.getvalue('name').encoding('utf-8')

s_sql1 = "select * from econews where keyword1 like %"+ site_name + "%;"

#s_sql2 = "select * from econews where keyword2 like %"+ site_name + "%"
#s_sql3 = "select * from econews where keyword3 like %"+ site_name + "%"
s_sql1 = s_sql1.encode('utf-8')
rows = cursor.execute(s_sql1)
#获取查询数据
data = cursor.fetchall()

#data[i][] 	0 	  1 	  2 	  3 	  4 	  5 	6
#			ID	time	title	key1	key2	key3	url
print ("Content-type:text/html")
print ()

print ("<html>")
print ("<head>")
print ("<meta charset=\"utf-8\">")
print ("<title>数据查询结果</title>")
print ("</head>")
print ("<body>")
for i in range(rows-1)
print ("<h2>%sID：%s</h2><h2>%sTIME：%s</h2><h2>%sTITLE：%s</h2><h2>%sKEYWORD1：%s</h2><h2>%sKEYWORD2：%s</h2><h2>%sKEYWORD3：%s</h2><h2>%sURL：%s</h2>" % (data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],data[i][5],data[i][6]))
print ("</body>")
print ("</html>")