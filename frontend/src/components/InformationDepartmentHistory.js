import styles from "../styles/InformationRoleHistory.module.css";

function InformationDepartmentHistory({ employeeInfo }) {
  return (
    <div>
      <div className={styles.table}>
        <div className={styles.infoWrapper}>
          <div className={styles.tableHeader}>Department</div>
          <div className={styles.tableHeader}>Start Date</div>
          <div className={styles.tableHeader}>End Date</div>
        </div>
        {employeeInfo.deptInfo.map((deptInfo, index) => {
              return (
                <div key={index} className={styles.infoWrapper}>
                  <div className={styles.tableInfo}>{deptInfo.departments.deptName}</div>
                  <div className={styles.tableInfo}>{deptInfo.deptEmp.fromDate}</div>
                  <div className={styles.tableInfo}>{deptInfo.deptEmp.toDate}</div>
                </div>
              );
            })
            }
      </div>
    </div>
  );
}

export default InformationDepartmentHistory;
