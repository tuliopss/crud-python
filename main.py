from db.config import openConn, closeConn


def insertEmployee(name, email, role, salary):
    connection, cursor = openConn()

    employee = ([ name, email, role, salary])
    
    query = f'INSERT INTO employees (name, email, role, salary) VALUES("{employee[0]}","{employee[1]}","{employee[2]}","{employee[3]}" )'
    cursor.execute(query)
    connection.commit()

    closeConn(connection, cursor)
    print("registrado")

insertEmployee("teste", "teste@email.com", "tester", 3000)