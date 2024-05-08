import mysql.connector


connection = mysql.connector.connect(
    host="localhost",  
    user="local", 
    password="123",  
    database="calculator_db",  
)


cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS operations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    operation1 VARCHAR(10) NOT NULL,
    operation2 VARCHAR(10) NOT NULL,
    operand VARCHAR(1) NOT NULL,
    result FLOAT NOT NULL
)
"""


cursor.execute(create_table_query)


connection.commit()

# operation1 = 5
# operation2 = 3
# operand = "+"
# result = 8


insert_query = """
INSERT INTO operations (operation1, operation2, operand, result)
VALUES (%s, %s, %s, %s)
"""


cursor.execute(insert_query, (operation1, operation2, operand, result))
connection.commit()
cursor.close()
connection.close()
