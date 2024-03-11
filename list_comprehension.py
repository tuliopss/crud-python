from db.config import openConn, closeConn

def list_comprehension():
    
    try:

        conn, cursor = openConn()
        
        cursor.execute("select * from employees where role = %s", ("dev",))

        #list comprehension
        
        lst = [i for i in cursor.fetchall() if i]

        closeConn(conn, cursor)

        return lst
    
    except Exception as e:
        
        return e

if __name__ == "__main__":
    
    print(list_comprehension())


