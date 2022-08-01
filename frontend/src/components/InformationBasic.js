import styles from "../styles/InformationBasic.module.css";
import { useContext } from "react";
import { AppContext } from "./AppContext";
import EditEmployee from "./EditEmployee";

function InformationBasic({ employeeInfo }) {
  const { loginInfo, location, setEditEmployee, editEmployee } = useContext(AppContext);

  const toggleEditEmployee = () => {
    setEditEmployee(!editEmployee);
  };

  return (
    <div>
      {employeeInfo.employeesManager !== "" && location.pathname === "/organisation" && (
        <>
          <h1 className={styles.headerMain}>Manager</h1>
          <div className={styles.employeeName}>
            {employeeInfo.employeesManager.firstName} {employeeInfo.employeesManager.lastName}
          </div>
        </>
      )}
      <h1 className={styles.headerMain}>Employee</h1>
      <div className={styles.employeeName}>
        {employeeInfo.user.userInfo.firstName} {employeeInfo.user.userInfo.lastName}
      </div>
      <div className={styles.editEmployeeWrapper}>
        <h2 className={styles.headerSecondary}>Employee Information</h2>
        {loginInfo.user.accessibility === "managerHR" && location.pathname === "/organisation" && (
          <div onClick={toggleEditEmployee} className={styles.hrLink}>
            {editEmployee ? "Cancel" : "Edit Details"}
          </div>
        )}
      </div>
      {editEmployee ? (
        <EditEmployee />
      ) : (
        <div className={styles.infoWrapperMain}>
          <div className={styles.infoWrapperSecondary}>
            <div className={styles.infoDetails}>
              <span className={styles.infoHeader}>First Name:</span>
              <br></br>
              {employeeInfo.user.userInfo.firstName}
            </div>
            <div className={styles.infoDetails}>
              <span className={styles.infoHeader}>Last Name:</span>
              <br></br>
              {employeeInfo.user.userInfo.lastName}
            </div>
            <div className={styles.infoDetails}>
              <span className={styles.infoHeader}>Gender:</span>
              <br></br>
              {employeeInfo.user.userInfo.gender}
            </div>
            <div className={styles.infoDetails}>
              <span className={styles.infoHeader}>Birth Date:</span>
              <br></br>
              {employeeInfo.user.userInfo.birthDate}
            </div>
          </div>
          <div className={styles.infoWrapperSecondary}>
            <div className={styles.infoDetails}>
              <span className={styles.infoHeader}>Employee Number:</span>
              <br></br>
              {employeeInfo.user.userInfo.empNo}
            </div>
            <div className={styles.infoDetails}>
              <span className={styles.infoHeader}>Current Role:</span>
              <br></br>
              {employeeInfo.titleInfo[0].title}
            </div>
            <div className={styles.infoDetails}>
              <span className={styles.infoHeader}>Current Department:</span>
              <br></br>
              {employeeInfo.deptInfo[0].departments.deptName}
            </div>
            <div className={styles.infoDetails}>
              <span className={styles.infoHeader}>Hire Date:</span>
              <br></br>
              {employeeInfo.user.userInfo.hireDate}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default InformationBasic;
