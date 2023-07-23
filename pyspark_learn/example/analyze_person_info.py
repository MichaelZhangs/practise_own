import os

import findspark
findspark.init(spark_home='D:\\bigdata\spark-3.3.2-bin-hadoop3')
from pyspark.sql import SparkSession
import json
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StringType, IntegerType, LongType

# os.environ['JAVA_HOME']='E:\jdk-11.0.6'
# os.environ["JAVA_HOME"] = '/usr/local/jdk-15.0.1'

session = SparkSession.builder.appName("json").master("local[*]").getOrCreate()

sc = session.sparkContext
df = session.read.format('json').load('../test_data/person_info.json')


class Anyailize_person():


    def __init__(self):
        self.df = self.__init_to_df()

    def test(self):
        print(self.df.show())

    def __init_to_df(self):

        self.df = df.withColumn('id', F.monotonically_increasing_id()). \
            select(F.col('id'),
                   F.col('_source.rname').alias('name'), F.col('_source.idno').alias('idno'),
                   F.col('_source.sex').alias('sex'),
                   F.col('_source.bplace').alias('bplace'),
                   F.col('_source.idtype').alias('idtype'), F.explode('sort').alias('sort'),
                   F.col('_source.bplace').substr(1,2).alias('province'),
                   F.col("_source.age").alias("age"), F.col("_source.birthday").alias("birthday"))
        return self.df

    def save_to_db(self):
        self.df.write.mode("overwrite").\
            format("jdbc"). \
            option('encoding', 'utf-8'). \
            option("url","jdbc:mysql://localhost:3306/bigdata?useSSL=false&characterEncoding=UTF-8&useUnicode=true&serverTimezone=UTC").\
            option("dbtable", "person_info"). \
            option("user", 'root'). \
            option('password', '123456'). \
            save()

    def search_for_db(self):

        pass


if __name__ == '__main__':
    ay = Anyailize_person()
    # ay.test()
    ay.search_for_db()


# df.printSchema()
#
# df = df.withColumn('id', F.monotonically_increasing_id()). \
#       select(F.col('id'),
#              F.col('_source.rname').alias('name'), F.col('_source.idno').alias('idno'),
#              F.col('_source.sex').alias('sex'),
#              F.col('_source.bplace').alias('bplace'),
#              F.col('_source.idtype').alias('idtype'), F.explode('sort').alias('sort'),
#              F.col("_source.age").alias("age"), F.col("_source.birthday").alias("birthday"))



# df.write.mode("overwrite").\
#     format("jdbc"). \
#     option('encoding', 'utf-8'). \
#     option("url","jdbc:mysql://localhost:3306/bigdata?useSSL=false&characterEncoding=UTF-8&useUnicode=true&serverTimezone=UTC").\
#     option("dbtable", "person_info"). \
#     option("user", 'root'). \
#     option('password', '123456'). \
#     save()



