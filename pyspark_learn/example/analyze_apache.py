from pyspark import SparkContext, SparkConf
from pyspark.storagelevel import StorageLevel
import os


os.environ["JAVA_HOME"] = '/usr/local/jdk-15.0.1'
conf = SparkConf().setAppName("test")
sc = SparkContext(conf=conf)

rdd = sc.textFile("../test_data/apache.log")

# TODO 计算当前网站访问的PV
res = rdd.count()
print(res)
# 当前访问的UV
user_rdd = rdd.map(lambda line: (line.split(" ")[0], 1)).reduceByKey(lambda x, y: x+y)
print(user_rdd.count())
# 统计访问的ip
print(user_rdd.map(lambda x:x[0]).collect())