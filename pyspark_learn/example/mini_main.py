from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, StringType, ArrayType, StructType
from pyspark.sql import functions as F
import os
from pyspark.storagelevel import StorageLevel


os.environ["JAVA_HOME"] = '/usr/local/jdk-15.0.1'

session = SparkSession.builder.appName("sparkSql").master("local[*]").config('spark.sql.shuffle.partitions', '2').getOrCreate()

sc = session.sparkContext


df = session.read.format('json').load('../test_data/mini.json'). \
    dropna(thresh=1, subset=['storeProvince']). \
    filter('storeProvince != "null"'). \
    filter('receivable < 10000'). \
    select('storeProvince', 'storeID', 'receivable', 'dateTs', 'payType')
# 省份信息缺失值过滤

# TODO 1： 各省销售额统计
province_df = df.groupBy('storeProvince').sum('receivable').\
    withColumnRenamed('sum(receivable)', 'money').\
    withColumn('money', F.round('money', 2)). \
    orderBy('money', ascending=False)

province_df.show()

#TODO 2: TOP3销售省份中， 有多少达到日均销售额 1000 +

top3_province_df = province_df.limit(3).select('storeProvince').withColumnRenamed('storeProvince', 'top3_province')

#2.2
top3_province_df_joined =  df.join(top3_province_df, on= df['storeProvince' ] == top3_province_df['top3_province'])

top3_province_df_joined.persist(StorageLevel.MEMORY_AND_DISK)
print(top3_province_df_joined.show())

tdf = top3_province_df_joined.groupBy("storeProvince", "storeID",
                                F.from_unixtime(df['dateTs'].substr(0,10), 'yyyy-MM-dd').alias('day')
                                ).sum('receivable').withColumnRenamed('sum(receivable)', 'money'). \
                                filter('money > 1000'). \
                                dropDuplicates(subset=['storeID']). \
                                groupBy('storeProvince').count()

tdf.show()

# TODO 3

top3_province_avg = top3_province_df_joined.groupBy('storeProvince'). \
    avg('receivable'). \
    withColumnRenamed('avg(receivable)', 'money'). \
    withColumn('money', F.round('money', 2)). \
    orderBy('money', ascending=False)

top3_province_avg.show(truncate=False)


#TODO 4: 各个省份中 支付比例
top3_province_df_joined.createTempView('province_pay')

def udf_func(percent):
    return str(round(percent * 100, 2)) + "%"

my_udf =  F.udf(udf_func, StringType())

pay_type_df = session.sql(
    '''
    select storeProvince, payType, (count(payType) / total) as percent from 
    (select storeProvince, payType, count(1) OVER(PARTITION BY storeProvince) as total from province_pay)
    group by storeProvince, payType, total order by percent DESC 
    '''
).withColumn('percent', my_udf('percent'))

pay_type_df.show()

top3_province_df_joined.unpersist()




