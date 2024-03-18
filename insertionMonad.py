from db.config import openConn, closeConn
from resultMonad import ResultMonad


def insertEmployee(name, email, role, salary):
    try:
        connection, cursor = openConn()

        dicEmployee = {"name": name, "email": email, "role": role, "salary": salary}
        employeesColumns = ', '.join(dicEmployee.keys())

        query = f"INSERT INTO employees ({employeesColumns}) VALUES('{dicEmployee['name']}','{dicEmployee['email']}','{dicEmployee['role']}','{dicEmployee['salary']}')"
        cursor.execute(query)
        connection.commit()

        closeConn(connection, cursor)
        return ResultMonad("Registrado com sucesso")
    except Exception as e:
        return ResultMonad(str(e), success=False)
