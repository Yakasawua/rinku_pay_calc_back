from django.core.management.base import BaseCommand
from django.db import connection

# Command to create a trigger to update an employee\'s bonus_hourly
class Command(BaseCommand):
    help = 'Create a trigger to update an employee\'s bonus_hourly'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TRIGGER update_employee_bonus_hourly
                BEFORE INSERT ON employees_employee
                FOR EACH ROW
                BEGIN
                    IF NEW.role = 'CH' THEN
                        SET NEW.bonus_hourly = 10;
                    ELSEIF NEW.role = 'CA' THEN
                        SET NEW.bonus_hourly = 5;
                    ELSEIF NEW.role = 'AU' THEN
                        SET NEW.bonus_hourly = 0;
                    END IF;
                END;
            """)
        self.stdout.write(self.style.SUCCESS('Trigger created successfully.'))