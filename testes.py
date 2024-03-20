import unittest
from repositoryEmployee import employeeRepository


class TestEmployeeRepository(unittest.TestCase):

    def setUp(self):
        self.repository = employeeRepository()

    def test_insertEmployee_valid_data(self):
        result = self.repository['insertEmployee']('Funcionario Teste', 'teste@teste.com', 'Cargo Teste', 5000)
        self.assertTrue(result.success)

    def test_insertEmployee_invalid_data(self):
        result = self.repository['insertEmployee']('', 'teste.com', '', -100)
        self.assertFalse(result.success)  # Verifica se a operação falhou
        self.assertIn("invalid", result.value.lower())  # Verifica se a mensagem de erro contém "invalid"

    def test_deleteEmployee_existing_employee(self):
        # Assuming there is at least one employee in the database
        existing_employee = self.repository['getEmployees']()[0]
        if existing_employee:
            existing_employee_id = existing_employee[0]
            result = self.repository['deleteEmployee'](existing_employee_id)
            self.assertTrue(result.success)
            self.assertEqual(result.value, "Employee deleted")
        else:
            self.fail("No existing employee found in the database")

    def test_deleteEmployee_non_existing_employee(self):
        result = self.repository['deleteEmployee'](9999)  # Assuming this ID doesn't exist
        self.assertFalse(result.success)
        self.assertIn("not found", result.value.lower())

    def test_getEmployeeById_existing_id(self):
        result = self.repository['getEmployeeById'](1, lambda emp: emp)
        self.assertIsNotNone(result)

    def test_getEmployeeById_non_existing_id(self):
        result = self.repository['getEmployeeById'](9999, lambda emp: emp)  # Assuming this ID doesn't exist
        self.assertIn("Employee not found", result.value)

    def test_getEmployees(self):
        employees = self.repository['getEmployees']()
        self.assertIsNotNone(employees)
        # Add more assertions to check the correctness of the returned employees list

    def test_editEmployee_existing_employee(self):
        # Assuming there is at least one employee in the database
        existing_employee = self.repository['getEmployees']()[0]
        if existing_employee:
            existing_employee_id = existing_employee[0]
            result = self.repository['editEmployee'](existing_employee_id, 'New Name', 'New Role', 6000)
            self.assertTrue(result.success)
            self.assertEqual(result.value, "Employee edited")
        else:
            self.fail("No existing employee found in the database")

    def test_editEmployee_non_existing_employee(self):
        result = self.repository['editEmployee'](9999, 'New Name', 'New Role', 6000)  # Assuming this ID doesn't exist
        self.assertFalse(result.success)
        self.assertEqual(result.value, "Employee not found")

    def test_searchEmployeesByRole_existing_role(self):
        result = self.repository['searchEmployeesByRole']('CEO')  # Assuming this role exists
        self.assertIsNotNone(result)
        self.assertTrue(any(emp[3].startswith('CEO') for emp in result))

    def test_searchEmployeesByRole_non_existing_role(self):
        result = self.repository['searchEmployeesByRole']('Non Existing Role')  
        self.assertIsNone(result)  # Verifying if the result is None
        if result is not None:
            self.assertIn("not found", result.lower())


if __name__ == '__main__':
    unittest.main()
