import mysql.connector
from mysql.connector import Error

# Connect to the MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',      # MySQL server host (usually 'localhost')
            database='your_database_name',  # Name of your database
            user='your_username',  # Your MySQL username
            password='your_password'  # Your MySQL password
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Function to authenticate user
def authenticate_user(username, password):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor(dictionary=True)
        
        # Parameterized query to prevent SQL injection
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        
        # Fetch one result
        user = cursor.fetchone()
        
        if user:
            print(f"Access granted. Welcome, {user['username']}!")
        else:
            print("Access denied. Incorrect username or password.")
        
        # Close the connection
        cursor.close()
        connection.close()
    else:
        print("Failed to connect to the database.")

# Example usage
username = input("Enter username: ")
password = input("Enter password: ")

authenticate_user(username, password)
