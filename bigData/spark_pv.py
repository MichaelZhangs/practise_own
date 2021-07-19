import os
PYSPARK_PYTHON = "/usr/bin/python3"
os.environ["PYSPARK_PYTHON"] = PYSPARK_PYTHON

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("pv").getOrCreate()

sc = spark.sparkContext

rdd1 = sc.textFile("file:///root/bigData/access.log")

rdd2 = rdd1.map(lambda x:("pv", 1)).reduceByKey(lambda a,b: a+b)
print(rdd2.collect())

