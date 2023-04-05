from django.core.management.base import BaseCommand
from django.db import connection

# Command to create the calculate_payroll stored procedure
class Command(BaseCommand):
    help = 'Creates the calculate_payroll stored procedure'

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute('''
                CREATE PROCEDURE calculate_payroll (
                    IN employee_id INT,
                    IN month DATE,
                    IN deliveries INT,
                    IN worked_hours DECIMAL(10,2)
                )
                BEGIN
                    DECLARE base_salary_ DECIMAL(10,2);
                    DECLARE deliveries_payment_employee_ DECIMAL(10,2);
                    DECLARE deliveries_payment DECIMAL(10,2);
                    DECLARE bonus_hourly_ DECIMAL(10,2);
                    DECLARE bonus_payment DECIMAL(10,2);
                    DECLARE isr_retention DECIMAL(10,2);
                    DECLARE grocery_vouchers DECIMAL(10,2);
                    DECLARE total_salary DECIMAL(10,2);

                    SELECT base_salary, deliveries_payment_employee, bonus_hourly
                    INTO base_salary_, deliveries_payment_employee_, bonus_hourly_
                    FROM employees_employee
                    WHERE id = employee_id;

                    SET deliveries_payment = deliveries * deliveries_payment_employee_;
                    SET bonus_payment = bonus_hourly_ * worked_hours;
                    SET base_salary_ = base_salary_ * worked_hours;
                    SET total_salary = base_salary_ + deliveries_payment + bonus_payment;
                    
                    IF total_salary > 10000 THEN
                        SET isr_retention = total_salary * 0.12;
                    ELSE
                        SET isr_retention = total_salary * 0.09;
                    END IF;

                    SET grocery_vouchers = 0.04 * total_salary;
                    SET total_salary = total_salary - isr_retention + grocery_vouchers;

                    INSERT INTO payroll_payroll (
                        employee_id, month, deliveries, worked_hours, deliveries_payment,
                        bonus_payment, isr_retention, grocery_vouchers, total_salary
                    ) VALUES (
                        employee_id, month, deliveries, worked_hours, deliveries_payment,
                        bonus_payment, isr_retention, grocery_vouchers, total_salary
                    );
                END;
            ''')
            self.stdout.write(self.style.SUCCESS('Stored procedure created successfully'))