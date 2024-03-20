from repositoryEmployee import employeeRepository
from employeeHelpers import checkIfEmployeeExist, queryGetEmployeeById


def printMenu():
    print("Select an option: ")
    print("1 - Insert employee")
    print("2 - Delete employee")
    print("3 - Search an employee by id")
    print("4 - Show all employees")
    print("5 - Show employees for a role")
    print("6 - Edit employee")
    print("7 - Exit")

def runOption():
    repository = employeeRepository()
    getEmployees = repository['getEmployees']   
    insertEmployee = repository['insertEmployee']
    editEmployee = repository['editEmployee']
    getEmployeeById = repository['getEmployeeById']   
    deleteEmployee = repository['deleteEmployee']    
    searchEmployeesByRole = repository['searchEmployeesByRole']
    option = input("Enter your choice: ")
    if not option.isdigit() or int(option) not in range(1, 8):
        print("Invalid choice. Please enter a number from 1 to 7.")
        return runOption()  # Chamada recursiva para solicitar uma entrada válida
    option = int(option)
    
    options = {
        1: lambda: inputInsertEmployee(insertEmployee),
        2: lambda: inputDeleteEmployee(deleteEmployee),
        3: lambda: inputGetEmployeeById(getEmployeeById),
        4: getEmployees,
        5: lambda: inputGetEmployeeForRole(searchEmployeesByRole),
        6: lambda: inputEditEmployee(editEmployee),    
        7: exitProgram,
    }

    fn = options.get(option)
    if not fn:
        print('Invalid option')
    else:
        fn()
        executeMenu()

def inputInsertEmployee(insertEmployee):
    name = input("Enter employee name: ")
    email = input("Enter employee email: ")
    role = input("Enter employee role: ")
    salary = input("Enter employee salary: ")

    if not salary:
        print("Salary cannot be empty.")
        return

    result = insertEmployee(name, email, role, salary)
    if result.success:
        print(result.value)
    else:
        print("Failed to insert employee:", result.value)


def inputGetEmployeeById(callback):
    employee_id = input("Enter the ID of employee you want to search: ")
    if not employee_id:
        print("Employee ID cannot be empty.")
        return

    callback(employee_id, printEmp) 


def inputEditEmployee(callback):
    id = input('Enter the employee ID: ')
    if not id:
        return runOption()
    employee = queryGetEmployeeById(id)
    if not employee:
        print("Employee not found")
        return runOption()
    updatedName = input("Enter the new name: ")
    updatedRole = input("Enter the new role: ")
    updatedSalary = input("Enter the new salary: ")
    if not updatedName or not updatedRole or not updatedSalary:
        print("Name, role, and salary cannot be empty.")
        return inputEditEmployee(callback)  # Chamando recursivamente para continuar pedindo ao usuário uma entrada válida
    callback(id, updatedName, updatedRole, updatedSalary)



def printEmp(emp):
    print(emp)


def inputGetEmployeeForRole(callback):
    role = input('Enter the employee role: ')
    if not role:
        print("Role cannot be empty.")
        return inputGetEmployeeForRole(callback)
    callback(role)


def inputDeleteEmployee(deleteEmployee):
    try:
        employee_id = int(input("Enter the ID of employee you want to delete: "))
    except ValueError:
        print("Invalid ID. Please enter a valid integer ID.")
        return

    result = deleteEmployee(employee_id)
    if result.success:
        print(result.value)
    else:
        print("Failed to delete employee:", result.value)


def exitProgram():
    print("Program closed.")
    exit()

def executeMenu():
    printMenu()
    runOption()
