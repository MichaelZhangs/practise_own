from pyspark.sql import SparkSession
import os
from pyspark.sql.types import StructType, StringType, IntegerType

os.environ["JAVA_HOME"] = '/usr/local/jdk-15.0.1'

session = SparkSession.builder.appName("test").master("local[*]").getOrCreate()

df = session.read.format("parquet").nload("../test_data/sql/users.parquet")

df.printSchema()
df.show()