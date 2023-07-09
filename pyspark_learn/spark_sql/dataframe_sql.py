from pyspark.sql import SparkSession
import os
from pyspark.sql.types import StructType, StringType, IntegerType

os.environ["JAVA_HOME"] = '/usr/local/jdk-15.0.1'

session = SparkSession.builder.appName("test").master("local[*]").getOrCreate()

sc = session.sparkContext

df = session.read.format("csv").\
    schema("id INT, subject STRING, score INT").\
    load("../test_data/sql/stu_score.txt")

df.createTempView("score")
df.createOrReplaceTempView("score_2")
df.createGlobalTempView("score_3")  # 使用时需要前缀 global_temp.表名

session.sql('''select subject, count(*) from score group by subject''').show()

session.sql('''select subject, count(*) from score_2 group by subject''').show()

session.sql('''select subject, count(*) from global_temp.score_3 group by subject''').show()


