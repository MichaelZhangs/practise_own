#coding: utf8
from pyspark import SparkContext, SparkConf
import os
os.environ["JAVA_HOME"]='/usr/local/jdk-15.0.1'

# 构建sparkContext 对象
conf = SparkConf().setAppName("test").setMaster("local[*]")

sc = SparkContext(conf=conf)

rdd = sc.parallelize([("a" , 1), ("b", 1), ("c", 1),("a" , 1), ("b", 1) ])

print(rdd.reduceByKey(lambda x, y : x+y).sortByKey(True, 2).collect())
