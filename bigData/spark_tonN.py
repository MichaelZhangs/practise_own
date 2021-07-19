from pyspark.sql import SparkSession
import os
PYSPARK_PYTHON = "/usr/bin/python3"
os.environ["PYSPARK_PYTHON"] = PYSPARK_PYTHON

spark = SparkSession.builder.appName("topN").getOrCreate()
sc = spark.sparkContext
rdd1 = sc.textFile("file:///root/bigData/access.log")
#对每一行按照空格拆分，将url数据取出，把每个url记为1
rdd2 = rdd1.map(lambda x:x.split(" ")).filter(lambda x:len(x)>10).map(lambda x:(x[10],1))
print(rdd2.collect())
#对数据进行累加，按照url出现次数的降序排列
rdd3 = rdd2.reduceByKey(lambda a,b:a+b).sortBy(lambda x:x[1],ascending=False).filter(lambda x:len(x[0]) > 6)
#取出序列数据中的前n个
print(rdd3.take(5))

sc.stop()