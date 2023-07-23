# import findspark
# findspark.init(spark_home='D:\\bigdata\spark-3.2.0-bin-hadoop3.2')
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, StringType, ArrayType
from pyspark.sql import functions as F
import os

os.environ["JAVA_HOME"] = '/usr/local/jdk-15.0.1'


session = SparkSession.builder.appName("json").master("local[*]").getOrCreate()

sc = session.sparkContext

rdd = sc.parallelize([['hadoop spark flink'], ['hadop flink java']])
df = rdd.toDF(['line'])

def split_line(data):
    return data.split(" ")


#TODO 1 方式1 构建UDF
udf2 =  session.udf.register('udf1', split_line, ArrayType(StringType()))

#DSL 风格
df.select(udf2(df['line'])).show()

#SQL 风格
df.createTempView('lines')
session.sql('select udf1(line) from lines').show(truncate=False)


#TODO 方式2
udf3 = F.udf(split_line, ArrayType(StringType()))

print("方式二 ====")

df.select(udf3('line')).show(truncate=False)
