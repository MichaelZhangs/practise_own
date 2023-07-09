from pyspark import SparkContext, SparkConf
import json

import os
os.environ["JAVA_HOME"]='/usr/local/jdk-15.0.1'

conf = SparkConf().setAppName("test")
sc = SparkContext(conf=conf)

rdd = sc.textFile("../test_data/order.text")
print(rdd.flatMap(lambda line: line.split("|")). \
      map(lambda str_dic: json.loads(str_dic)). \
      map(lambda dic:(dic.get("areaName"), dic.get("category"))). \
      filter(lambda x: x[0] == "北京"). \
      distinct().   \
      groupByKey(). \
      map(lambda x: (x[0],list(x[1]))). \
      collect())

