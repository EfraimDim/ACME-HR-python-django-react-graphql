from ....queries.hr_manager_queries.edit_current_employee_title_info import edit_current_employee_title_info
from ....queries.hr_manager_queries.add_new_employee_title import add_new_employee_title
from ....queries.hr_manager_queries.add_new_employee_dept_manager import add_new_employee_dept_manager
from ....queries.hr_manager_queries.edit_current_employee_dept_manager_info import edit_current_employee_dept_manager_info



def edit_employee_role_mutation(employee_id, dept_no, original_role, new_role, new_role_start_date):
    edit_current_employee_title_info(employee_id, new_role_start_date)
    add_new_employee_title(employee_id, new_role, new_role_start_date)
    if (new_role == "Manager" and original_role != "Manager"):
        add_new_employee_dept_manager(
            employee_id, dept_no, new_role_start_date)
    if (original_role == "Manager" and new_role != "Manager"):
        edit_current_employee_dept_manager_info(
            employee_id, new_role_start_date)
    return 'Title Information updated to the database!'
