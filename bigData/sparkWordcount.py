import os
PYSPARK_PYTHON = "/usr/bin/python3"
os.environ["PYSPARK_PYTHON"] = PYSPARK_PYTHON

from pyspark import SparkContext
sc = SparkContext("local[*]", "wordcount")
words = sc.textFile("file:///root/bigData/word.txt").flatMap(lambda line: line.split(" ")).map(lambda x: (x, 1))
count =  words.reduceByKey(lambda a, b: a+b).collect()
print(count)
