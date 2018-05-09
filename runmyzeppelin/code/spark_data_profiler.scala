

import org.apache.spark.sql.functions._ 

var df1 =spark.read.option("delimeter",",").option("header","true")
                                            .option("InferSchema","true")
                                            .csv("/Users/aloktiwari/Downloads/SFFoodProgram_Complete_Data/businesses_plus.csv")

val df2 = df1.select($"*").withColumn("newdt",to_date(from_unixtime(unix_timestamp(df1("application_date"),"MM/dd/yyyy"))))

df2.show

df2.createOrReplaceTempView("temp_dq_assessment")
val df3 = spark.sql(s"""
	                SELECT 'business_id' column_name, 
	                                count(*) total_cnt,
	                                count(business_id) not_null_cnt,
	                                count(distinct business_id) distinct_cnt,
	                                percentile(business_id, 0.01) as perc_1,
	                                percentile(business_id, 0.05) as perc_5,
	                                min(business_id) min, 
	                                max(business_id) max, 
	                                percentile(business_id, 0.95) as perc_95,
	                                percentile(business_id, 0.99) as perc_99,
	                                avg(business_id) avg 
	                from temp_dq_assessment
	                """)

df3.show

import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import scala.collection.mutable.ListBuffer
import spark.sqlContext.implicits._


def profileData(df:DataFrame) {
 for (column <- df.schema) if (column.dataType == IntegerType || column.dataType == DoubleType || column.dataType == LongType ){
   var columnName = new ListBuffer[String]()  //hello this is comment
	  columnName += column.name
	  for (col_name <- columnName) {
	  df.createOrReplaceTempView("temp_dq_assessment")
	  val t_values = spark.sql(s"""
	                SELECT '$col_name' column_name, 
	                                count(*) total_cnt,
	                                count($col_name) not_null_cnt,
	                                count(distinct $col_name) distinct_cnt,
	                                percentile($col_name, 0.01) as perc_1,
	                                percentile($col_name, 0.05) as perc_5,
	                                min($col_name) min, 
	                                max($col_name) max, 
	                                percentile($col_name, 0.95) as perc_95,
	                                percentile($col_name, 0.99) as perc_99,
	                                avg($col_name) avg 
	                from temp_dq_assessment
	                """)
	  t_values.show(false)
	    
	   }
 }else if (column.dataType == StringType ){
  var columnName = new ListBuffer[String]()
	  columnName += column.name
	  for (col_name <- columnName) {
	  df.createOrReplaceTempView("temp_dq_assessment")
	  val t_values = spark.sql(s"""SELECT '$col_name' column_name, 
	                                       count(*) total_cnt, 
	                                       count($col_name) not_null_cnt,
	                                       count(distinct $col_name) distinct_cnt 
	                           from temp_dq_assessment""")

	  t_values.show(false)
	  
	  }
 }else if  (column.dataType == DateType ||column.dataType == TimestampType  ){
   var columnName = new ListBuffer[String]()
	  columnName += column.name
	  for (col_name <- columnName) {
	  df.createOrReplaceTempView("temp_dq_assessment")
	  val t_values = spark.sql(s"""SELECT '$col_name' column_name,
	                                       count(*) total_cnt,
	                                       count($col_name) null_cnt,
	                                       min($col_name) min_date,
	                                       max($col_name) max_date 
	                           from temp_dq_assessment""")
	
	  t_values.show(false)

	   }

}  else ("not found")

}




// this is a profile data function

profileData(df2)

df3.coalesce(1).
    write.
    format("com.databricks.spark.csv").
    option("header", "true").
    mode("overwrite").
    save("/Users/aloktiwari/myfile.csv")