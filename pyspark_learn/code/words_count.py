from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("wordsCount")

sc = SparkContext(conf=conf)
#  读取配置文件
file_rdd = sc.textFile("../test_data/words.txt")
print("file_rdd = ", file_rdd.collect())
# 按行切割
words_rdd = file_rdd.flatMap(lambda line : line.split(" "))
print("words_rdd =  ", words_rdd.collect())
#  构造成元组
words_with_one_rdd = words_rdd.map(lambda x: (x,1))
print("words_with_one_rdd = ", words_with_one_rdd.collect())
# 汇聚计算
result_rdd = words_with_one_rdd.reduceByKey(lambda a, b: a+b)
print("result_rdd = ", result_rdd)
print(result_rdd.collect())