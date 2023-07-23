import findspark
findspark.init(spark_home='D:\\bigdata\spark-3.2.0-bin-hadoop3.2')
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType
from pyspark.sql import functions as F

session = SparkSession.builder.appName("json").master("local[*]").getOrCreate()

sc = session.sparkContext

rdd = sc.parallelize([1,2,3,4,5,6,7,8,9]).map(lambda x: [x])
print(rdd.collect())
df = rdd.toDF(['num'])

print(df.toPandas())

#TODO
def num_ride_10(num):
    return num * 10

# 参数 1： 注册的UDF 的名称， 这个名称， 仅仅可以用于SQL 风格
# 参数 2： UDF 的处理逻辑， 是一个单独的方法
# 参数 3： 声明UDF 的返回值类型，注意： UDF注册时候， 必须声明返回值类型， 并且UDF 的真实返回值一定要和声明的返回值一致

udf1 =  session.udf.register('udf1', num_ride_10, IntegerType())

#SQL 风格
# slectExpr, 以select 的表达式执行， 表达式SQL风格的表达式
df.selectExpr('udf1(num)').show()

#DSL 风格
# 返回值UDF 对象， 如果作方法使用，传入的参数 一定是Column对象
df.select(udf1(df['num'])).show()
print("*"*10)
df.select(udf1('num')).show()

# TODO 2 : 方式2注册, 仅用于DSL风格
print("方式2")
udf3 = F.udf(num_ride_10, IntegerType())
df.select(udf3(df['num'])).show()
print('='*10)
df.select(udf3('num').alias("num")).show()