import styles from "../styles/DepartmentsTable.module.css";
import { useContext } from "react";
import { AppContext } from "./AppContext";

function DepartmentsTable() {
  const { setAddDepartment, displayEmployeeDetails, myOrganisation } = useContext(AppContext);

  const toggleAddDepartment = () => {
    setAddDepartment(true);
  };

  return (
    <div>
      <div className={styles.headerWrapper}>
        <h2 className={styles.header}>Departments</h2>
        <div onClick={toggleAddDepartment} className={styles.hrLink}>
          Add Department
        </div>
      </div>
      <div className={styles.table}>
        <div className={styles.departmentWrapper}>
          <div className={styles.tableHeader}>Dept Number</div>
          <div className={styles.tableHeader}>Department</div>
          <div className={styles.tableHeader}>Manager's Last Name</div>
          <div className={styles.tableHeader}>Manager's First Name</div>
          <div className={styles.tableHeader}>No. Employees</div>
        </div>
        {myOrganisation.deptWithManagersList.map((depts, index) => {
          return (
            <div key={index} className={styles.departmentWrapper} onClick={() => displayEmployeeDetails(`${depts.manager.emp_no}`)}>
              <div className={styles.tableInfo}>{depts.department.deptNo}</div>
              <div className={styles.tableInfo}>{depts.department.deptNo_DeptName}</div>
              <div className={styles.tableInfo}>{depts.manager.empNo_LastName}</div>
              <div className={styles.tableInfo}>{depts.manager.empNo_FirstName}</div>
              <div className={styles.tableInfo}>{depts.department.total}</div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default DepartmentsTable;
