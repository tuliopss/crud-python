from db.config import openConn, closeConn
from employeeHelpers import queryGetEmployeeById, checkIfEmployeeExist
from resultMonad import ResultMonad

def get_connection_and_cursor():
    return openConn()

def employeeRepository():
    connection, cursor = openConn()

    if connection is None or cursor is None:
        print("Failed to open connection. Check your database configuration.")
        return None

    def insertEmployee(name, email, role, salary):
        try:
            if not name or not email or not role or float(salary) < 0:
                return ResultMonad("Invalid data", success=False)
        except ValueError:
            return ResultMonad("Invalid salary", success=False)

        try:
            connection, cursor = get_connection_and_cursor()

            dicEmployee = {"name": name, "email": email, "role": role, "salary": float(salary)}
            employeesColumns = ', '.join(dicEmployee.keys())

            query = f"INSERT INTO employees ({employeesColumns}) VALUES('{dicEmployee['name']}','{dicEmployee['email']}','{dicEmployee['role']}','{dicEmployee['salary']}')"
            cursor.execute(query)
            connection.commit()

            closeConn(connection, cursor)
            return ResultMonad("Employee registered")
        except Exception as e:
            return ResultMonad(str(e), success=False)


    def editEmployee(id, updatedName, updatedRole, updatedSalary):      
        try:
            connection, cursor = get_connection_and_cursor()
            employee = queryGetEmployeeById(id)
            checkIfEmployeeExist(employee)

            if employee:
                dicEmployee = {"name": employee[1], "email": employee[2], "role": employee[3], "salary": employee[4]}
                
                if updatedName == "":
                    updatedName = dicEmployee['name']
                
                if updatedRole == "":
                    updatedRole = dicEmployee['role']
                if updatedSalary == "":
                    updatedSalary = dicEmployee['salary'] 

                dicEmployee['name'] = updatedName
                dicEmployee['role'] = updatedRole
                dicEmployee['salary'] = updatedSalary

                query = f"UPDATE employees SET name = '{updatedName}', role = '{updatedRole}', salary = '{updatedSalary}' WHERE id = {id}"

                cursor.execute(query)
                connection.commit()
                closeConn(connection, cursor)
                return ResultMonad("Employee edited", success=True)  # Definir success=True para operação bem-sucedida
        except Exception as e:
            return ResultMonad(f'Failed to edit employee: {e}', success=False)

        return ResultMonad("Employee not found", success=False)


    def getEmployees(print_details=True):
        try:
            connection, cursor = get_connection_and_cursor()
            query = f'SELECT * FROM employees'
            cursor.execute(query)
            result = cursor.fetchall()
            
            def readEmployees():
                for employee in result:
                    if print_details:
                        print(employee)
                        print("=================================================================\n")

            readEmployees()

            closeConn(connection, cursor)
            return result
        except Exception as e:
            return ResultMonad(f'Failed to get employees: {e}', success=False)



    def getEmployeeById(id, printCb):
        try:
            connection, cursor = get_connection_and_cursor()
            employee = queryGetEmployeeById(id)
            checkIfEmployeeExist(employee)
            closeConn(connection, cursor)
            if employee:
                printCb(employee)
                return ResultMonad(employee)
            else:
                return ResultMonad("Employee not found", success=False)
        except Exception as e:
            return ResultMonad(f'Failed to get employee by ID: {e}', success=False)

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
                return ResultMonad("Employee deleted", success=True)  # Definir success=True para operação bem-sucedida
            else:
                return ResultMonad("Employee not found", success=False)
        except Exception as e:
            return ResultMonad(f'Failed to delete employee: {e}', success=False)

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
    return {
        "getEmployees": getEmployees, 
        "insertEmployee": insertEmployee,
        'deleteEmployee': deleteEmployee, 
        'getEmployeeById': getEmployeeById, 
        'searchEmployeesByRole': searchEmployeesByRole,
        'editEmployee': editEmployee
    }
