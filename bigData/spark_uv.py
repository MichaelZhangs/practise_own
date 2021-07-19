from pyspark.sql import SparkSession
import os
PYSPARK_PYTHON = "/usr/bin/python3"
os.environ["PYSPARK_PYTHON"] = PYSPARK_PYTHON

spark = SparkSession.builder.appName("pv").getOrCreate()
sc = spark.sparkContext
rdd1 = sc.textFile("file:///root/bigData/access.log")
#对每一行按照空格拆分，将ip地址取出
rdd2 = rdd1.map(lambda x:x.split(" ")).map(lambda x:x[0])
print(rdd2.collect())
#把每个ur记为1
rdd3 = rdd2.distinct().map(lambda x:("uv",1))
print(rdd3.collect())
rdd4 = rdd3.reduceByKey(lambda a,b:a+b)
# rdd4.saveAsTextFile("hdfs://localhost:9000/uv/result")

print(rdd4.collect())
sc.stop()