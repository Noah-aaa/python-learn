""""
演示python插入数据
"""
from pymysql import Connection

# 构建到MySQL数据库链接
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    autocommit=True  # 设置自动自动提交
)

# 执行非查询性语句
cursor = conn.cursor() # 获得游标对象
conn.select_db("students") # 选择数据库

# 插入数据返回的是影响结果的行数
len = cursor.execute("insert into student(sno,sname,ssex) values('113222223','周杰伦','男');")  # 执行sql语句，开始插入数据,

# conn.commit()  # 提交数据 通过commit进行提交类似数据库的事务提交也可以设置事务自动提交。
print(len)

# 建立查询结果对象
cursor1= conn.cursor()

# 选择数据库
conn.select_db("students")
# 执行sql语句
cursor1.execute("select * from student;")

# 获取结果得元组
results = cursor1.fetchall()

# 得到结果。为元组并进行输出
print(results)
for r in results:
    print(r)

# 得到查询结果
# results = cursor.fetchall()  # 得到一个元组(),元组中包括所有的结果。
# cursor.execute("select * from student;")
# for r in results:  #
#     print(r)
# 关闭链接

conn.close()
# 选择数据库
# conn.select_db()