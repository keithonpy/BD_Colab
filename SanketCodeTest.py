import unittest
from pyspark.sql import SparkSession

class TestDataLoading(unittest.TestCase):
    def setUp(self):
        # Initialize SparkSession
        self.spark = SparkSession.builder \
            .appName("TestDataLoading") \
            .master("local[2]") \
            .enableHiveSupport() \
            .getOrCreate()

    def tearDown(self):
        # Stop SparkSession
        self.spark.stop()

    def test_data_loading(self):
        # Define test data
        expected_count = 2  # Expected number of rows loaded from PostgreSQL

        # Read data from PostgreSQL
        postgres_url = "jdbc:postgresql://ec2-3-9-191-104.eu-west-2.compute.amazonaws.com:5432/testdb"
        postgres_properties = {
            "user": "consultants",
            "password": "WelcomeItc@2022",
            "driver": "org.postgresql.Driver",
        }
        postgres_table_name = "health_insurance"
        df_postgres = self.spark.read.jdbc(url=postgres_url, table=postgres_table_name, properties=postgres_properties)
        df_postgres.show()

        # Perform data loading to Hive
        hive_database_name = "sanket_db"
        hive_table_name = "health_insurance"
        df_postgres.write.mode('overwrite').saveAsTable("sanket_db.health_insurance")

        # Read Hive table
        df_hive = self.spark.read.table("sanket_db.health_insurance")
        df_hive.show()
        # Verify the number of rows loaded to Hive
        actual_count = df_hive.count()
        self.assertEqual(actual_count, expected_count, "Number of rows loaded to Hive does not match expected count")

if __name__ == '__main__':
    unittest.main()
