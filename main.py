from db.config import openConn, closeConn


def insertEmployee(name, email, role, salary):
    connection, cursor = openConn()

    dicEemployee = {"name": name, "email": email, "role": role, "salary": salary}
    employeesColumns = ', '.join(dicEemployee.keys())

    query = f'INSERT INTO employees ({employeesColumns}) VALUES("{dicEemployee['name']}","{dicEemployee['email']}","{dicEemployee['role']}","{dicEemployee['salary']}")'
    cursor.execute(query)
    connection.commit()

    closeConn(connection, cursor)
    print("registrado")

def getEmployees(table):
    connection, cursor = openConn()
    query = f'SELECT * FROM {table}'

    cursor.execute(query)
    result = cursor.fetchall() 

    def readEmployees():
        list(map(lambda emp: print(emp), result))
        
    readEmployees()
    closeConn(connection, cursor)


# insertEmployee("refac", "refac@email.com", "re", 4000)
        
getEmployees('employees')