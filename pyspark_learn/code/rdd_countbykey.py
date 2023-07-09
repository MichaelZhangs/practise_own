from pyspark import SparkContext, SparkConf

import os

os.environ["JAVA_HOME"] = '/usr/local/jdk-15.0.1'
conf = SparkConf().setAppName("test")
sc = SparkContext(conf=conf)

rdd = sc.textFile("../test_data/words.txt")

s = rdd.flatMap(lambda line: line.split(" ")).map(lambda x: (x, 1)).countByKey()
print(s.items())
print(type(s))
print(s.get("hello"))

print(rdd.flatMap(lambda line: line.split(" ")).reduce(lambda x, y: x + y))

rdd = sc.parallelize([1, 2, 0, 9, 3, 4, 5, 6, 7, 8, 10], 4)

print(rdd.takeSample(True, 3))
print(rdd.takeOrdered(3))
print(rdd.top(3))
print(rdd.top(4, lambda x: -x))
print(rdd.takeOrdered(4, lambda x: -x))

print("RDD foreach")
print(rdd.foreach(lambda x: x * 10))


# rdd.saveAsTextFile("./num.txt")

def f(iter):
    res = []
    for it in iter:
        res.append(it * 10)
    return res


res = rdd.mapPartitions(lambda iter: [i * 10 for i in iter], True).collect()

print(res)

print(rdd.foreachPartition(lambda iter: [i * 20 for i in iter]))

