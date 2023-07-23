import os

import findspark
findspark.init(spark_home='D:\\bigdata\spark-3.2.0-bin-hadoop3.2')
from pyspark.sql import SparkSession
import json
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StringType, IntegerType, LongType

# os.environ['JAVA_HOME']='E:\jdk-11.0.6'
# os.environ["JAVA_HOME"] = '/usr/local/jdk-15.0.1'

session = SparkSession.builder.appName("json").master("local[*]").getOrCreate()

sc = session.sparkContext
df = session.read.format('json').option("multiline", True).load('../test_data/address.json')


# print(df.printSchema())
print(df.show(3))