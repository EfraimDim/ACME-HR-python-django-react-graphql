from ....models import Employee
from ....queries.user_queries.get_employee_department_info import get_employee_department_info
from ....queries.user_queries.get_employee_salary_info import get_employee_salary_info
from ....queries.user_queries.get_employee_title_info import get_employee_title_info
from ....queries.manager_queries.get_manager_of_employee import get_manager_of_employee
from graphql import GraphQLError


def get_employee_details_query(employee_id, accessibility):
    try:
        employee = Employee.objects.filter(emp_no=employee_id).values()
        dept_info = get_employee_department_info(employee_id)
        salary_info = get_employee_salary_info(employee_id)
        title_info = get_employee_title_info(employee_id)
        employees_manager = ''
        user = {'userInfo': employee[0]}
        if (accessibility == 'managerHR'):
            employees_manager = get_manager_of_employee(
                dept_info[0]['dept_emp']['dept_no'])
        response = {'user': user, 'deptInfo': dept_info, 'salaryInfo': salary_info,
                    'titleInfo': title_info, 'employeesManager': employees_manager}
        return response
    except(IndexError):
        raise GraphQLError('Employee ID not found')
