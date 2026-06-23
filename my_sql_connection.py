from loguru import logger
import mysql.connector

connection = mysql.connector.connect(host = "localhost",
                                     user = "root",
                                     password = "Gaurav@936",
                                     database = "home_builder")

logger.info(f"{connection}")

cursor = connection.cursor()

# cursor.execute("select * from labours_table")
insert_query = "INSERT INTO labours_table (name, role, wages) VALUES (%s, %s, %s)"
cursor.execute(insert_query, ('Rahul', 'labour', 700))
connection.commit()
logger.info("Entry Done")
connection.close()
connection.close()
# result = cursor.fetchall()

# logger.info(f"{result}")
