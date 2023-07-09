from pyspark.sql import SparkSession
import os
from pyspark.sql.types import StructType, StringType, IntegerType

os.environ["JAVA_HOME"] = '/usr/local/jdk-15.0.1'

session = SparkSession.builder.appName("test").master("local[*]").getOrCreate()

# 构建structType
schema = StructType().add("data", StringType(), nullable=True)

df = session.read.format("text").\
    schema(schema=schema).\
    load("../test_data/sql/people.txt")
df.printSchema()
df.show()





