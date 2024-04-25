#导入数据库包的连接方法
from pymysql import Connection

#获取MySQL数据库连接对象
conn = Connection(
    host='1.94.34.99',
    port=3306,
    user='root',
    password='dao5049jin64',
    autocommit=True             #设置自动提交确认数据变更
)
#print(conn.get_server_info())

#通过连接对象的cursor方法创建游标对象
cursor = conn.cursor()
#cursor.execute("create database jinpengcheng")
conn.select_db("jinpengcheng")      #打开test数据库
#使用游标对象，执行sql语句,创建表，添加数据
#cursor.execute("create table test_pymysql(id int,info varchar(255))")
"""
#查询表
cursor.execute("select user,host from user")    #查询后返回一个元组
results: tuple = cursor.fetchall()     #用fetchall方法返回查询的元组
for r in results:
    print(r)
"""

cursor.execute("insert into test_pymysql (id,info) value('003','陈凯'),('004','张先锋')")
#执行插入语句后要通过链接对象提交确认
#conn.commit()

#数据读取


#关闭链接
conn.close()