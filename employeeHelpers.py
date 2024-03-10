from db.config import openConn, closeConn
connection, cursor = openConn()

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

