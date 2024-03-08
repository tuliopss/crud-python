from db.config import openConn, closeConn

def employeeRepository():
    connection, cursor = openConn()

    def insertEmployee(name, email, role, salary):
        # connection, cursor = openConn()

        dicEemployee = {"name": name, "email": email, "role": role, "salary": salary}
        employeesColumns = ', '.join(dicEemployee.keys())

        query = f'INSERT INTO employees ({employeesColumns}) VALUES("{dicEemployee['name']}","{dicEemployee['email']}","{dicEemployee['role']}","{dicEemployee['salary']}")'
        cursor.execute(query)
        connection.commit()

        closeConn(connection, cursor)
        print("registrado")

    def getEmployees(table):
        query = f'SELECT * FROM {table}'

        cursor.execute(query)
        result = cursor.fetchall() 

        def readEmployees():
            listaEmployees = []
            list(map(lambda emp: listaEmployees.append(emp), result))
            print(listaEmployees)

            return listaEmployees

        readEmployees()
        closeConn(connection, cursor)

    def getEmployeeById(id):
        query = f'SELECT * FROM employees'
        cursor.execute(query)

        result = cursor.fetchall()

        def readEmployee():
            employee = list(filter(lambda emp: emp[0] == id, result))
            print(employee)
        
        readEmployee()
        closeConn(connection, cursor)


    def deleteEmployee(id):
        query = f'DELETE FROM employees WHERE id={id}'
        
        cursor.execute(query)
        connection.commit()
        closeConn(connection,cursor)
        print('deletado')

    return {"getEmployees": getEmployees, "insertEmployee": insertEmployee, 'deleteEmployee': deleteEmployee, 'getEmployeeById': getEmployeeById} #chatgpt

# insertEmployee("refac", "refac@email.com", "re", 4000)

repository = employeeRepository()
getEmployees = repository['getEmployees']   
getEmployeeById = repository['getEmployeeById']   
deleteEmployee = repository['deleteEmployee']    
# getEmployees('employees')


getEmployeeById(1)
