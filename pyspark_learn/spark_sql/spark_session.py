#coding:utf8


from pyspark.sql import SparkSession
import os


os.environ["JAVA_HOME"] = '/usr/local/jdk-15.0.1'

session = SparkSession.builder.appName("test").master("local[*]").getOrCreate()

sc = session.sparkContext

# SparkSQL
df = session.read.csv("../test_data/stu_score.txt", sep=",", header=False)
df2 = df.toDF("id", "name", "score")
print(df2.printSchema())
print(df2.show())
df2.createTempView("score")

# SQL
session.sql(''' select * from score where name='语文' limit 5 ''').show()
# DSL
df2.where("name='语文'").limit(5).show()