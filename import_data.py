import psycopg2
from psycopg2 import Error


def insert_iris_list(input_list):
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="postgres",
                                      password="123",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="iris")

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Executing a SQL query
        sql = "INSERT INTO iris_flower(sepal_length, sepal_width, petal_length, petal_width) VALUES(%s, %s, %s, %s);"
        cursor.execute(sql, input_list)
        connection.commit()
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            # print("PostgreSQL connection is closed")
