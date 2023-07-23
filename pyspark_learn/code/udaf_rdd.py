from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType
from pyspark.sql import functions as F
import os

os.environ["JAVA_HOME"] = '/usr/local/jdk-15.0.1'


session = SparkSession.builder.appName("json").master("local[*]").getOrCreate()

sc = session.sparkContext

rdd = sc.parallelize([1,2,3,4,5,6,7,8,9], 3)

df = rdd.map(lambda x: [x]).toDF(['num'])

df.show()

single_partition =  df.rdd.repartition(1)

def process(iter):
    sum = 0
    for row in iter:
        sum += row['num']

    return [sum]


print(single_partition.mapPartitions(process).collect())



