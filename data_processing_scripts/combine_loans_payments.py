import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node payments
payments_node1732342878594 = glueContext.create_dynamic_frame.from_catalog(database="raw_data", table_name="payments", transformation_ctx="payments_node1732342878594")

# Script generated for node loans
loans_node1732342903224 = glueContext.create_dynamic_frame.from_catalog(database="raw_data", table_name="loans", transformation_ctx="loans_node1732342903224")

# Script generated for node Join
payments_node1732342878594DF = payments_node1732342878594.toDF()
loans_node1732342903224DF = loans_node1732342903224.toDF()
Join_node1732343080032 = DynamicFrame.fromDF(payments_node1732342878594DF.join(loans_node1732342903224DF, (payments_node1732342878594DF['loan_id'] == loans_node1732342903224DF['loan_id']), "right"), glueContext, "Join_node1732343080032")

# Script generated for node combined_loans_payments
combined_loans_payments_node1732343219742 = glueContext.getSink(path="s3://realfi-loan-tape-data-nov-2024/processedData/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], compression="snappy", enableUpdateCatalog=True, transformation_ctx="combined_loans_payments_node1732343219742")
combined_loans_payments_node1732343219742.setCatalogInfo(catalogDatabase="processed_data",catalogTableName="combined_loans_payments")
combined_loans_payments_node1732343219742.setFormat("csv")
combined_loans_payments_node1732343219742.writeFrame(Join_node1732343080032)
job.commit()