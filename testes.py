import unittest
from repositoryEmployee import employeeRepository

class TestEmployeeRepository(unittest.TestCase):

    def setUp(self):
        self.repository = employeeRepository()

    def test_insertEmployee_valid_data(self):
        result = self.repository['insertEmployee']('Funcionario Teste', 'teste@teste.com', 'Cargo Teste', 5000)
        self.assertEqual(result, "Employee registered")

    def test_insertEmployee_invalid_data(self):
        result = self.repository['insertEmployee']('', 'teste.com', '', -100)
        self.assertNotEqual(result, "Employee registered")
        self.assertIn("invalid", result.lower())

    def test_deleteEmployee_existing_employee(self):
        # Assuming employee with ID=1 exists for this test
        result = self.repository 
        self.assertEqual(result, "Employee deleted")

    def test_deleteEmployee_non_existing_employee(self):
        result = self.repository   # Assuming this ID doesn't exist
        self.assertIn("not found", result.lower())

    def test_getEmployeeById_existing_id(self):
        result = self.repository['getEmployeeById'](1, lambda emp: emp)
        self.assertIsNotNone(result)

    def test_getEmployeeById_non_existing_id(self):
        result = self.repository['getEmployeeById'](9999, lambda emp: emp)  # Assuming this ID doesn't exist
        self.assertIn("not found", result.lower())

    def test_getEmployees(self):
        employees = self.repository['getEmployees']()
        self.assertIsNotNone(employees)
        # Add more assertions to check the correctness of the returned employees list

    def test_editEmployee_existing_employee(self):
        # Assuming employee with ID=1 exists for this test
        result = self.repository['editEmployee'](1, 'New Name', 'New Role', 6000)
        self.assertEqual(result, "Employee edited")

    def test_editEmployee_non_existing_employee(self):
        result = self.repository['editEmployee'](9999, 'New Name', 'New Role', 6000)  # Assuming this ID doesn't exist
        self.assertIn("not found", result.lower())

    def test_searchEmployeesByRole_existing_role(self):
        result = self.repository['searchEmployeesByRole']('CEO')  # Assuming this role exists
        self.assertIsNotNone(result)

    def test_searchEmployeesByRole_non_existing_role(self):
        result = self.repository['searchEmployeesByRole']('Non Existing Role')  
        self.assertIn("not found", result.lower())

if __name__ == '__main__':
    unittest.main()
