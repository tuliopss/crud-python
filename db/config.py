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

def create_table():
    print("Creating or checking the 'employees' table...")
    connection, cursor = openConn()

    try:
        # Altera para o banco de dados 'employeespy'
        cursor.execute("USE employeespy")

        # Defina a estrutura da tabela
        table_query = """
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            role VARCHAR(100) NOT NULL,
            salary FLOAT NOT NULL,
            created DATETIME NOT NULL
        )
        """

        cursor.execute(table_query)
        connection.commit()

        print("Table 'employees' created or checked.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        closeConn(connection, cursor)

# Chama a função create_table quando este script é executado diretamente
if __name__ == "__main__":
    create_table()
