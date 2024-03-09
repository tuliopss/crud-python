from db.config import openConn, closeConn



def queryGetEmployeeById(id):
        connection, cursor = openConn()

        query = f'SELECT * FROM employees WHERE id={id}'
        cursor.execute(query)

        employee = cursor.fetchone()

        # employee = list(filter(lambda emp: emp[0] == id, result))
        # checkIfEmployeeExist(employee)
        closeConn(connection, cursor)
        return employee

def checkIfEmployeeExist(emp):
      if not emp:
       return print('Employee not Found')
        
      return emp

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
        employee = queryGetEmployeeById(id)
        checkIfEmployeeExist(employee)

        def readEmployee(employee):
            if employee:
                print(employee)
        readEmployee(employee)
        closeConn(connection, cursor)
        
    def deleteEmployee(id):
        employee = queryGetEmployeeById(id)
        print('employee', employee)
        checkIfEmployeeExist(employee)
        if employee:
            query = f'DELETE FROM employees WHERE id={employee[0]}'
            cursor.execute(query)
            connection.commit()
            closeConn(connection,cursor)
            print('deletado')

    return {"getEmployees": getEmployees, "insertEmployee": insertEmployee, 'deleteEmployee': deleteEmployee, 'getEmployeeById': getEmployeeById} #chatgpt


repository = employeeRepository()
getEmployees = repository['getEmployees']   
insertEmployee = repository['insertEmployee']
getEmployeeById = repository['getEmployeeById']   
deleteEmployee = repository['deleteEmployee']    

# getEmployees('employees')
deleteEmployee(6)
# insertEmployee("emp4", "emp2@email.com", "dev", 4000)

# getEmployeeById(41)
