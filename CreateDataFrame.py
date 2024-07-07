# Databricks notebook source
from pyspark.sql.types import * 

data = [(1,'Srijan'),(2,'Disha')]

# schema = ['id','name']
schema = StructType([StructField(name = 'id' ,dataType = IntegerType()),
           StructField(name = 'name' ,dataType = StringType())])
df = spark.createDataFrame(data = data,schema = schema)
df.show()
df.printSchema()

# COMMAND ----------

data1 = [{'id':1 ,'name':'Srijan'},
       {'id':2 ,'name':'Disha'}]
        
df = spark.createDataFrame(data = data1)
df.show()
df.printSchema()
