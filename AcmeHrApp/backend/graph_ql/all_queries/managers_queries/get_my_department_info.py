from ....models import Department
from ....queries.manager_queries.get_department_employees import get_department_employees


def get_my_department_info_query(dept_no):
    department_employees = get_department_employees(dept_no)
    department = Department.objects.filter(
        dept_no=dept_no).all().values('dept_no', 'dept_name')
    response = {
        'department': department[0], 'departmentEmployees': department_employees}
    return response
