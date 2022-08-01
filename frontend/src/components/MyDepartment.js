import styles from "../styles/MyDepartment.module.css";
import { useContext, useEffect } from "react";
import { AppContext } from "./AppContext";
import EmployeeTable from "./EmployeeTable";
import InformationBasic from "./InformationBasic";
import InformationRoleHistory from "./InformationRoleHistory";
import InformationSalary from "./InformationSalary";
import RoleDepartmentToggle from "./RoleDepartmentToggle";
import InformationDepartmentHistory from "./InformationDepartmentHistory";
import { GET_MY_DEPARTMENT_INFO } from "../graphql/queries";
import { useLazyQuery } from "@apollo/client";
import LoadingSpinner from "./LoadingButtonComponent"

function MyDepartment() {
  const {
    paginationPageDepEmp,
    setPaginationPageDepEmp,
    setPaginationDepEmpArray,
    paginationDepEmpArray,
    paginationCountDepEmp,
    employeeDepInfo,
    paginationCountSalaryDepEmp,
    paginationSalaryArrayDepEmp,
    setPaginationSalaryArrayDepEmp,
    paginationPageSalaryDepEmp,
    setPaginationPageSalaryDepEmp,
    roleDepartmentToggle,
    setPaginationCountDepEmp,
    setMyDepartment,
    myDepartmentInfoCalledOnce,
    myDepartment,
    loginInfo
  } = useContext(AppContext);

  const [getMyDepartmentInfo] = useLazyQuery(GET_MY_DEPARTMENT_INFO, {
    onCompleted: (myDepartmentInformation) => {
      try {
        console.log(myDepartmentInformation)
        setPaginationCountDepEmp(Math.ceil(myDepartmentInformation.getMyDepartmentInfo.departmentEmployees.edges.length / 10));
        setPaginationDepEmpArray(myDepartmentInformation.getMyDepartmentInfo.departmentEmployees.edges.slice(0, 10));
        setMyDepartment(myDepartmentInformation.getMyDepartmentInfo)
      } catch (e) {
        console.log(e);
      }
    },
  });

  useEffect(() => {
    if (myDepartmentInfoCalledOnce.current) {
      return;
    } else {
      getMyDepartmentInfo({ variables: { deptNo: loginInfo.user.deptNo } });
      myDepartmentInfoCalledOnce.current = true;
    }
  });

  return (
    <>
      {!myDepartment ? (
        <LoadingSpinner loadSpinner={!myDepartment} />
      ) : (
        <>
          {myDepartment && (
            <div>
              <h1 className={styles.headerMain}>Department</h1>
              <div className={styles.departmentName}>{myDepartment.department.dept_name}</div>
              <EmployeeTable
                manager={true}
                arrayToPaginate={myDepartment.departmentEmployees.edges}
                paginatedArray={paginationDepEmpArray}
                setPaginatedArray={setPaginationDepEmpArray}
                paginationCount={paginationCountDepEmp}
                paginationPage={paginationPageDepEmp}
                setPaginationPage={setPaginationPageDepEmp}
              />
              {employeeDepInfo && (
                <>
                  <InformationBasic employeeInfo={employeeDepInfo} />
                  <RoleDepartmentToggle />
                  {roleDepartmentToggle ? (
                    <InformationRoleHistory employeeInfo={employeeDepInfo} />
                  ) : (
                    <InformationDepartmentHistory employeeInfo={employeeDepInfo} />
                  )}
                  <InformationSalary
                    arrayToPaginate={employeeDepInfo.salaryInfo}
                    paginatedArray={paginationSalaryArrayDepEmp}
                    setPaginatedArray={setPaginationSalaryArrayDepEmp}
                    paginationCount={paginationCountSalaryDepEmp}
                    paginationPage={paginationPageSalaryDepEmp}
                    setPaginationPage={setPaginationPageSalaryDepEmp}
                  />
                </>
              )}
            </div>
          )}
        </>
      )}
    </>
  );
}

export default MyDepartment;
