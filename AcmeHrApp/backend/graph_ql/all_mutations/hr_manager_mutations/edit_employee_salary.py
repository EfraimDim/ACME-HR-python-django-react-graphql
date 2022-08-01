from ....queries.hr_manager_queries.edit_current_employee_salary_info import edit_current_employee_salary_info
from ....queries.hr_manager_queries.add_new_employee_salary import add_new_employee_salary


def edit_employee_salary_mutation(employee_id, new_salary, new_salary_start_date):
    edit_current_employee_salary_info(employee_id, new_salary_start_date)
    add_new_employee_salary(employee_id, new_salary, new_salary_start_date)
    return 'Salary Information updated to the database!'
