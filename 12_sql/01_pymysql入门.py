# 导包
from pymysql import Connection

# 构建MySQL数据库链接
conn = Connection(
    host="localhost",  # 主机名(IP地址也可以，127.0.0.1)
    port=3306,  # 端口名
    user="root",  # 用户名
    password="123456"  # 密码
)

print(conn.get_server_info())
# 执行非查询性质的SQL
cursor = conn.cursor()
# 选择数据库
conn.select_db("test")  
# 执行sql
# cursor.execute("create table test_pymysql(id int);")  # 分号可以写，可以不写
cursor.execute("select * from student;")
# 获得查询结果
results = cursor.fetchall()  # 得到一个元组。tuple()
for r in results:
    print(r)

# 关闭链接
conn.close()