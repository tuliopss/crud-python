from db.config import create_table
from menu import printMenu
from repositoryEmployee import employeeRepository
from insertionMonad import insertEmployee
from employeeHelpers import insertSampleEmployee
repository = employeeRepository()
getEmployees = repository['getEmployees']