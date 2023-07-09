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
print(rdd.collect())

schema = StructType().add(field="name",data_type=StringType(), nullable=True).\
    add(field= "age",data_type= IntegerType(), nullable=False)

df = session.createDataFrame(rdd, schema=schema)

df.printSchema()
df.show()
