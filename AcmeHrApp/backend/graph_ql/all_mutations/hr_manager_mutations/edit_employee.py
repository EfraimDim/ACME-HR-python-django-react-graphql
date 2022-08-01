from ....queries.hr_manager_queries.edit_current_employee_basic_info import edit_current_employee_basic_info
from ....queries.hr_manager_queries.edit_current_employee_title_info import edit_current_employee_title_info
from ....queries.hr_manager_queries.add_new_employee_title import add_new_employee_title
from ....queries.hr_manager_queries.edit_current_employee_department_info import edit_current_employee_department_info
from ....queries.hr_manager_queries.add_new_employee_department import add_new_employee_department
from ....queries.hr_manager_queries.add_new_employee_dept_manager import add_new_employee_dept_manager
from ....queries.hr_manager_queries.edit_current_employee_dept_manager_info import edit_current_employee_dept_manager_info


def edit_employee_mutation(first_name, last_name, gender, birth_date, employee_id, new_role, new_dept_no, hire_date, original_dept_no, original_role, current_date):
    edit_current_employee_basic_info(
        first_name, last_name, gender, birth_date, employee_id, hire_date)
    if (new_role != original_role):
        edit_current_employee_title_info(employee_id, current_date)
        add_new_employee_title(employee_id, new_role, current_date)

    if (new_dept_no != original_dept_no):
        edit_current_employee_department_info(employee_id, current_date)
        add_new_employee_department(employee_id, new_dept_no, current_date)

    if (new_role == "Manager" and original_role != "Manager"):
        add_new_employee_dept_manager(
            employee_id, new_dept_no, current_date)

    if (original_role == "Manager" and new_role != "Manager"):
        edit_current_employee_dept_manager_info(employee_id, current_date)

    return 'Employee Details Succesfully Edited in the database!'
