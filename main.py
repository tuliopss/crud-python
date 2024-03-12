from db.config import create_table
from menu import printMenu
from repositoryEmployee import employeeRepository
from insertionMonad import insertEmployee
from employeeHelpers import insertSampleEmployee


# Use a função insertEmployee


# result = insertEmployee("Novo Funcionário", "novo@email.com", "Novo Cargo", 6000)  
#if result.success:
#    print(result.value)
#else:
#    print(f"Falha: {result.value}")


# Exibe todos os funcionários após a inserção
repository = employeeRepository()
getEmployees = repository['getEmployees']
getEmployees() 
