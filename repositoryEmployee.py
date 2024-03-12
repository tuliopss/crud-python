from db.config import openConn, closeConn
from employeeHelpers import queryGetEmployeeById, checkIfEmployeeExist

def employeeRepository(): #funcao de alta ordem
    connection, cursor = openConn()

    #closures
    def insertEmployee(name, email, role, salary):
        # connection, cursor = openConn()

        dicEemployee = {"name": name, "email": email, "role": role, "salary": salary}
        employeesColumns = ', '.join(dicEemployee.keys())

        query = f'INSERT INTO employees ({employeesColumns}) VALUES("{dicEemployee['name']}","{dicEemployee['email']}","{dicEemployee['role']}","{dicEemployee['salary']}")'
        cursor.execute(query)
        connection.commit()

        closeConn(connection, cursor)
        print("registrado")

    def getEmployees():
        query = f'SELECT * FROM employees'

        cursor.execute(query)
        listEmployees = cursor.fetchall() 
        print(listEmployees)
        closeConn(connection, cursor)
        return listEmployees
        # def readEmployees():
        #     listaEmployees = []
        #     list(map(lambda emp: listaEmployees.append(emp), result))
        #     print('read', listaEmployees)

        #     return listaEmployees

        # readEmployees()

    def getEmployeeById(id):
        employee = queryGetEmployeeById(id)
        checkIfEmployeeExist(employee)
        if employee:
            print(employee)
        
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

    def searchEmployeesByRole(role):
        query = f'SELECT * FROM employees'

        cursor.execute(query)
        listEmployees = cursor.fetchall() 

        # list compreheension e lambda
        listEmployeesByRole = lambda role : [emp for emp in listEmployees if emp[3].startswith(role) ]
        print(listEmployeesByRole(role))
        return listEmployeesByRole(role)

    return {"getEmployees": getEmployees, 
            "insertEmployee": insertEmployee,
            'deleteEmployee': deleteEmployee, 
            'getEmployeeById': getEmployeeById, 
            'searchEmployeesByRole':searchEmployeesByRole} #chatgpt


repository = employeeRepository()
getEmployees = repository['getEmployees']   
insertEmployee = repository['insertEmployee']
getEmployeeById = repository['getEmployeeById']   
deleteEmployee = repository['deleteEmployee']    
searchEmployeesByRole = repository['searchEmployeesByRole']
# getEmployees()
# deleteEmployee(6)
# insertEmployee("julio", "julio@email.com", "test analysys", 4000)

getEmployeeById(4)
# searchEmployeesByRole('test')