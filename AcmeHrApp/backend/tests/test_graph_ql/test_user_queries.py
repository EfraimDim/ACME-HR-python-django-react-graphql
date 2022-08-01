from ..set_up import set_up_manager, set_up_departments
from django.test import TestCase
import unittest
import xmlrunner
from ...graph_ql.schema import schema
from graphene.test import Client

LOGIN_QUERY = '''
query login($employeeId: String! $password: String!) {
  login(employeeId: $employeeId password: $password) {
  	colleagues(first: 1000){
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
    user {
      userInfo {
        birthDate
        empNo
        firstName
        lastName
        gender
        hireDate
      }
      deptNo
      accessibility
    }
    totalEmployeeCount
	}
}
        '''

GET_MY_INFORMATION_QUERY = '''
query getMyInformation($employeeId: Int!) {
  getMyInformation(employeeId: $employeeId) {
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
  }
}

'''

class UserQueriesTestCase(TestCase):
    def setUp(self):
        set_up_departments()
        set_up_manager()

    def test_login_manager_user_query(self):
        client = Client(schema)
        variables = {
            'employeeId': '8888888', 'password': '1990-01-01'
        }
        executed = client.execute(LOGIN_QUERY, None, None, variables)
        self.assertEqual(executed['data']['login']
                         ['user']['userInfo']['empNo'], 8888888)
        self.assertEqual(executed['data']['login']['user']
                         ['userInfo']['birthDate'], '1990-01-01')
        self.assertEqual(executed['data']['login']['user']
                         ['userInfo']['firstName'], 'Practice')
        self.assertEqual(executed['data']['login']['user']
                         ['userInfo']['lastName'], 'Test')
        self.assertEqual(executed['data']['login']
                         ['user']['userInfo']['gender'], 'M')
        self.assertEqual(executed['data']['login']['user']
                         ['userInfo']['hireDate'], '2000-01-01')
        self.assertEqual(executed['data']['login']
                         ['user']['accessibility'], 'managerHR')
        self.assertDictEqual(executed['data']['login']['colleagues']['edges'][0]['node'], {'title': {
                             'title': 'Manager', 'toDate': '9999-01-01'}, 'birthDate': '1990-01-01', 'empNo': 8888888, 'firstName': 'Practice', 'lastName': 'Test', 'gender': 'M', 'hireDate': '2000-01-01'})
        assert executed == {'data': {'login': {'colleagues': {'pageInfo': {'startCursor': 'YXJyYXljb25uZWN0aW9uOjA=', 'endCursor': 'YXJyYXljb25uZWN0aW9uOjA=', 'hasNextPage': False, 'hasPreviousPage': False}, 'edges': [{'cursor': 'YXJyYXljb25uZWN0aW9uOjA=', 'node': {'title': {
            'title': 'Manager', 'toDate': '9999-01-01'}, 'birthDate': '1990-01-01', 'empNo': 8888888, 'firstName': 'Practice', 'lastName': 'Test', 'gender': 'M', 'hireDate': '2000-01-01'}}]}, 'user': {'userInfo': {'birthDate': '1990-01-01', 'empNo': 8888888, 'firstName': 'Practice', 'lastName': 'Test', 'gender': 'M', 'hireDate': '2000-01-01'}, 'deptNo': 'd003', 'accessibility': 'managerHR'}, 'totalEmployeeCount': 1}}}

    def test_login_incorrect_password(self):
        client = Client(schema)
        variables = {
            'employeeId': '8888888', 'password': '1990-01-03'
        }
        executed = client.execute(LOGIN_QUERY, None, None, variables)
        self.assertEqual(executed['errors'][0]
                         ['message'], 'Incorrect Password')

    def test_login_incorrect_id(self):
        client = Client(schema)
        variables = {
            'employeeId': '8888', 'password': '1990-01-01'
        }
        executed = client.execute(LOGIN_QUERY, None, None, variables)
        self.assertEqual(executed['errors'][0]
                         ['message'], 'Employee ID Doesnt Exist!')

    def test_my_information(self):
        client = Client(schema)
        variables = {
            'employeeId': 8888888
        }
        executed = client.execute(
            GET_MY_INFORMATION_QUERY, None, None, variables)
        self.assertEqual(executed['data']['getMyInformation']['deptInfo'], [{'departments': {'deptName': 'Testing3', 'deptNo': 'd003'}, 'deptEmp': {
                         'empNo': 8888888, 'fromDate': '2000-01-01', 'toDate': '9999-01-01', 'deptNo': 'd003'}}])
        self.assertDictEqual(executed['data']['getMyInformation']['salaryInfo'][0],
                             {'empNo': 8888888, 'salary': '100000', 'fromDate': '2000-01-01', 'toDate': '9999-01-01'})
        self.assertDictEqual(executed['data']['getMyInformation']['titleInfo'][0],
                             {'empNo': 8888888, 'title': 'Manager', 'fromDate': '2000-01-01', 'toDate': '9999-01-01'})

if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        # these make sure that some options that are not applicable
        # remain hidden from the help menu.
        failfast=False, buffer=False, catchbreak=False)
