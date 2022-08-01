import json
from ..set_up import set_up_departments, set_up_manager, set_up_regular_employee
from django.test import TestCase
from datetime import datetime
from ...models import Department, DeptEmp, DeptManager, Employee, Salary, Title
import unittest
import xmlrunner
from ...graph_ql.schema import schema
from graphene.test import Client

GET_MY_ORGANISATION_INFO_QUERY = '''
query getMyOrganisationInfo {
  getMyOrganisationInfo {
    deptWithManagersList{
      department {
      deptNo_DeptName
      deptNo
      total
      }
      manager {
        empNo
        empNo_FirstName
        empNo_LastName
      }
    }
    titlesList {
      title
      }
    }
  }
'''

ADD_EMPLOYEE_MUTATION = '''
mutation addEmployee(
  $firstName: String!
  $lastName: String!
  $gender: String!
  $birthDate: String!
  $empNum: String!
  $role: String!
  $department: String!
  $hireDate: String!
  $salary: String!
) {
  addEmployee(
    firstName: $firstName
    lastName: $lastName
    gender: $gender
    birthDate: $birthDate
    empNum: $empNum
    role: $role
    department: $department
    hireDate: $hireDate
    salary: $salary
  ) {
    message
  }
}
'''

EDIT_EMPLOYEE_MUTATION = '''
mutation editEmployee(
  $firstName: String!
  $lastName: String!
  $gender: String!
  $birthDate: String!
  $empNum: String!
  $originalDeptNo: String!
  $originalRole: String!
  $role: String!
  $department: String!
  $hireDate: String!
  $currentDate: String!
) {
  editEmployee(
    firstName: $firstName
    lastName: $lastName
    gender: $gender
    birthDate: $birthDate
    empNum: $empNum
    originalDeptNo: $originalDeptNo
    originalRole: $originalRole
    role: $role
    department: $department
    hireDate: $hireDate
    currentDate: $currentDate
  ) {
    message
  }
}
'''

EDIT_EMPLOYEE_ROLE_MUTATION = '''
mutation editEmployeeRole($empNum: Int!, $departmentNo: String!, $originalRole: String!, $newRole: String!, $newRoleStartDate: String!) {
  editEmployeeRole(
    empNum: $empNum
    departmentNo: $departmentNo
    originalRole: $originalRole
    newRole: $newRole
    newRoleStartDate: $newRoleStartDate
  ) {
    message
  }
}
'''

EDIT_EMPLOYEE_DEPARTMENT_MUTATION = '''
mutation editEmployeeDepartment($empNum: Int!, $newDepartmentNo: String!, $newDepartmentStartDate: String!) {
  editEmployeeDepartment(empNum: $empNum, newDepartmentNo: $newDepartmentNo, newDepartmentStartDate: $newDepartmentStartDate) {
    message
  }
}
'''

EDIT_EMPLOYEE_SALARY_MUTATION = '''
mutation editEmployeeSalary($empNum: Int!, $newSalary: String!, $newSalaryStartDate: String!) {
  editEmployeeSalary(empNum: $empNum, newSalary: $newSalary, newSalaryStartDate: $newSalaryStartDate) {
    message
  }
}
'''

ADD_DEPARTMENT_MUTATION = '''
mutation addDepartment($deptNo: String!, $deptName: String!, $managersEmpNum: String!, $startDate: String!) {
  addDepartment(deptNo: $deptNo, deptName: $deptName, managersEmpNum: $managersEmpNum, startDate: $startDate) {
    message
    newManager {
      firstName
      lastName
    }
  }
}
'''

ADD_TITLE_MUTATION = '''
mutation addTitle($titleName: String!) {
  addTitle(titleName: $titleName) {
    message
  }
}
'''

