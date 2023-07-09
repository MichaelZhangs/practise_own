from pyspark.sql import SparkSession
import os
import pandas as pd
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StringType, IntegerType, LongType

os.environ["JAVA_HOME"] = '/usr/local/jdk-15.0.1'

session = SparkSession.builder.appName("test").master("local[*]").getOrCreate()

sc = session.sparkContext

rdd = sc.textFile("../test_data/sql/u.data").map(lambda x: x.split("\t")).map(lambda x:[int(x[0]), int(x[1]), int(x[2]), int(x[3])])
print(rdd.take(3))

schema = StructType().\
    add(field="user_id", data_type=IntegerType(), nullable=True).\
    add(field="movie_id", data_type=IntegerType(), nullable=True). \
    add(field="score", data_type=IntegerType(), nullable=True). \
    add(field="time", data_type=StringType(), nullable=True)

sdf =  session.createDataFrame(rdd, schema=schema)
print(sdf['score'])
print(sdf.printSchema())
sdf.createTempView("s_movie")
session.sql('''select user_id,  avg(score) as s from s_movie  group by  user_id  order by s desc  ''').show()

# schema = StructType().add()

# 读取数据集

df = session.read.format("csv").\
    option("sep", "\t"). \
    option("header", False). \
    schema("user_id INT , movie_id INT , score INT, time INT "). \
    load("../test_data/sql/u.data")



df.createTempView("movie")

session.sql('''select user_id, round(avg(score), 2) as score from movie group by user_id order by score DESC''').show()

# DSL 风格
# df.groupBy("user_id").avg("score"). \
#     withColumnRenamed("avg(score)", "avg_score"). \
#     orderBy("avg_score", ascending=True). \
#     show()

# 电影平均分
print("电影平均分....")
df.groupBy("movie_id"). \
    avg("score"). \
    withColumnRenamed("avg(score)", "avg_score"). \
    withColumn("avg_score", F.round("avg_score", 2)). \
    orderBy("avg_score", ascending=False). \
    show()

# TODO 3  查询大于平均分的电影的数据
print("TODO 3  查询大于平均分的电影的数据 ")
print(df.select(F.avg(df["score"])).first())
print(df.where(df['score'] > df.select(F.avg(df["score"])).first()["avg(score)"]).count())
session.sql(''' select count(1) from movie where  score > (select avg(score) from movie ) ''').show()

# TODO 4 查询 高分电影(>3)打分最多的用户， 此人打分的平均分
print("TODO 4 查询 高分电影(>3)打分最多的用户， 此人打分的平均分")
user_id = df.where("score>3").groupBy("user_id").count(). \
    withColumnRenamed("count", "cnt"). \
    orderBy("cnt", ascending=False). \
    limit(1). \
    first()["user_id"]
print(user_id)
df.filter(df["user_id"]==user_id).select(F.round(F.avg('score'), 2)).show()

# TODO 5 查询 每个用户的平均分， 最高打分， 最低打分
print('TODO 5 查询 每个用户的平均分， 最高打分， 最低打分')
df.groupBy("user_id").\
    agg(
        F.round(F.avg("score"), 2).alias("avg_score"),
        F.min('score').alias('min_score'),
        F.max('score').alias('max_score')
).show()
print("sql 输出")
session.sql('''
SELECT user_id, AVG(score) AS avg_score, MAX(score) AS max_score, MIN(score) AS min_score
FROM movie
GROUP BY user_id;
''').show()

# TODO 5 查询评分超过100次的电影的平均分 排名 前10
print("查询评分超过100次的电影的平均分 排名 前10")
session.sql('''
SELECT movie_id,count(1), AVG(score) AS avg_score
FROM movie
GROUP BY movie_id
HAVING COUNT(*) > 100
ORDER BY avg_score DESC
LIMIT 10;

''').show()

df.groupBy("movie_id"). \
    agg(
    F.count("movie_id").alias('cnt'),
    F.round(F.avg('score'), 2).alias('avg_score')
).where('cnt > 100').orderBy('avg_score', ascending=False).limit(10).show()




