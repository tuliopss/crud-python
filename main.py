from db.config import openConn, closeConn


def insertEmployee(name, email, role, salary):
    connection, cursor = openConn()

    dicEemployee = {"name": name, "email": email, "role": role, "salary": salary}
    employeesColumns = ', '.join(dicEemployee.keys())

    
    print(employeesColumns)
    # query = f'INSERT INTO employees ({employeesColumns[0],}{employeesColumns[1],}{employeesColumns[2],}{employeesColumns[3],}) VALUES("{employeeValues[0]}","{employeeValues[1]}","{employeeValues[2]}","{employeeValues[3]}" )'
    query = f'INSERT INTO employees ({employeesColumns}) VALUES("{dicEemployee['name']}","{dicEemployee['email']}","{dicEemployee['role']}","{dicEemployee['salary']}")'
    cursor.execute(query)
    connection.commit()

    closeConn(connection, cursor)
    print("registrado")

insertEmployee("refac", "refac@email.com", "re", 4000)