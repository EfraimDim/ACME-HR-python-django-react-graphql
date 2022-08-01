import { useState, useRef } from "react";
import "./styles/App.module.css";
import LoadingButtonComponent from "./components/LoadingButtonComponent";
import Login from "./components/Login";
import HomePage from "./components/HomePage";
import { AppContext } from "./components/AppContext";
import { useLocation } from "react-router-dom";
import { useLazyQuery } from "@apollo/client";
import { LOGIN, GET_MY_ORGANISATION_INFO, GET_EMPLOYEE_DETAILS, GET_PAGINATED_COLLEAGUES } from "./graphql/queries";
import swal from "sweetalert";

function App() {
  const [loginInfo, setLoginInfo] = useState(null);
  const [loadSpinner, setLoadSpinner] = useState(false);
  const [paginationCountEmployee, setPaginationCountEmployee] = useState(1);
  const [paginationEmployeeArray, setPaginationEmployeeArray] = useState([]);
  const [paginationPageEmployee, setPaginationPageEmployee] = useState(1);

  const [paginationCountSalary, setPaginationCountSalary] = useState(1);
  const [paginationSalaryArray, setPaginationSalaryArray] = useState([]);
  const [paginationPageSalary, setPaginationPageSalary] = useState(1);

  const [paginationCountDepEmp, setPaginationCountDepEmp] = useState(1);
  const [paginationDepEmpArray, setPaginationDepEmpArray] = useState([]);
  const [paginationPageDepEmp, setPaginationPageDepEmp] = useState(1);

  const [paginationCountSalaryDepEmp, setPaginationCountSalaryDepEmp] = useState(1);
  const [paginationSalaryArrayDepEmp, setPaginationSalaryArrayDepEmp] = useState([]);
  const [paginationPageSalaryDepEmp, setPaginationPageSalaryDepEmp] = useState(1);

  const [employeeDepInfo, setEmployeeDepInfo] = useState(null);

  const [roleDepartmentToggle, setRoleDepartmentToggle] = useState(true);

  const [addEmployee, setAddEmployee] = useState(false);
  const [editEmployee, setEditEmployee] = useState(false);

  const [updateRole, setUpdateRole] = useState(false);
  const [updateDepartment, setUpdateDepartment] = useState(false);
  const [updateSalary, setUpdateSalary] = useState(false);

  const [addDepartment, setAddDepartment] = useState(false);
  const [addTitle, setAddTitle] = useState(false);

  const [myInformation, setMyInformation] = useState(null);
  const [myDepartment, setMyDepartment] = useState(null);
  const [myOrganisation, setMyOrganisation] = useState(null);

  const [colleaguesCursor, setColleaguesCursor] = useState(0);
  const [hasNextPage, setHasNextPage] = useState(true);

  const myInformationCalledOnce = useRef(false);
  const myDepartmentInfoCalledOnce = useRef(false);
  const myOrganisationInfoCalledOnce = useRef(false);

  const location = useLocation();

  const [userLogin] = useLazyQuery(LOGIN, {
    onError: (error) => {
      setLoadSpinner(false);
      swal({
        title: "Login Failed!",
        text: `${error.message}`,
        icon: "error",
        button: "okay",
      });
    },
    onCompleted: (loginData) => {
      try {
        if (loginData.login === null) {
          return;
        }
        setPaginationCountEmployee(Math.ceil(loginData.login.colleagues.edges.length / 10));
        setPaginationEmployeeArray(loginData.login.colleagues.edges.slice(0, 10));
        console.log(loginData);
        setLoginInfo(loginData.login);
        swal({
          title: "Login Success!",
          text: `Welcome ${loginData.login.user.userInfo.firstName} ${loginData.login.user.userInfo.lastName}`,
          icon: "success",
          button: "continue!",
        });
      } catch (e) {
        setLoadSpinner(false);
        console.log(e);
      }
    },
  });

  const [getPaginatedColleagues] = useLazyQuery(GET_PAGINATED_COLLEAGUES, {
    onCompleted: (colleaguesData) => {
      try {
        if (colleaguesData.getPaginatedColleagues.hasNextPage === false) {
          setHasNextPage(false);
        }
        const newLoginInfo = { ...loginInfo };
        newLoginInfo.colleagues = colleaguesData.getPaginatedColleagues.colleagues.edges;
        setLoginInfo(newLoginInfo);
        setPaginationCountEmployee(Math.ceil(colleaguesData.getPaginatedColleagues.colleagues.edges.length / 10));
        setPaginationEmployeeArray(colleaguesData.getPaginatedColleagues.colleagues.edges.slice(0, 10));
      } catch (e) {
        console.log(e);
      }
    },
  });

  const [getMyOrganisationInfo] = useLazyQuery(GET_MY_ORGANISATION_INFO, {
    onCompleted: (myOrganisationInformation) => {
      try {
        console.log(myOrganisationInformation.getMyOrganisationInfo)
        setMyOrganisation(myOrganisationInformation.getMyOrganisationInfo);
      } catch (e) {
        console.log(e);
      }
    },
  });

  const [getEmployeeDetails] = useLazyQuery(GET_EMPLOYEE_DETAILS, {
    onCompleted: (employeeData) => {
      try {
        console.log(employeeData)
        setPaginationPageSalaryDepEmp(1);
        setPaginationCountSalaryDepEmp(Math.ceil(employeeData.getEmployeeDetails.salaryInfo.length / 10));
        setPaginationSalaryArrayDepEmp(employeeData.getEmployeeDetails.salaryInfo.slice(0, 10));
        setEmployeeDepInfo(employeeData.getEmployeeDetails);
      } catch (e) {
        console.log(e);
      }
    },
  });


  const displayEmployeeDetails = async (empNo) => {
    try {
      setEditEmployee(false);
      setUpdateRole(false);
      setUpdateDepartment(false);
      await getEmployeeDetails({ variables: { empNo: empNo, accessibility: loginInfo.user.accessibility } });
    } catch (e) {
      console.log(e);
    }
  };


  const updateNewRoleOnFrontend = (empNo, updatedRole) => {
    const newColleaguesArray = [...loginInfo.colleagues];
    const colleagueToUpdate = newColleaguesArray.find((colleague) => colleague.emp_no === empNo);
    colleagueToUpdate.title.title = updatedRole;
    setPaginationCountEmployee(Math.ceil(newColleaguesArray.length / 10));
    setPaginationEmployeeArray(newColleaguesArray.slice(0, 10));
  };

  return (
    <AppContext.Provider
      value={{
        setLoginInfo,
        loginInfo,
        setLoadSpinner,
        loadSpinner,
        paginationCountEmployee,
        setPaginationCountEmployee,
        paginationEmployeeArray,
        setPaginationEmployeeArray,
        paginationCountSalary,
        setPaginationCountSalary,
        paginationSalaryArray,
        setPaginationSalaryArray,
        paginationPageSalary,
        setPaginationPageSalary,
        paginationPageEmployee,
        setPaginationPageEmployee,
        paginationCountDepEmp,
        setPaginationCountDepEmp,
        paginationDepEmpArray,
        setPaginationDepEmpArray,
        paginationPageDepEmp,
        setPaginationPageDepEmp,
        employeeDepInfo,
        setEmployeeDepInfo,
        paginationCountSalaryDepEmp,
        setPaginationCountSalaryDepEmp,
        paginationSalaryArrayDepEmp,
        setPaginationSalaryArrayDepEmp,
        paginationPageSalaryDepEmp,
        setPaginationPageSalaryDepEmp,
        roleDepartmentToggle,
        setRoleDepartmentToggle,
        addEmployee,
        setAddEmployee,
        location,
        editEmployee,
        setEditEmployee,
        updateRole,
        setUpdateRole,
        updateDepartment,
        setUpdateDepartment,
        displayEmployeeDetails,
        addDepartment,
        setAddDepartment,
        updateSalary,
        setUpdateSalary,
        updateNewRoleOnFrontend,
        addTitle, 
        setAddTitle,
        myInformation, 
        setMyInformation,
        myInformationCalledOnce,
        myDepartmentInfoCalledOnce,
        myDepartment, 
        setMyDepartment,
        myOrganisation, 
        setMyOrganisation,
        myOrganisationInfoCalledOnce,
        userLogin,
        getMyOrganisationInfo,
        getEmployeeDetails,
        hasNextPage,
        getPaginatedColleagues,
        setColleaguesCursor,
        colleaguesCursor,
      }}
    >
      <>
        {loadSpinner && <LoadingButtonComponent loadSpinner={loadSpinner} />}
        {!loadSpinner && loginInfo && <HomePage />}
        {!loadSpinner && !loginInfo && <Login />}
      </>
    </AppContext.Provider>
  );
}

export default App;
