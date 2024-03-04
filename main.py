

import unittest
from Mock_PostGres import TestPostgresUtils

from pyspark.sql import SparkSession
from Pyspark_Full_Load import TestFullDataLoading
from Pyspark_Full_Load import TestIncrDataLoading

if __name__ == "__main__":


    print("Testing the Mock_PostGres")

    ########################Testing the Postgres##############################
    # Load the test cases from TestPostgresUtils
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPostgresUtils)

    # Run the tests
    unittest.TextTestRunner().run(suite)

    ######################Test Pyspark Full load #############################

    # Initialize SparkSession
    spark = SparkSession.builder \
        .appName("TestFullDataLoading") \
        .master("local[2]") \
        .enableHiveSupport() \
        .getOrCreate()

    # Load the test cases from TestDataLoading
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFullDataLoading)

    # Run the tests
    unittest.TextTestRunner().run(suite)

    # Stop SparkSession
    spark.stop()

    #####################Test Pyspark Incremental load #########################

    # Initialize SparkSession
    spark = SparkSession.builder \
        .appName("TestIncrDataLoading") \
        .master("local[2]") \
        .enableHiveSupport() \
        .getOrCreate()

    # Load the test cases from TestDataLoading
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIncrDataLoading)

    # Run the tests
    unittest.TextTestRunner().run(suite)

    # Stop SparkSession
    spark.stop()


