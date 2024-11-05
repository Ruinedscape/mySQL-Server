import maskpass
import mysql.connector
from mysql.connector import Error

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

host_name = "localhost"
user_name = "root"
user_password = maskpass.askpass(mask="*")

while True:
    db_name = input("Enter the name of the database: ")
    connection = create_db_connection(host_name, user_name, user_password, db_name)
    results = read_query(connection, "SHOW TABLES")
    for result in results:
        print(result)

    table = input("Enter the name of the table: ")
    query = "SELECT * FROM " + table
    results = read_query(connection, query)
    for result in results:
        print(result)
