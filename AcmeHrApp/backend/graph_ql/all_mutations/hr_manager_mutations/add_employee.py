from ....models import Employee
from ....queries.hr_manager_queries.add_employee_to_database import add_employee_to_database
from graphql import GraphQLError

def add_employee_mutation(first_name, last_name, gender, birth_date, emp_num, role, department, hire_date, salary):
    employee_id_available = Employee.objects.filter(
        emp_no=emp_num).values()
    if (len(employee_id_available) == 0):
        pass
    else:
        raise GraphQLError('Employee ID taken')
    add_employee_to_database(first_name, last_name, gender, birth_date, emp_num, role, department, hire_date, salary)
    return 'Employee Succesfully added to database!'
