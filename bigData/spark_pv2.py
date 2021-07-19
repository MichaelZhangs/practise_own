import os
PYSPARK_PYTHON = "/usr/bin/python3"
os.environ["PYSPARK_PYTHON"] = PYSPARK_PYTHON

from pyspark import SparkContext
sc = SparkContext("local[*]", "pv")

rdd1 = sc.textFile("file:///root/bigData/access.log").map(lambda x: ("pv", 1)).reduceByKey(lambda a, b :a + b)
print(rdd1.collect())