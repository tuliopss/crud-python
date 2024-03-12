from db.config import openConn, closeConn
connection, cursor = openConn()

def insertSampleEmployee():
    connection, cursor = openConn()

    dicEmployee = {"name": "Sample Employee", "email": "sample@email.com", "role": "Sample Role", "salary": 5000}
    employeesColumns = ', '.join(dicEmployee.keys())

    query = f"INSERT INTO employees ({employeesColumns}) VALUES('{dicEmployee['name']}','{dicEmployee['email']}','{dicEmployee['role']}','{dicEmployee['salary']}')"
    cursor.execute(query)
    connection.commit()

    closeConn(connection, cursor)
    print("Sample employee inserted.")

# Chama a função para inserir um funcionário de exemplo
#insertSampleEmployee()

def queryGetEmployeeById(id):
        query = f'SELECT * FROM employees WHERE id={id}'
        cursor.execute(query)

        employee = cursor.fetchone()

        # employee = list(filter(lambda emp: emp[0] == id, result))
        # checkIfEmployeeExist(employee)
        closeConn(connection, cursor)
        return employee

def checkIfEmployeeExist(emp):
    if not emp:
          print('Employee not found')
    return emp
    # return emp if emp else print('a Employee not Found')

