from pyspark import SparkContext, SparkConf
import os
import re

os.environ["JAVA_HOME"] = '/usr/local/jdk-15.0.1'
conf = SparkConf().setAppName("test")
sc = SparkContext(conf=conf)

rdd = sc.textFile("../test_data/accumulator_broadcast_data.txt")

abnormal_char = [",", ".", "!", "#", "$", "%"]

broad_value = sc.broadcast(abnormal_char)
accmu = sc.accumulator(0)

def map_filter(data):
    global accmu
    if data in broad_value.value:
        accmu += 1
    else:
        return data
res  = rdd.flatMap(lambda line: re.split("\s+", line)).filter(map_filter).map(lambda x: (x, 1)).reduceByKey(lambda x, y:x + y).sortBy(lambda x: x[1], ascending=False)
# res = rdd.flatMap(lambda line: line.split(" ")).filter(map_filter).collect()
print(res.collect())
print(accmu)









