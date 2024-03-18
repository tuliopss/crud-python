from db.config import openConn, closeConn
from employeeHelpers import queryGetEmployeeById, checkIfEmployeeExist

# Função para obter a conexão e o cursor
def get_connection_and_cursor():
    return openConn()

def employeeRepository():
    connection, cursor = openConn()

    if connection is None or cursor is None:
        print("Failed to open connection. Check your database configuration.")
        return None

    def insertEmployee(name, email, role, salary):
        connection, cursor = get_connection_and_cursor()

        dicEmployee = {"name": name, "email": email, "role": role, "salary": salary}
        employeesColumns = ', '.join(dicEmployee.keys())

        query = f"INSERT INTO employees ({employeesColumns}) VALUES('{dicEmployee['name']}','{dicEmployee['email']}','{dicEmployee['role']}','{dicEmployee['salary']}')"
        cursor.execute(query)
        connection.commit()

        closeConn(connection, cursor)
        print("Employee registered")

    def getEmployees():
        connection, cursor = get_connection_and_cursor()

        query = f'SELECT * FROM employees'

        cursor.execute(query)
        result = cursor.fetchall()

        def readEmployees():
            for employee in result:
                print("Employee found:")
                print(employee)
                print("\n")

        readEmployees()

        closeConn(connection, cursor)
        # return listEmployees
        # def readEmployees():
        #     listaEmployees = []
        #     list(map(lambda emp: listaEmployees.append(emp), result))
        #     print('read', listaEmployees)

        #     return listaEmployees

        # readEmployees()

        # Retornando a função getEmployees
        return getEmployees

    def getEmployeeById(id, printCb):
        connection, cursor = get_connection_and_cursor()
        employee = queryGetEmployeeById(id)  # Aqui está o problema
        checkIfEmployeeExist(employee)

        def readEmployee(employee):
            if employee:
                print("Employee found:")
                printCb(employee)
                print("\n")
            else:
                print(f"Employee with ID {id} not found.")

        readEmployee(employee)
        closeConn(connection, cursor)

    def deleteEmployee(id):
        try:
            connection, cursor = get_connection_and_cursor()

            employee = queryGetEmployeeById(id)  # Passar o ID como argumento
            checkIfEmployeeExist(employee)

            if employee:
                query = f'DELETE FROM employees WHERE id={id}'  # Usar o ID passado como argumento
                cursor.execute(query)
                connection.commit()
                closeConn(connection, cursor)
                print('Employee deleted')
        except Exception as e:
            print(f'Failed to delete employee: {e}')
        finally:
            closeConn(connection, cursor)

    def searchEmployeesByRole(role):
        try:
            connection, cursor = openConn()
            query = f"SELECT * FROM employees"
            cursor.execute(query)

            listEmployees = cursor.fetchall()

            listEmployeesByRole = lambda role : [emp for emp in listEmployees if emp[3].startswith(role) ]

            if(len(listEmployeesByRole(role)) == 0):
                return print(f'Employees with role "{role}" not found')
            
            print(listEmployeesByRole(role))
        
            return listEmployeesByRole(role)
        except Exception as e:
            print(f"Failed to search employees by role: {e}")
        finally:
            closeConn(connection, cursor)

    # Retornando todas as funções
    return {"getEmployees": getEmployees, 
            "insertEmployee": insertEmployee,
            'deleteEmployee': deleteEmployee, 
            'getEmployeeById': getEmployeeById, 
            'searchEmployeesByRole':searchEmployeesByRole,
            }

repository = employeeRepository()

if repository:
    getEmployees = repository['getEmployees']
    insertEmployee = repository['insertEmployee']
    getEmployeeById = repository['getEmployeeById']
    deleteEmployee = repository['deleteEmployee']

    # getEmployees()
    # deleteEmployee(6)
    # insertEmployee("emp4", "emp2@email.com", "dev", 4000)

    def printEmployee(employee):
        print("Employee found:")
        print(employee)

    getEmployeeById(1, printEmployee)  # Passando a função de callback para printar o resultado
else:
    print("Repository creation failed.")
