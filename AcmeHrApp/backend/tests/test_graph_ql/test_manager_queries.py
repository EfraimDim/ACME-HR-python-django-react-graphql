from ..set_up import set_up_departments, set_up_manager, set_up_regular_employee
from django.test import TestCase
import unittest
import xmlrunner
from ...graph_ql.schema import schema
from graphene.test import Client

GET_EMPLOYEE_DETAILS_QUERY = '''
query getEmployeeDetails($empNo: Int!, $accessibility: String!) {
  getEmployeeDetails(empNo: $empNo, accessibility: $accessibility) {
    deptInfo {
      departments {
        deptName
        deptNo
      }
      deptEmp {
        empNo
        fromDate
        toDate
        deptNo
      }  
    }
    salaryInfo {
      empNo
      salary
      fromDate
      toDate
    }
    titleInfo {
      empNo
      title
      fromDate
      toDate
    }
    user {
      userInfo {
        birthDate
        empNo
        firstName
        lastName
        gender
        hireDate
      }
    }
    employeesManager {
      birthDate
      empNo
      firstName
      lastName
      gender
      hireDate
    }
  }
}
'''

GET_MY_DEPARTMENT_INFO_QUERY = '''
query getMyDepartmentInfo($deptNo: String!) {
  getMyDepartmentInfo(deptNo: $deptNo) {
    department {
      deptName
      deptNo
    }
    departmentEmployees {
    	pageInfo {
      	startCursor
      	endCursor
      	hasNextPage
      	hasPreviousPage
      	}
      	edges {
        	cursor
        	node {
          	title {
            	title
            	toDate
          	}
          	birthDate
          	empNo
          	firstName
          	lastName
          	gender
          	hireDate
        	}
      	}
    	}
  }
}
'''


class ManagerQueriesTestCase(TestCase):
    def setUp(self):
        set_up_departments()
        set_up_manager()
        set_up_regular_employee()

    def test_get_employee_details_correct_emp_no(self):
        client = Client(schema)
        variables = {
            'empNo': 777777, 'accessibility': 'managerHR'
        }
        executed = client.execute(
            GET_EMPLOYEE_DETAILS_QUERY, None, None, variables)
        self.assertEqual(executed['data']['getEmployeeDetails']
                         ['user']['userInfo']['empNo'], 777777)
        self.assertEqual(
            executed['data']['getEmployeeDetails']['user']['userInfo']['birthDate'], '1999-02-02')
        self.assertEqual(executed['data']['getEmployeeDetails']['user']
                         ['userInfo']['firstName'], 'Regular')
        self.assertEqual(executed['data']['getEmployeeDetails']['user']
                         ['userInfo']['lastName'], 'Employee')
        self.assertEqual(
            executed['data']['getEmployeeDetails']['user']['userInfo']['gender'], 'F')
        self.assertEqual(executed['data']['getEmployeeDetails']
                         ['user']['userInfo']['hireDate'], '2010-01-01')
        self.assertEqual(executed['data']['getEmployeeDetails']['salaryInfo'], [{'empNo': 777777, 'salary': '60000', 'fromDate': '2014-01-01', 'toDate': '9999-01-01'}, {
                         'empNo': 777777, 'salary': '50000', 'fromDate': '2012-01-01', 'toDate': '2014-01-01'}, {'empNo': 777777, 'salary': '40000', 'fromDate': '2010-01-01', 'toDate': '2012-01-01'}])
        self.assertEqual(executed['data']['getEmployeeDetails']['titleInfo'], [{'empNo': 777777, 'title': 'Senior Staff', 'fromDate': '2012-01-01', 'toDate': '9999-01-01'}, {
                         'empNo': 777777, 'title': 'Staff', 'fromDate': '2010-01-01', 'toDate': '2012-01-01'}])
        self.assertEqual(executed['data']['getEmployeeDetails']['employeesManager'], {
                         'empNo': 8888888, 'birthDate': '1990-01-01', 'firstName': 'Practice', 'lastName': 'Test', 'gender': 'M', 'hireDate': '2000-01-01'})

    def test_get_employee_details_incorrect_emp_no(self):
        client = Client(schema)
        variables = {
            'empNo': 77777, 'accessibility': 'managerHR'
        }
        executed = client.execute(
            GET_EMPLOYEE_DETAILS_QUERY, None, None, variables)
        self.assertEqual(executed['errors'][0]
                         ['message'], 'Employee ID not found')

    def test_get_my_department_info_view(self):
        client = Client(schema)
        variables = {
            'deptNo': 'd003'
        }
        executed = client.execute(
            GET_MY_DEPARTMENT_INFO_QUERY, None, None, variables)
        print(executed['data']['getMyDepartmentInfo']
              ['departmentEmployees']['edges'])
        self.assertEqual(executed['data']['getMyDepartmentInfo']['department'], {
                         'deptName': 'Testing3', 'deptNo': 'd003'})
        self.assertEqual(executed['data']['getMyDepartmentInfo']['departmentEmployees']['edges'], [{'cursor': 'YXJyYXljb25uZWN0aW9uOjA=', 'node': {'title': {'title': 'Senior Staff', 'toDate': '9999-01-01'}, 'birthDate': '1999-02-02', 'empNo': 777777, 'firstName': 'Regular', 'lastName': 'Employee', 'gender': 'F', 'hireDate': '2010-01-01'}}, {
                         'cursor': 'YXJyYXljb25uZWN0aW9uOjE=', 'node': {'title': {'title': 'Manager', 'toDate': '9999-01-01'}, 'birthDate': '1990-01-01', 'empNo': 8888888, 'firstName': 'Practice', 'lastName': 'Test', 'gender': 'M', 'hireDate': '2000-01-01'}}])


if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        # these make sure that some options that are not applicable
        # remain hidden from the help menu.
        failfast=False, buffer=False, catchbreak=False)
