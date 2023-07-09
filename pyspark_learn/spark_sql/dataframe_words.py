from pyspark.sql import SparkSession
import os
from pyspark.sql import functions as F

os.environ["JAVA_HOME"] = '/usr/local/jdk-15.0.1'

session = SparkSession.builder.appName("test").master("local[*]").getOrCreate()

sc = session.sparkContext

# df = session.read.format("csv").\
#     schema("id INT, subject STRING, score INT").\
#     load("../test_data/sql/stu_score.txt")

# TODO 1 sql 风格进行处理
rdd = sc.textFile("../test_data/words.txt").flatMap(lambda line: line.split(" ")). \
    map(lambda x: [x])
print(rdd.collect())

df = rdd.toDF(["word"])

df.createTempView("words")

session.sql('''select word, count(*) as c from words group by  word order  by c DESC ''').show()

#TODO  DSL 风格
df = session.read.format("text").load("../test_data/words.txt")
df2 = df.withColumn("value", F.explode(F.split(df['value'], " ")))
print(df2.groupBy("value"). \
      count().toJSON().collect())

df2.groupBy("value"). \
      count().\
      orderBy("count", ascending=True). \
      show()


