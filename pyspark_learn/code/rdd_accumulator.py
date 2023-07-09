from pyspark import SparkContext, SparkConf
import os


os.environ["JAVA_HOME"] = '/usr/local/jdk-15.0.1'
conf = SparkConf().setAppName("test")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1,2,3,4,5,6,7,8,10], 2)


accumu = sc.accumulator(0)

print(accumu)

def map_func(data):
    global accumu
    accumu += 1
    print("count  = ", accumu )


print(rdd.map(map_func).collect())
print("count = ", accumu.value)
