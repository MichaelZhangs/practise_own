from pyspark import SparkContext, SparkConf
import os


os.environ["JAVA_HOME"] = '/usr/local/jdk-15.0.1'
conf = SparkConf().setAppName("test")
sc = SparkContext(conf=conf)

stu_info_list = [
    (1, "张三", 11),
    (2, "李四", 14),
    (3, "王五", 11),
    (4, "赵六", 13)
]
broadcast = sc.broadcast(stu_info_list)
score_info_rdd = sc.parallelize([
    (1, "语文", 98),
    (2, "数学", 98),
    (3, "英语", 98),
    (4, "编程", 98),
    (1, "语文", 98),
    (2, "数学", 98),
    (3, "英语", 98),
    (4, "编程", 98)
], 3)

def map_func(data):
    stu_id = data[0]
    name = ''
    for i in broadcast.value:
        if stu_id == i[0]:
            name = i[1]
    return (name, data[1], data[2])


print(score_info_rdd.map(map_func).collect())
print(broadcast.value)
