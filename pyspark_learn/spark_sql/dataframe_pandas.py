from pyspark.sql import SparkSession
import os
import pandas as pd


os.environ["JAVA_HOME"] = '/usr/local/jdk-15.0.1'

session = SparkSession.builder.appName("test").master("local[*]").getOrCreate()

# 基于RDD 转换成DataFrame

sc = session.sparkContext

# rdd = (sc.textFile("../test_data/sql/people.txt"). \
#        map(lambda line: line.split(","))).\
#         map(lambda x: (x[0], int(x[1])))

pdf = pd.DataFrame({
    "id": [1,2,3],
    "name": ["张三", "李四", "王五"],
    "age": [24, 26, 29]
})
df = session.createDataFrame(pdf)
df.printSchema()
df.show()

