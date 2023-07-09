from pyspark import SparkContext, SparkConf

import os

os.environ["JAVA_HOME"] = '/usr/local/jdk-15.0.1'
conf = SparkConf().setAppName("test")
sc = SparkContext(conf=conf)

rdd = sc.textFile("../test_data/words.txt")

rdd2 = rdd.flatMap(lambda line: line.split(" ")).map(lambda x: (x, 1))

rdd3 = rdd2.reduceByKey(lambda a, b : a + b )
# rdd3.cache() 
# rdd3.persist()

print(rdd3.collect())

rdd4 =  rdd3.groupByKey()
print(rdd4.map(lambda x: (x[0], list(x[1]))).collect())

rdd6 =  rdd4.mapValues(lambda x: sum(x))
print(rdd6.collect())




