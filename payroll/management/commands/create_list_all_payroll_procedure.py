from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = 'Creates a stored procedure to get payroll list by month and year'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute('''
                CREATE PROCEDURE `payroll_list_by_month_year`(
                    IN month_year DATE
                )
                BEGIN
                    SELECT *
                    FROM payroll_payroll
                    WHERE YEAR(month) = YEAR(month_year)
                    AND MONTH(month) = MONTH(month_year);
                END
            ''')
        self.stdout.write(self.style.SUCCESS('Procedure created successfully.'))