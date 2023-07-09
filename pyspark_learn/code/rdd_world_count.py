from pyspark import SparkContext, SparkConf
import os
os.environ["JAVA_HOME"]='/usr/local/jdk-15.0.1'

# 构建sparkContext 对象
conf = SparkConf().setAppName("test").setMaster("local[*]")

sc = SparkContext(conf=conf)

rdd = sc.textFile("../test_data/words.txt")

rdd = rdd.flatMap(lambda x: x.split(" ")).map(lambda x:(x, 1)).reduceByKey(lambda x , y: x + y)
print(rdd.collect())
