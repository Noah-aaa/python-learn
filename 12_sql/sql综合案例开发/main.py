"""
面向对象，数据分析案例，主业务逻辑代码

"""
from pymysql import *
from file_define import *
from data_define import *
from pyecharts.charts import *
from pyecharts.options import *
from pyecharts.globals import *

text_file_reader = TextFileReader("D:/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("D:/2011年2月销售数据JSON.txt")

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

# 合并数据
all_data: list[Record] = jan_data + feb_data

# 构建Connection

conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    autocommit=True
)

# 构建游标对象
cursor = conn.cursor()

# 选择数据库
conn.select_db("py_sql")

# 组织SQL语言
for record in all_data:
    sql = f"insert into orders values('{record.date}','{record.order_id}',{record.money},'{record.province}')"
    cursor.execute(sql)

# # 查询结果
# cursor.execute("select * from orders;")
# results=cursor.fetchall()
# print(results)
# 关闭链接
conn.close()