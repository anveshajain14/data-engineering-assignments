from pyspark.sql.functions import *

df = spark.read.csv("/Volumes/cyntexa_dev/sales/raw/sales (1).csv", header = True)
df.write.mode("overwrite").saveAsTable("cyntexa_dev.bronze.sales")