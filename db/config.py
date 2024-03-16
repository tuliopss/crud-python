import mysql.connector  

def openConn():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="employeespy"
    )
    cursor = connection.cursor()
    return connection, cursor

def closeConn(conn, cursor):
    cursor.close()
    conn.close()




