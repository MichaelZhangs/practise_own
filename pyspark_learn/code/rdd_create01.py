#coding: utf8
from pyspark import SparkContext, SparkConf

# 构建sparkContext 对象
conf = SparkConf().setAppName("test")

sc = SparkContext(conf=conf)

#本地集合， 到RDD 的对象
rdd = sc.parallelize([1,2,3,4,5,6,7,8,9])

# 没有给定分区数, 默认根据CPU 核心数量
print("默认分区数: ", rdd.getNumPartitions())

rdd2 = sc.parallelize([1,2,3], 3)
print("指定分区数： ", rdd2.getNumPartitions())

print("rdd 的集合: ", rdd.collect())


