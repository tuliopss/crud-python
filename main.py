from menu import printMenu
from repositoryEmployee import employeeRepository
repository = employeeRepository()
printMenu()
option = input('selecione')

if(option == 1):
    employeeRepository['getEmployees']