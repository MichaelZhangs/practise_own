from pyspark import SparkContext, SparkConf
import os
os.environ["JAVA_HOME"]='/usr/local/jdk-15.0.1'

# 构建sparkContext 对象
conf = SparkConf().setAppName("test").setMaster("local[*]")

sc = SparkContext(conf=conf)

rdd = sc.parallelize([("a", 1), ("a", 1), ("b", 1),("b", 1),("b", 1), ("c", 1)])

# groupby 传入
result = rdd.groupBy(lambda t: t[0])
print(result.map(lambda t: (t[0], list(t[1]))).collect())

s = rdd.reduceByKey(lambda x,y: x+y).filter(lambda x: x[1]>1).collect()
print(s)


rdd = sc.parallelize([1,2,1,1,1,2,3,4,5,6,7], 4)
s2 = rdd.distinct().collect()
print(s2)

rdd1 = sc.parallelize([1,2,3])
rdd2 = sc.parallelize(["a", "b", "c", 1,2])
print(rdd1.union(rdd2).collect())

# join
rdd1 = sc.parallelize([("a", 1), ("b", 2), ("c", 3)])
rdd2 = sc.parallelize([("c", 3), ("d", 1)])
print(rdd1.join(rdd2).collect())
print(rdd1.leftOuterJoin(rdd2).collect())
print("============")
rdd1 = sc.parallelize([("a", 1), ("b", 2), ("c", 3)])
rdd2 = sc.parallelize([("c", 3), ("d", 1)])
print(rdd1.intersection(rdd2).collect())

rdd3 = sc.parallelize([1, 2, 3, 'a', 'b', 'c', 1, 2], 4)
print(rdd3.glom().flatMap(lambda x: x).collect())

rdd4 = sc.parallelize([("b", 1),("E", 4),("D", 1), ("b", 2), ("c", 3)])
print(rdd4.groupByKey().map(lambda x: (x[0], list(x[1]))).collect())

rdd5 = sc.parallelize([4, 1, 5, 2, 6, 3, 7])
print(rdd5.sortBy( lambda x: x,ascending=True, numPartitions=2).collect())
# 按value 排序
print(rdd4.sortBy(lambda x: x[1], ascending=True, numPartitions=3).collect())
# 按key排序
print(rdd4.sortBy(lambda x: x[0], ascending=True, numPartitions=3).collect())

print(rdd4.sortByKey(ascending=True,numPartitions=1,keyfunc=lambda x: str(x).upper()).collect())