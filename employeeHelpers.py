from db.config import openConn, closeConn

# Função para obter a conexão e o cursor
def get_connection_and_cursor():
    return openConn()

def insertSampleEmployee():
    connection, cursor = get_connection_and_cursor()

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
    connection, cursor = get_connection_and_cursor()
    query = f'SELECT * FROM employees WHERE id={id}'
    cursor.execute(query)
    employee = cursor.fetchone()
    closeConn(connection, cursor)
    return employee


def checkIfEmployeeExist(emp):
    if not emp:
        print('Employee not found')
    return emp
    # return emp if emp else print('a Employee not Found')
