# rinku pay calc back

Project considerations:  
Move the docker-compose.dev.yaml file to the folder where you did the git clone.  
Being in the same folder where the docker-compose.dev.yaml file is, use the following commands:  
docker compose -f docker-compose.dev.yaml build  
docker compose -f docker-compose.dev.yaml up

When starting the project for the first time it is necessary to do first:  
python manage.py migrate  

After doing the migrate it is necessary to run the following commands:  
python manage.py create_list_all_employees_procedure  
python manage.py create_employee_procedure  
python manage.py create_trigger_update_employee_bonus_hourly  
python manage.py create_list_all_payroll_procedure  
python manage.py create_payroll_procedure

You can configure the .env file not to use the database service created in the docker-compose.dev.yaml file,  
if it is not the case then when starting for the first time the backend will not be able to connect to the database  
because was being created, for this it is necessary to stop the back service and start it again.