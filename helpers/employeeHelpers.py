print('antes')
from ..db.config import openConn, closeConn
print('2linha')
connection, cursor = openConn()

def queryGetEmployeeById(id):
        print('dentro funcao')
        query = f'SELECT * FROM employees'
        cursor.execute(query)

        result = cursor.fetchall()

        employee = list(filter(lambda emp: emp[0] == id, result))
        checkIfEmployeeExist(employee)
        closeConn(connection, cursor)

def checkIfEmployeeExist(emp):
    return emp if emp else print('Employee not Found')

print(queryGetEmployeeById(1))
