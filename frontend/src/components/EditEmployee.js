import { useContext, useState } from "react";
import { AppContext } from "./AppContext";
import { useMutation } from "@apollo/client";
import swal from "sweetalert";
import AddAndEditEmployeeForm from "./AddAndEditEmployeeForm";
import { EDIT_EMPLOYEE } from "../graphql/mutations"

function EditEmployee() {
  const { employeeDepInfo, getEmployeeDetails, loginInfo, getPaginatedColleagues, colleaguesCursor } =
    useContext(AppContext);

  const [firstName, setFirstName] = useState(employeeDepInfo.user.userInfo.firstName);
  const [lastName, setLastName] = useState(employeeDepInfo.user.userInfo.lastName);
  const [gender, setGender] = useState(employeeDepInfo.user.userInfo.gender);
  const [birthDate, setBirthDate] = useState(employeeDepInfo.user.userInfo.birthDate);
  const [empNum, setEmpNum] = useState(`${employeeDepInfo.user.userInfo.empNo}`);
  const [role, setRole] = useState(employeeDepInfo.titleInfo[0].title);
  const [department, setDepartment] = useState(employeeDepInfo.deptInfo[0].departments.deptNo);
  const [hireDate, setHireDate] = useState(employeeDepInfo.user.userInfo.hireDate);

  const handleFirstName = (e) => {
    setFirstName(e.target.value);
  };

  const handleLastName = (e) => {
    setLastName(e.target.value);
  };

  const handleGender = (e) => {
    setGender(e.target.value);
  };

  const handleBirthDate = (e) => {
    setBirthDate(e.target.value);
  };

  const handleEmpNum = (e) => {
    setEmpNum(e.target.value);
  };

  const handleRole = (e) => {
    setRole(e.target.value);
  };

  const handleDepartment = (e) => {
    setDepartment(e.target.value);
  };

  const handleHireDate = (e) => {
    setHireDate(e.target.value);
  };

  const [editEmployee] = useMutation(EDIT_EMPLOYEE, {
    onError: (error) => {
      swal({
        title: "Edit Employee Failed!",
        text: `${error.message}`,
        icon: "error",
        button: "okay",
      });
      console.log(error);
    },
    onCompleted: async(editEmployeeData) => {
      try {
        console.log(editEmployeeData)
        swal({
          title: "Success!",
          text: `${editEmployeeData.editEmployee.message}`,
          icon: "success",
          button: "continue!",
        });
        await getEmployeeDetails({ variables: { empNo: empNum, accessibility: loginInfo.user.accessibility } });
        await getPaginatedColleagues({ variables: { cursor: colleaguesCursor } });
      } catch (e) {
        console.log(e);
      }
    },
  });

  const editAnEmployee = async (ev) => {
    try {
      ev.preventDefault();
      const currentDate = new Date().toISOString().split("T")[0];
      await editEmployee({
        variables: {
          firstName: firstName,
          lastName: lastName,
          gender: gender,
          birthDate: birthDate,
          empNum: empNum,
          originalDeptNo: employeeDepInfo.deptInfo[0].departments.deptNo,
          originalRole: employeeDepInfo.titleInfo[0].title,
          role: role,
          department: department,
          hireDate: hireDate,
          currentDate: currentDate,
        },
      });
    } catch (e) {
      console.log(e);
    }
  };
  return (
    <div>
      <AddAndEditEmployeeForm
        handleSubmit={editAnEmployee}
        firstName={firstName}
        lastName={lastName}
        gender={gender}
        birthDate={birthDate}
        empNum={empNum}
        role={role}
        department={department}
        hireDate={hireDate}
        handleFirstName={handleFirstName}
        handleLastName={handleLastName}
        handleGender={handleGender}
        handleBirthDate={handleBirthDate}
        handleEmpNum={handleEmpNum}
        handleRole={handleRole}
        handleDepartment={handleDepartment}
        handleHireDate={handleHireDate}
        addEmployee={false}
      />
    </div>
  );
}

export default EditEmployee;
