# import findspark
# findspark.init(spark_home='D:\\bigdata\spark-3.3.2-bin-hadoop3')
from pyspark import SparkContext
sc = SparkContext("local", "count app")

words = sc.parallelize(
    ["scala",
     "java",
     "hadoop",
     "spark",
     "akka",
     "spark vs hadoop",
     "pyspark",
     "pyspark and spark"
     ])
# print(words)
print("words --- ", words.count())
print(words.collect())

s = sc.parallelize([1,2,3,4,5]).map(lambda x: x*10).collect()
print(s)

s2 = sc.parallelize([1,2,3,4,5,6,7,8,9],3).glom().count()
print(s2)
s3 = sc.parallelize([1,2,3,4,5,6,7,8,9],3)

def add(n):
    return n* 10

print(s3.map(add).collect())
print("======================")
print(s3.map(lambda x: x * 10).collect())
