#!C:\Program Files\Python\python.exe
#> python cgi-script.py 
# CGI处理模块
import cgi
import cgitb
import pymysql

cgitb.enable()
#db = pymysql.connect(host=mysql_host, port=mysql_port, user=mysql_user, password=mysql_password, db=mysql_db,charset='utf8')
db = pymysql.connect(host='127.0.0.1', port=3306, user='testuser', password='123456', db='test',charset='utf8')
cursor = db.cursor()

# 创建 FieldStorage 的实例化
form = cgi.FieldStorage()

# 获取数据
keyword = form.getvalue('keyword')
#s_sql1 = "select * from econews"
s_sql1 = "select * from econews where keyword1 like \"%"+ keyword + "%\""
rows = cursor.execute(str(s_sql1))
#获取查询数据
data = cursor.fetchall()
db.commit()
db.close()

#print("%s,%s,%s,%s,%s,%s,%s"%(data[0][0],data[0][1],data[0][2],data[0][3],data[0][4],data[0][5],data[0][6]))


#data[i][] 	0 	  1 	  2 	  3 	  4 	  5 	6
#			ID	time	title	key1	key2	key3	url
print ("Content-type:text/html")
print ()

print ("<html>")
print ("<head>")
print ("<meta charset=\'gbk2312\'>")
print ("<title>数据查询结果</title>")
print ("</head>")
print ("<body>")
#print ("<form action="http://localhost:8080/test/cgi-bin/test.py" method="post">关键字: <input type="text" name="kword">  <br/><input type="submit" value="提交" /></form>")
print ("<table border = \"1\">")
#print ("%s"%(s_sql1))
#<a href= url>url</a>
print ("<tr><th>ID</th><th>TIME</th><th>TITLE</th><th>KEYWORD1</th><th>KEYWORD2</th><th>KEYWORD3</th><th>URL</th></tr>")
for i in range(rows):
	print ("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><a href=%s>%s</a></td></tr>"%(data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],data[i][5],data[i][6],data[i][6]))
print ("</table>")
print ("<a>共%s个结果</a>"%(rows))
print ("</body>")
print ("</html>")