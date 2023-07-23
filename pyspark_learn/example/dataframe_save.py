from pyspark.sql import SparkSession
import os
from pyspark.sql import functions as F
from pyspark.sql.types import StructType , IntegerType, StringType


os.environ["JAVA_HOME"] = '/usr/local/jdk-15.0.1'

session = SparkSession.builder.appName("test").master("local[*]").getOrCreate()

sc = session.sparkContext
schema = StructType().\
    add(field="user_id", data_type=IntegerType(), nullable=True).\
    add(field="movie_id", data_type=IntegerType(), nullable=True). \
    add(field="score", data_type=IntegerType(), nullable=True). \
    add(field="time", data_type=StringType(), nullable=True)
# 读取数据集
df = session.read.format("csv").\
    option("sep", "\t"). \
    option("header", False). \
    option("encoding", 'utf-8'). \
    schema(schema=schema). \
    load("../test_data/sql/u.data")

df.toDF(schema)
# JDBC
df.write.mode("overwrite").\
    format("jdbc"). \
    option("url","jdbc:mysql://localhost:3308/bigdata?useSSL=false&useUnicode=true").\
    option("tbtable", "movie_data"). \
    option("user", 'root'). \
    option('password', '123456'). \
    save()

# # write text
# df.select(F.concat_ws("---", "user_id", "movie_id", "score", "time")). \
#     write. \
#     mode('overwrite'). \
#     format("text"). \
#     save("../test_data/sql/text")
#
# # write csv
# df.write.mode("overwrite"). \
#     format("csv"). \
#     option('sep', ';'). \
#     option('header', True). \
#     save('../test_data/sql/csv')
#
# # write json
# df.write.mode('overwrite'). \
#     format('json'). \
#     save('../test_data/sql/json')
# #
# # # write parque
# df.write.mode('overwrite'). \
#     format('parquet'). \
#     save('../test_data/sql/parquet')

