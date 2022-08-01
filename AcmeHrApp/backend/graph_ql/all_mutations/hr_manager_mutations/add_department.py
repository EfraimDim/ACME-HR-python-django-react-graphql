from ....models import Employee
from ....queries.hr_manager_queries.edit_current_employee_title_info import edit_current_employee_title_info
from ....queries.hr_manager_queries.add_new_employee_title import add_new_employee_title
from ....queries.hr_manager_queries.edit_current_employee_department_info import edit_current_employee_department_info
from ....queries.hr_manager_queries.add_new_employee_department import add_new_employee_department
from ....queries.hr_manager_queries.add_new_employee_dept_manager import add_new_employee_dept_manager
from ....queries.hr_manager_queries.edit_current_employee_dept_manager_info import edit_current_employee_dept_manager_info
from ....queries.hr_manager_queries.find_new_managers_current_role import find_new_managers_current_role
from ....queries.hr_manager_queries.add_new_department import add_new_department
from graphql import GraphQLError


def add_department_mutation(managers_employee_id, dept_no, dept_name, start_date):
    emp_id_exists = Employee.objects.filter(
        emp_no=managers_employee_id).values()
    if (len(emp_id_exists) != 0):
        managers_current_role = find_new_managers_current_role(
            managers_employee_id)
        new_manager = emp_id_exists[0]
    else:
        raise GraphQLError('Employee Number Does not Exist')
    add_new_department(dept_no, dept_name)
    edit_current_employee_department_info(managers_employee_id, start_date)
    add_new_employee_department(managers_employee_id, dept_no, start_date)
    edit_current_employee_title_info(managers_employee_id, start_date)
    add_new_employee_title(managers_employee_id, "Manager", start_date)
    if (managers_current_role == "Manager"):
        edit_current_employee_dept_manager_info(
            managers_employee_id, start_date)
    add_new_employee_dept_manager(
        managers_employee_id, dept_no, start_date)
    response = {'message': 'Department added to the database!',
                'newManager': new_manager}
    return response
