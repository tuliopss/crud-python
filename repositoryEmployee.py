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

    def getEmployeeById(id):
        connection, cursor = get_connection_and_cursor()

        employee = queryGetEmployeeById(id)
        checkIfEmployeeExist(employee)

        def readEmployee(employee):
            if employee:
                print("Employee found:")
                print(employee)
                print("\n")
            else:
                print(f"Employee with ID {id} not found.")

        readEmployee(employee)
        closeConn(connection, cursor)

    def deleteEmployee(id):
        connection, cursor = get_connection_and_cursor()

        employee = queryGetEmployeeById(id)
        checkIfEmployeeExist(employee)

        if employee:
            query = f'DELETE FROM employees WHERE id={employee[0]}'
            cursor.execute(query)
            connection.commit()
            closeConn(connection, cursor)
            print('Employee deleted')

    return {"getEmployees": getEmployees, "insertEmployee": insertEmployee, 'deleteEmployee': deleteEmployee, 'getEmployeeById': getEmployeeById}

repository = employeeRepository()

if repository:
    getEmployees = repository['getEmployees']
    insertEmployee = repository['insertEmployee']
    getEmployeeById = repository['getEmployeeById']
    deleteEmployee = repository['deleteEmployee']

    # getEmployees()
    # deleteEmployee(6)
    # insertEmployee("emp4", "emp2@email.com", "dev", 4000)

    getEmployeeById(1)
else:
    print("Repository creation failed.")
