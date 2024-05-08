import mysql.connector

# Establish connection to MySQL
connection = mysql.connector.connect(
    host="localhost",  # Your MySQL host
    user="username",  # Your MySQL username
    password="password",  # Your MySQL password
    database="calculator_db",  # Your MySQL database name
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()
# Define the SQL query to create a table
create_table_query = """
CREATE TABLE IF NOT EXISTS operations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    operation1 VARCHAR(10) NOT NULL,
    operation2 VARCHAR(10) NOT NULL,
    operand VARCHAR(1) NOT NULL,
    result FLOAT NOT NULL
)
"""

# Execute the query
cursor.execute(create_table_query)

# Commit the changes
connection.commit()
# Sample data
operation1 = 5
operation2 = 3
operand = "+"
result = 8

# Define the SQL query to insert data
insert_query = """
INSERT INTO operations (operation1, operation2, operand, result)
VALUES (%s, %s, %s, %s)
"""

# Execute the query with the data
cursor.execute(insert_query, (operation1, operation2, operand, result))

# Commit the changes
connection.commit()
# Close the cursor
cursor.close()

# Close the connection
connection.close()
