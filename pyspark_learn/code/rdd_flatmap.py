#coding: utf8
from pyspark import SparkContext, SparkConf



# 构建sparkContext 对象
conf = SparkConf().setAppName("test")

sc = SparkContext(conf=conf)

rdd = sc.parallelize(["hello ahha hh", "你好 哈哈 嘿嘿", "Good Bad Hard "])
print(rdd.flatMap(lambda line: line.split(" ")).collect())

