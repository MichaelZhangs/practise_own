import string

from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, StringType, ArrayType, StructType
from pyspark.sql import functions as F
import os

os.environ["JAVA_HOME"] = '/usr/local/jdk-15.0.1'


session = SparkSession.builder.appName("json").master("local[*]").getOrCreate()

sc = session.sparkContext

# 传入三个数字， 1，2，3 返回字典
# {'num': 1, 'letter': 'a}

rdd = sc.parallelize([[1], [2], [3]])
df = rdd.toDF(['num'])

def process(data):
    return {"num": data, "letters": string.ascii_letters[data]}

udf1 =  session.udf.register('udf1', process, StructType().add('num', IntegerType(), nullable=True). \
                     add('letters', StringType(), nullable=True))

df.selectExpr('udf1(num)').show(truncate=True)

df.select(udf1('num')).show(truncate=True)









