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
            list(map(lambda emp: print(emp), result))

        readEmployees()
        closeConn(connection, cursor)

    # def updateEmployee(id, emp):
     
        # dicEemployee = {"name": name, "email": email, "role": role, "salary": salary}

        # queryUpdate = f'UPDATE books SET name = "{dicEemployee["name"]}", email ="{dicEemployee["email"]}", role = "{dicEemployee["role"]}", salary="{dicEemployee["salary"]}" WHERE id = ${id}'
        # queryUpdate = f'UPDATE employees SET name = "{emp.name}", email ="{emp.email}", role = "{emp.role}", salary="{emp.salary}" WHERE id = ${id}'

    def deleteEmployee(id):
        query = f'DELETE FROM employees WHERE id={id}'
        
        cursor.execute(query)
        connection.commit()
        closeConn(connection,cursor)
        print('deletado')

    return {"getEmployees": getEmployees, "insertEmployee": insertEmployee, 'deleteEmployee': deleteEmployee} #chatgpt

# insertEmployee("refac", "refac@email.com", "re", 4000)

repository = employeeRepository()
getEmployees = repository['getEmployees']   
deleteEmployee = repository['deleteEmployee']    
# getEmployees('employees')

deleteEmployee(2)