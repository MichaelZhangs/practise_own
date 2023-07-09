from pyspark.sql import SparkSession
import os


os.environ["JAVA_HOME"] = '/usr/local/jdk-15.0.1'

session = SparkSession.builder.appName("test").master("local[*]").getOrCreate()

# 基于RDD 转换成DataFrame

sc = session.sparkContext

rdd = (sc.textFile("../test_data/sql/people.txt"). \
       map(lambda line: line.split(","))).\
        map(lambda x: (x[0], int(x[1])))

df = session.createDataFrame(rdd,schema=["name", "age"])

df.printSchema()

df.where("age>20").show()
df.show(20, False)

df.createOrReplaceTempView("people")
session.sql(''' select * from people where age < 30 ''').show()
