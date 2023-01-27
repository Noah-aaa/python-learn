from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:\Python\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("spark_test")
sc = SparkContext(conf=conf)


rdd = sc.parallelize([1, 2, 3, 4, 5])


# 通过map方法将全部数字乘以10
def func(data):
    return data*10

rdd2 = rdd.map(func)  # 通过map方法将rdd中的所有元素进行数据操作。


# (T) -> U

print(rdd2.collect())

# 对rdd每个元素进行处理，链式调用
