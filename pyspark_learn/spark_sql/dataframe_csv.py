from pyspark.sql import SparkSession
import os
from pyspark.sql.types import StructType, StringType, IntegerType

os.environ["JAVA_HOME"] = '/usr/local/jdk-15.0.1'

session = SparkSession.builder.appName("test").master("local[*]").getOrCreate()

# CSV
df = session.read.format("csv").\
    option("sep", ";").\
    option("header", True).\
    option("encoding", "utf-8").\
    schema("name STRING, age INT, job STRING" ).\
    load("../test_data/sql/people.csv")

df.printSchema()
df.show()

df.where("age is null").show()
print(df.count())