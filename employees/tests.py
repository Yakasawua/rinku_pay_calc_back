from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .models import Employee

#TODO: It is necessary to include the stored procedure that is being used

#Tests View
class EmployeeTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_employee(self):
        """
        Test creating a new employee with valid data
        """
        data = {
            'employee_number': '1234510',
            'name': 'John Doe',
            'role': 'CA'
        }
        response = self.client.post('/employees/create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that the employee exists in the database
        self.assertEqual(Employee.objects.count(), 1)
        self.assertEqual(Employee.objects.get().employee_number, '1234510')
        self.assertEqual(Employee.objects.get().name, 'John Doe')
        self.assertEqual(Employee.objects.get().role, 'CA')

    def test_create_employee_invalid_data(self):
        """
        Test creating a new employee with invalid data
        """
        data = {
            'employee_number': '',
            'name': '',
            'role': ''
        }
        response = self.client.post('/employees/create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Check that the employee does not exist in the database
        self.assertEqual(Employee.objects.count(), 0)

#Tests Model
class EmployeeModelTestCase(TestCase):
    
    def setUp(self):
        self.emp_num = '12345'
        self.emp_name = 'John Doe'
        self.emp_role = 'CH'

    def test_create_employee(self):
        # Create an employee
        created = Employee.create(self.emp_num, self.emp_name, self.emp_role)

        # Check that the employee was created successfully
        self.assertTrue(created)

        # Check that the employee exists in the database
        employee = Employee.objects.get(employee_number=self.emp_num)
        self.assertEqual(employee.name, self.emp_name)
        self.assertEqual(employee.role, self.emp_role)

    def test_create_employee_invalid(self):
        # Try to create an employee with an invalid role
        created = Employee.create(self.emp_num, self.emp_name, 'InvalidRole')
        
        # Check that the employee was not created
        self.assertFalse(created)

        # Check that the employee does not exist in the database
        with self.assertRaises(Employee.DoesNotExist):
            Employee.objects.get(employee_number=self.emp_num)