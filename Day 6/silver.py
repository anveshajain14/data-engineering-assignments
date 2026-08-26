from pyspark.sql.functions import *

df = spark.read.table("cyntexa_dev.bronze.sales")
df_cleaned = df.withColumn("sale_id", col("sale_id").cast("int")) \
    .withColumn("customer_id", col("customer_id").cast("int")) \
        .withColumn("product_id", col("product_id").cast("int")) \
            .withColumn("quantity", col("quantity").cast("double")) \
                .withColumn("sale_amount", col("sale_amount").cast("double")) \
                    .withColumn("sale_date", to_date(col("sale_date")))\
                        .dropDuplicates().dropna()

df_cleaned.write.mode("overwrite").saveAsTable("cyntexa_dev.silver.sales_cleaned")