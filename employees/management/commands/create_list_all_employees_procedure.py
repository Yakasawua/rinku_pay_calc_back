from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = 'Creates the get_all_employees procedure in the database'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE PROCEDURE `get_all_employees`()
                BEGIN
                    SELECT * FROM employees_employee;
                END
            """)
        self.stdout.write(self.style.SUCCESS('Procedure created successfully.'))