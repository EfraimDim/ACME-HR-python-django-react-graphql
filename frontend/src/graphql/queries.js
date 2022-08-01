import { gql } from "@apollo/client";

const LOGIN_QUERY = `
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
}`;

const LOGIN = gql`
  ${LOGIN_QUERY}
`;

const GET_PAGINATED_COLLEAGUES_QUERY = `
query getPaginatedColleagues($cursor: Int!) {
  getPaginatedColleagues(cursor: $cursor) {
    hasNextPage
    colleagues {
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
`;

const GET_PAGINATED_COLLEAGUES = gql`
  ${GET_PAGINATED_COLLEAGUES_QUERY}
`;

const GET_EMPLOYEE_DETAILS_QUERY = `
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
`;

const GET_EMPLOYEE_DETAILS = gql`
  ${GET_EMPLOYEE_DETAILS_QUERY}
`;

const GET_MY_INFORMATION_QUERY = `
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
`;

const GET_MY_INFORMATION = gql`
  ${GET_MY_INFORMATION_QUERY}
`;

const GET_MY_DEPARTMENT_INFO_QUERY = `
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
`;

const GET_MY_DEPARTMENT_INFO = gql`
  ${GET_MY_DEPARTMENT_INFO_QUERY}
`;

const GET_MY_ORGANISATION_INFO_QUERY = `
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
`;

const GET_MY_ORGANISATION_INFO = gql`
  ${GET_MY_ORGANISATION_INFO_QUERY}
`;

export {
  LOGIN_QUERY,
  GET_MY_DEPARTMENT_INFO_QUERY,
  GET_MY_ORGANISATION_INFO_QUERY,
  LOGIN,
  GET_PAGINATED_COLLEAGUES_QUERY,
  GET_EMPLOYEE_DETAILS_QUERY,
  GET_EMPLOYEE_DETAILS,
  GET_PAGINATED_COLLEAGUES,
  GET_MY_INFORMATION_QUERY,
  GET_MY_INFORMATION,
  GET_MY_DEPARTMENT_INFO,
  GET_MY_ORGANISATION_INFO,
};
