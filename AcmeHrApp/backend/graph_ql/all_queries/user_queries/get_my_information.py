from ....queries.user_queries.get_employee_department_info import get_employee_department_info
from ....queries.user_queries.get_employee_salary_info import get_employee_salary_info
from ....queries.user_queries.get_employee_title_info import get_employee_title_info


def get_my_information_query(employee_id):
    dept_info = get_employee_department_info(employee_id)
    salary_info = get_employee_salary_info(employee_id)
    title_info = get_employee_title_info(employee_id)
    response = {'deptInfo': dept_info,
                'salaryInfo': salary_info, 'titleInfo': title_info}
    return response
