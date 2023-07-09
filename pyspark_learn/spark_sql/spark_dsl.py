from pyspark.sql import SparkSession
import os
from pyspark.sql.types import StructType, StringType, IntegerType

os.environ["JAVA_HOME"] = '/usr/local/jdk-15.0.1'

session = SparkSession.builder.appName("test").master("local[*]").getOrCreate()

sc = session.sparkContext

df = session.read.format("csv").\
    schema("id INT, subject STRING, score INT").\
    load("../test_data/sql/stu_score.txt")

id_column = df["id"]
subject_column = df["subject"]

print(f"{id_column} === {subject_column}")

df.select("id", "subject").limit(3).show()
# List 格式
df.select(["id", "subject"]).limit(3).show()

df.where("score < 99").limit(3).show()

df.filter(df["score"] < 99).limit(3).show()

df.groupBy(df["subject"], "score").count().show()

res = df.select(id_column, subject_column).limit(5).toJSON().collect()
# print(type(res))
import json
for i in res:
    # print(i.id, i.subject)
    print(i, json.loads(i).get("id"), json.loads(i).get("subject"))