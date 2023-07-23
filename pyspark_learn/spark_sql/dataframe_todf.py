from pyspark.sql import SparkSession
import os
from pyspark.sql.types import StructType, StringType, IntegerType

os.environ["JAVA_HOME"] = '/usr/local/jdk-15.0.1'

session = SparkSession.builder.appName("test").master("local[*]").getOrCreate()

# 基于RDD 转换成DataFrame

sc = session.sparkContext

rdd = sc.textFile("../test_data/sql/people.txt"). \
       map(lambda line: line.split(",")).\
        map(lambda x: (x[0], int(x[1])))

df1 = rdd.toDF(["name", "age"])
df1.printSchema()
df1.show()


schema = StructType().add("name", StringType(), nullable=True). \
            add("age", IntegerType(), nullable=False)

df2 = rdd.toDF(schema)
df2.printSchema()

df2.show()

