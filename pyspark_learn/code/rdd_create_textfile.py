from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("test")

sc = SparkContext(conf=conf)

file_rdd1 = sc.textFile("../test_data/words.txt")

print("默认读取分区数 ： ", file_rdd1.getNumPartitions())
print("file_rdd1 内容： ", file_rdd1.collect())

