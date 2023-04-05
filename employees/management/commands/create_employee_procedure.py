from django.core.management.base import BaseCommand
from django.db import connection

# Command to create a stored procedure that saves employees
class Command(BaseCommand):
    help = 'Creates the create_employee procedure in the database'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE PROCEDURE `create_employee`(IN emp_num VARCHAR(10), IN emp_name VARCHAR(255), IN emp_role VARCHAR(2))
                BEGIN
                    INSERT INTO employees_employee (employee_number, name, role, base_salary, deliveries_payment_employee) VALUES (emp_num, emp_name, emp_role, 30.00, 5.00);
                END
            """)
        self.stdout.write(self.style.SUCCESS('Procedure created successfully.'))