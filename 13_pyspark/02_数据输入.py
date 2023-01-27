from pyspark import *
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)


conf = SparkConf().setMaster("local[*]").setMaster("test_spark")
sc = SparkContext(conf=conf)

# rdd1 = sc.parallelize([1, 2, 3, 4, 5])   #直接将python数据容器转换成rdd数据
# rdd2 = sc.parallelize((1, 2, 3, 4, 5))
# rdd3 = sc.parallelize("abcdeg")
# rdd4 = sc.parallelize({1, 2, 3, 4, 5})
# rdd5 = sc.parallelize({"key1":"value1", "key2":"value2"})
#
# # 如果要查看rdd里面有什么内容，需要用collect()方法
#
# print(rdd1.collect())
# print(rdd2.collect())
# print(rdd3.collect())
# print(rdd4.collect())
# print(type(rdd5.collect()))  # 打印出来之后是列表，
#
# sc.stop()

# 通过文件读进来

rdd = sc.textFile("D:/Pycharm/python-learn/13_pyspark/hello.txt")  # 将文件转换成rdd对象
print(rdd.collect())  # 读出结果是列表