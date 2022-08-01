from graphql import GraphQLError
from ....models import Employee, DeptManager
from ....queries.user_queries.get_all_employees import get_all_employees
from ....queries.user_queries.get_total_active_employees import get_total_active_employees


def login_query(employee_id, password):
        employee = Employee.objects.filter(emp_no=employee_id).values()
        if(len(employee) == 0):
            raise GraphQLError('Employee ID Doesnt Exist!')
        if(employee[0]['birth_date'].strftime('%Y-%m-%d') == password):
            pass
        else:
            raise GraphQLError('Incorrect Password')

        depManager = DeptManager.objects.filter(emp_no=employee_id).values()

        if (len(depManager) == 0):
            accessibility = 'regularEmp'
            dept_no = ''
        elif (depManager[0]['dept_no_id'] == 'd003'):
            accessibility = 'managerHR'
            dept_no = depManager[0]['dept_no_id']
        else:
            accessibility = 'manager'
            dept_no = depManager[0]['dept_no_id']

        total_active_employees = get_total_active_employees()

        colleagues = get_all_employees(1000, 0)

        user = {'userInfo': employee[0],
                'accessibility': accessibility, 'dept_no': dept_no}
        response = {'user': user, 'colleagues': colleagues,
                    'totalEmployeeCount': total_active_employees}
        return response
