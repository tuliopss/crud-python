from repositoryEmployee import employeeRepository
repository = employeeRepository()
getEmployees = repository['getEmployees']


def printMenu():
    print("Select an option: ")
    print("1 - Insert employee")
    print("2 - Delete employee")
    print("3 - Search a employee by id")
    print("4 - Show all employees")
    print("5 - Exit")
