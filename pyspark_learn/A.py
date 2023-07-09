# -*- coding: utf-8 -*-
import jieba
# import findspark
# findspark.init(spark_home='D:\\bigdata\spark-3.3.2-bin-hadoop3')


from pyspark.context import SparkContext

def word_count():
    # 读取数据，创建弹性式分布数据集（RDD）.<class 'pyspark.rdd.RDD'>
    data = spark.textFile(r"docs.txt")
    # 读取中文停用词
    with open(r'data.txt', 'r', encoding='utf-8') as f:
        s = f.readlines()
    stop = [i.replace('\n', '') for i in s]

    # reduceByKey函数利用映射函数将每个K对应的V进行运算
    # 分词并统计词频
    data = data.flatMap(lambda line: jieba.cut(line, cut_all=False)). \
        filter(lambda w: w not in stop). \
        map(lambda w: (w, 1)). \
        reduceByKey(lambda w0, w1: w0 + w1). \
        sortBy(lambda x: x[1], ascending=False)
    data.foreach(lambda x: print(x))
    print(data.collect())
    # 写入文件
    data.saveAsTextFile(r"result.txt")
    # 输出前100个高频词汇
    print(data.take(100))

if __name__ == '__main__':
    # 实例化一个SparkContext，用于连接Spark集群
    # 第一个参数“local”表示以本地模式加载集群
    # 第二个参数“WordCount”表示appName，不能有空格
    spark = SparkContext("local", "WordCount")
    word_count()