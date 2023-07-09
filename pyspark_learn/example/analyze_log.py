import jieba
from pyspark import SparkContext, SparkConf
from pyspark.storagelevel import StorageLevel
import os
import func

os.environ["JAVA_HOME"] = '/usr/local/jdk-15.0.1'
conf = SparkConf().setAppName("test")
sc = SparkContext(conf=conf)

rdd = sc.textFile("../test_data/SogouQ.txt")

rdd2 = rdd.map(lambda line: line.split("\t"))

rdd2.persist(StorageLevel.DISK_ONLY)

# res = rdd2.takeSample(True, 3)
# print(res)

context_rdd = rdd2.map(lambda x: x[2])

words_rdd = context_rdd.flatMap(func.context_jieba)
# print(words_rdd.collect())

# 过滤
# 院校 帮 -
filter_rdd =  words_rdd.filter(func.filter_words )
# print(filter_rdd.collect())

final_words_rdd = filter_rdd.map(func.append_words)
# print(final_words_rdd.collect())

#对单词进行分组排序聚合

result = final_words_rdd.reduceByKey(lambda x, y: x+y).sortBy(lambda x: x[1], ascending=False, numPartitions=1).take(5)
print(result)

# TODO 用户和关键词组合分析 用户id ， 搜索内容

user_content_rdd = rdd2.map(lambda x:(x[1], x[2]))

#对用户的搜索内容分词， 然后再次聚合
user_word_with_one_rdd = user_content_rdd.flatMap(func.extract_user_word)
res = user_word_with_one_rdd.reduceByKey(lambda a, b: a+b).sortBy(lambda a:a[1], ascending=False, numPartitions=1).take(5)
print(res)

# TODO 热门搜索时间段分析

time_rdd = rdd2.map(lambda x:x[0])
hour_rdd = time_rdd.map(lambda x:(x.split(":")[0], 1))
#分组聚合排序
res = hour_rdd.reduceByKey(lambda a, b : a+b).sortBy(lambda a:a[1], ascending=False, numPartitions=1).collect()
print(res)