from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType
from pyspark.sql import functions as F
from pyspark.sql.types import IntegerType, StringType, ArrayType, StructType

import os

os.environ["JAVA_HOME"] = '/usr/local/jdk-15.0.1'


session = SparkSession.builder.appName("json").master("local[*]").getOrCreate()

sc = session.sparkContext

rdd = sc.parallelize([
    ("王一", 'class_1', 60),
    ("王二", 'class_2', 70),
    ("王三", 'class_3', 80),
    ("张一", 'class_1', 60),
    ("张二", 'class_2', 70),
    ("张三", 'class_3', 80),
    ("刘一", 'class_1', 60),
    ("刘二", 'class_2', 70),
    ("刘三", 'class_3', 80),
    ("丁一", 'class_1', 60),
    ("丁二", 'class_2', 70),
    ("丁三", 'class_3', 80),
])

schema = StructType().add('name', StringType()). \
    add('class', StringType()). \
    add('score', IntegerType())

df = rdd.toDF(schema)

df.createTempView('stu')

session.sql('''
    select * , AVG(score) OVER() AS avg_score from stu;
''').show()



