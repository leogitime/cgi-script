#从数据库里统计关键字频率，并输出
import pymysql
import re
from sql_output import sql_output
from collections import Counter

def keyword_counts(mysql_host,mysql_port,mysql_db,mysql_user,mysql_password):
	data = sql_output(mysql_host,mysql_port,mysql_db,mysql_user,mysql_password)[0];
	rows = sql_output(mysql_host,mysql_port,mysql_db,mysql_user,mysql_password)[1];
	seq = ""
	for i in range(rows):
		seq = seq + data[i][3] +','+ data[i][4]+','+ data[i][5]+','

	#print(seq)
	l1 = re.split('\W+',seq)
	keyword_counts = Counter(l1)  
	#print(keyword_counts.most_common(5))
	return keyword_counts
most_common = keyword_counts('127.0.0.1',3306,'test','root','live4real').most_common(10)
print('<body>most_common</body>')