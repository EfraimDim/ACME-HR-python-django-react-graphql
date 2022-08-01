from ....queries.hr_manager_queries.edit_current_employee_department_info import edit_current_employee_department_info
from ....queries.hr_manager_queries.add_new_employee_department import add_new_employee_department


def edit_employee_department_mutation(employee_id, new_dept_no, new_department_start_date):
    edit_current_employee_department_info(
        employee_id, new_department_start_date)
    add_new_employee_department(
        employee_id, new_dept_no, new_department_start_date)
    return 'Department Information updated to the database!'