class HRManagerQueryAndMutationsTestCase(TestCase):
    def setUp(self):
        set_up_departments()
        set_up_manager()
        set_up_regular_employee()

    def test_get_my_organisation_info_view(self):
        client = Client(schema)
        executed = client.execute(
            GET_MY_ORGANISATION_INFO_QUERY)
        self.assertEqual(executed['data']['getMyOrganisationInfo']['deptWithManagersList'], [{'department': {
                         'deptNo_DeptName': 'Testing3', 'deptNo': 'd003', 'total': 2}, 'manager': {'empNo': 8888888, 'empNo_FirstName': 'Practice', 'empNo_LastName': 'Test'}}])


    def test_add_employee(self):
        variables = {"firstName": "John", "lastName": "Smith", "gender": "M", "birthDate": "1994-01-01",
                                "empNum": "7777777", "role": "staff", "department": "d003", "hireDate": "1999-01-01", "salary": "100000"}
        client = Client(schema)
        executed = client.execute(
            ADD_EMPLOYEE_MUTATION, None, None, variables)
        self.assertEqual(executed['data']['addEmployee']['message'], 'Employee Succesfully added to database!')
        new_employee = Employee.objects.get(emp_no=7777777)
        self.assertEqual(new_employee.emp_no, 7777777)
        self.assertEqual(new_employee.first_name, 'John')
        self.assertEqual(new_employee.last_name, 'Smith')
        self.assertEqual(new_employee.gender, 'M')
        self.assertEqual(datetime.strftime(
            new_employee.birth_date, '%Y-%m-%d'), '1994-01-01')
        self.assertEqual(datetime.strftime(
            new_employee.hire_date, '%Y-%m-%d'), '1999-01-01')
        new_dept_employee = DeptEmp.objects.get(emp_no=7777777)
        self.assertEqual(new_dept_employee.emp_no_id, 7777777)
        self.assertEqual(new_dept_employee.dept_no_id, 'd003')
        self.assertEqual(datetime.strftime(
            new_dept_employee.from_date, '%Y-%m-%d'), '1999-01-01')
        self.assertEqual(datetime.strftime(
            new_dept_employee.to_date, '%Y-%m-%d'), '9999-01-01')
        new_title = Title.objects.get(emp_no=7777777)
        self.assertEqual(new_title.emp_no_id, 7777777)
        self.assertEqual(new_title.title, 'staff')
        self.assertEqual(datetime.strftime(
            new_title.from_date, '%Y-%m-%d'), '1999-01-01')
        self.assertEqual(datetime.strftime(
            new_title.to_date, '%Y-%m-%d'), '9999-01-01')
        new_salary = Salary.objects.get(emp_no=7777777)
        self.assertEqual(new_salary.emp_no_id, 7777777)
        self.assertEqual(new_salary.salary, 100000)
        self.assertEqual(datetime.strftime(
            new_salary.from_date, '%Y-%m-%d'), '1999-01-01')
        self.assertEqual(datetime.strftime(
            new_salary.to_date, '%Y-%m-%d'), '9999-01-01')

    def test_edit_employee(self):
        variables = {"firstName": "New",
                                   "lastName": "Name",
                                   "gender": "F",
                                   "birthDate": "1990-01-01",
                                   "empNum": "777777",
                                   "originalDeptNo": "d003",
                                   "originalRole": "Senior Staff",
                                   "role": "Expert Staff",
                                   "department": "d007",
                                   "hireDate": "2010-01-01",
                                   "currentDate": "2020-01-01", }
        client = Client(schema)
        executed = client.execute(
            EDIT_EMPLOYEE_MUTATION, None, None, variables)
        self.assertEqual(executed['data']['editEmployee']['message'], 'Employee Details Succesfully Edited in the database!')
        edited_employee = Employee.objects.get(emp_no=777777)
        self.assertEqual(edited_employee.emp_no, 777777)
        self.assertEqual(edited_employee.first_name, 'New')
        self.assertEqual(edited_employee.last_name, 'Name')
        self.assertEqual(edited_employee.gender, 'F')
        self.assertEqual(datetime.strftime(
            edited_employee.birth_date, '%Y-%m-%d'), '1990-01-01')
        self.assertEqual(datetime.strftime(
            edited_employee.hire_date, '%Y-%m-%d'), '2010-01-01')
        edited_dept_employee = DeptEmp.objects.filter(
            emp_no=777777).order_by('to_date').all().values()
        self.assertEqual(datetime.strftime(
            edited_dept_employee[0]['to_date'], '%Y-%m-%d'), '2020-01-01')
        self.assertEqual(datetime.strftime(
            edited_dept_employee[1]['from_date'], '%Y-%m-%d'), '2020-01-01')
        self.assertEqual(datetime.strftime(
            edited_dept_employee[1]['to_date'], '%Y-%m-%d'), '9999-01-01')
        self.assertEqual(edited_dept_employee[1]['dept_no_id'], 'd007')
        edited_title = Title.objects.filter(
            emp_no=777777).order_by('-from_date').all().values()
        self.assertEqual(datetime.strftime(
            edited_title[1]['to_date'], '%Y-%m-%d'), '2020-01-01')
        self.assertEqual(datetime.strftime(
            edited_title[0]['to_date'], '%Y-%m-%d'), '9999-01-01')
        self.assertEqual(datetime.strftime(
            edited_title[0]['from_date'], '%Y-%m-%d'), '2020-01-01')
        self.assertEqual(edited_title[0]['title'], 'Expert Staff')

    def test_edit_employee_role_not_manager(self):
        variables = {"empNum": 777777,
                             "originalRole": "Senior Staff",
                             "newRole": "Expert Staff",
                             "departmentNo": "d003",
                             "newRoleStartDate": "2020-01-01"}
        client = Client(schema)
        executed = client.execute(
            EDIT_EMPLOYEE_ROLE_MUTATION, None, None, variables)
        self.assertEqual(executed['data']['editEmployeeRole']['message'], 'Title Information updated to the database!')
        edited_title = Title.objects.filter(
            emp_no=777777).order_by('-from_date').all().values()
        self.assertEqual(datetime.strftime(
            edited_title[1]['to_date'], '%Y-%m-%d'), '2020-01-01')
        self.assertEqual(datetime.strftime(
            edited_title[0]['to_date'], '%Y-%m-%d'), '9999-01-01')
        self.assertEqual(datetime.strftime(
            edited_title[0]['from_date'], '%Y-%m-%d'), '2020-01-01')
        self.assertEqual(edited_title[0]['title'], 'Expert Staff')

    def test_edit_employee_role_new_manager(self):
        variables = {"empNum": 777777,
                             "originalRole": "Senior Staff",
                             "newRole": "Manager",
                             "departmentNo": "d003",
                             "newRoleStartDate": "2020-01-01"}
        client = Client(schema)
        executed = client.execute(
            EDIT_EMPLOYEE_ROLE_MUTATION, None, None, variables)
        self.assertEqual(executed['data']['editEmployeeRole']['message'], 'Title Information updated to the database!')
        edited_title = Title.objects.filter(
            emp_no=777777).order_by('-from_date').all().values()
        self.assertEqual(datetime.strftime(
            edited_title[1]['to_date'], '%Y-%m-%d'), '2020-01-01')
        self.assertEqual(datetime.strftime(
            edited_title[0]['to_date'], '%Y-%m-%d'), '9999-01-01')
        self.assertEqual(datetime.strftime(
            edited_title[0]['from_date'], '%Y-%m-%d'), '2020-01-01')
        self.assertEqual(edited_title[0]['title'], 'Manager')
        added_manager = DeptManager.objects.filter(
            emp_no=777777).order_by('-from_date').all().values()
        self.assertEqual(datetime.strftime(
            added_manager[0]['to_date'], '%Y-%m-%d'), '9999-01-01')
        self.assertEqual(datetime.strftime(
            added_manager[0]['from_date'], '%Y-%m-%d'), '2020-01-01')
        self.assertEqual(added_manager[0]['dept_no_id'], 'd003')

    def test_edit_employee_role_old_manager(self):
        variables = {"empNum": 8888888,
                             "originalRole": "Manager",
                             "newRole": "Staff",
                             "departmentNo": "d003",
                             "newRoleStartDate": "2020-01-01"}
        client = Client(schema)
        executed = client.execute(
            EDIT_EMPLOYEE_ROLE_MUTATION, None, None, variables)
        self.assertEqual(executed['data']['editEmployeeRole']['message'], 'Title Information updated to the database!')
        edited_title = Title.objects.filter(
            emp_no=8888888).order_by('-from_date').all().values()
        self.assertEqual(datetime.strftime(
            edited_title[1]['to_date'], '%Y-%m-%d'), '2020-01-01')
        self.assertEqual(edited_title[1]['title'], 'Manager')
        self.assertEqual(datetime.strftime(
            edited_title[0]['to_date'], '%Y-%m-%d'), '9999-01-01')
        self.assertEqual(datetime.strftime(
            edited_title[0]['from_date'], '%Y-%m-%d'), '2020-01-01')
        self.assertEqual(edited_title[0]['title'], 'Staff')
        added_manager = DeptManager.objects.filter(
            emp_no=8888888).order_by('-from_date').all().values()
        self.assertEqual(datetime.strftime(
            added_manager[0]['to_date'], '%Y-%m-%d'), '2020-01-01')
        self.assertEqual(added_manager[0]['dept_no_id'], 'd003')

    def test_edit_employee_department(self):
        variables = {
            "empNum": 777777,
            "newDepartmentNo": "d006",
            "newDepartmentStartDate": "2021-01-01",
        }
        client = Client(schema)
        executed = client.execute(
            EDIT_EMPLOYEE_DEPARTMENT_MUTATION, None, None, variables)
        self.assertEqual(executed['data']['editEmployeeDepartment']['message'], 'Department Information updated to the database!')
        edited_department = DeptEmp.objects.filter(
            emp_no=777777).order_by('-from_date').all().values()
        self.assertEqual(datetime.strftime(
            edited_department[1]['to_date'], '%Y-%m-%d'), '2021-01-01')
        self.assertEqual(datetime.strftime(
            edited_department[0]['to_date'], '%Y-%m-%d'), '9999-01-01')
        self.assertEqual(datetime.strftime(
            edited_department[0]['from_date'], '%Y-%m-%d'), '2021-01-01')
        self.assertEqual(edited_department[0]['dept_no_id'], 'd006')

    def test_edit_employee_salary(self):
        variables = {
            "empNum": 777777,
            "newSalary": "80000",
            "newSalaryStartDate": "2022-03-03"
        }
        client = Client(schema)
        executed = client.execute(
            EDIT_EMPLOYEE_SALARY_MUTATION, None, None, variables)
        self.assertEqual(executed['data']['editEmployeeSalary']['message'], 'Salary Information updated to the database!')
        edited_salary = Salary.objects.filter(
            emp_no=777777).order_by('-from_date').all().values()
        self.assertEqual(datetime.strftime(
            edited_salary[1]['to_date'], '%Y-%m-%d'), '2022-03-03')
        self.assertEqual(datetime.strftime(
            edited_salary[0]['to_date'], '%Y-%m-%d'), '9999-01-01')
        self.assertEqual(datetime.strftime(
            edited_salary[0]['from_date'], '%Y-%m-%d'), '2022-03-03')
        self.assertEqual(edited_salary[0]['salary'], 80000)

    def test_add_department(self):
        variables = {
            "deptNo": "d009",
            "deptName": "Testing9",
            "managersEmpNum": "777777",
            "startDate": "2022-03-04",
        }
        client = Client(schema)
        executed = client.execute(
            ADD_DEPARTMENT_MUTATION, None, None, variables)
        self.assertEqual(executed['data']['addDepartment']['message'], 'Department added to the database!')
        self.assertEqual(executed['data']['addDepartment']['newManager']['firstName'], 'Regular')
        self.assertEqual(executed['data']['addDepartment']['newManager']['lastName'], 'Employee')
        new_department = Department.objects.filter(
            dept_no='d009').all().values()
        self.assertEqual(new_department[0]['dept_no'], 'd009')
        self.assertEqual(new_department[0]['dept_name'], 'Testing9')
        self.assertEqual(len(new_department), 1)
        new_manager = DeptManager.objects.filter(emp_no=777777).all().values()
        self.assertEqual(len(new_manager), 1)
        self.assertEqual(new_manager[0]['dept_no_id'], 'd009')
        self.assertEqual(datetime.strftime(
            new_manager[0]['to_date'], '%Y-%m-%d'), '9999-01-01')
        self.assertEqual(datetime.strftime(
            new_manager[0]['from_date'], '%Y-%m-%d'), '2022-03-04')

        new_dept_emp = DeptEmp.objects.filter(
            emp_no=777777).order_by('-from_date').all().values()
        self.assertEqual(len(new_dept_emp), 2)
        self.assertEqual(new_dept_emp[0]['dept_no_id'], 'd009')
        self.assertEqual(datetime.strftime(
            new_dept_emp[0]['to_date'], '%Y-%m-%d'), '9999-01-01')
        self.assertEqual(datetime.strftime(
            new_dept_emp[0]['from_date'], '%Y-%m-%d'), '2022-03-04')
        self.assertEqual(new_dept_emp[1]['dept_no_id'], 'd003')
        self.assertEqual(datetime.strftime(
            new_dept_emp[1]['to_date'], '%Y-%m-%d'), '2022-03-04')
        self.assertEqual(datetime.strftime(
            new_dept_emp[1]['from_date'], '%Y-%m-%d'), '2010-01-01')

        new_title = Title.objects.filter(
            emp_no=777777).order_by('-from_date').all().values()
        self.assertEqual(datetime.strftime(
            new_title[1]['to_date'], '%Y-%m-%d'), '2022-03-04')
        self.assertEqual(new_title[1]['title'], 'Senior Staff')
        self.assertEqual(datetime.strftime(
            new_title[0]['to_date'], '%Y-%m-%d'), '9999-01-01')
        self.assertEqual(datetime.strftime(
            new_title[0]['from_date'], '%Y-%m-%d'), '2022-03-04')
        self.assertEqual(new_title[0]['title'], 'Manager')

    def test_add_title(self):
        Employee.objects.create(first_name='title', last_name='holder',
            emp_no=35128, birth_date='2000-01-01', gender='M', hire_date='2000-01-01')
        variables = {
            "titleName": "Tech King",
        }
        client = Client(schema)
        executed = client.execute(
            ADD_TITLE_MUTATION, None, None, variables)
        self.assertEqual(executed['data']['addTitle']['message'], 'Title added to the database!')
        new_title = Title.objects.filter(title='Tech King').all().values()
        self.assertEqual(len(new_title), 1)
        self.assertEqual(new_title[0]['title'], 'Tech King')


if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        # these make sure that some options that are not applicable
        # remain hidden from the help menu.
        failfast=False, buffer=False, catchbreak=False)
