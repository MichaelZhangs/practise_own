from pyspark.sql import SparkSession
import os
import pandas as pd
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StringType, IntegerType, LongType

os.environ["JAVA_HOME"] = '/usr/local/jdk-15.0.1'

session = SparkSession.builder.appName("test").master("local[*]").getOrCreate()

sc = session.sparkContext

df = session.read.format("csv"). \
    option("sep", ";"). \
    option("header", True). \
    load("../test_data/sql/people.csv")

df.dropDuplicates().show()

df.dropDuplicates(["name", "age"]).show()

# 缺失值处理
df.dropna().show()
# 至少满足2个有效列 ， 否则删除
df.dropna(thresh=1).show()

#对缺失列进行填充
df.fillna("lost").show()

