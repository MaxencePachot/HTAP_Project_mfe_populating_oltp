import mysql.connector

#MySQL local account details
host = "localhost"
user = "root"
password = "secret"

# Create MySQL connection
def get_mysql_connection():
    try:
        print("Connection in progress")
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
        )
        print("------------------------------------------")  
        print("Successfully connected to MySQL!")
        for i in range (2) : 
            print("------------------------------------------")
        return conn
    except Exception as e:
        print("------------------------------------------")  
        print("Error connecting to MySQL: ", e)
        return None