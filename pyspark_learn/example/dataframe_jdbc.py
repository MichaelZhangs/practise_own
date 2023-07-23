from pyspark.sql import SparkSession

from pyspark.sql.types import StructType , IntegerType, StringType

import findspark

findspark.init(spark_home='D:\\bigdata\spark-2.4.7-bin-hadoop2.7')

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


# 存入数据库 JDBC
# df.write.mode("overwrite").\
#     format("jdbc"). \
#     option("url","jdbc:mysql://localhost:3306/bigdata?useSSL=false&characterEncoding=UTF-8&useUnicode=true&serverTimezone=UTC").\
#     option("dbtable", "movie_data"). \
#     option("user", 'root'). \
#     option('password', '123456'). \
#     save()

# 从数据库读取
df2 = session.read.format('overwrite'). \
    format("jdbc"). \
    option("url",
           "jdbc:mysql://localhost:3306/bigdata?useSSL=false&characterEncoding=UTF-8&useUnicode=true&serverTimezone=UTC"). \
    option("dbtable", "movie_data"). \
    option("user", 'root'). \
    option('password', '123456'). \
    load()

df2.printSchema()
df2.show()