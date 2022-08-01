import styles from "../styles/InformationRoleHistory.module.css";

function InformationRoleHistory({ employeeInfo }) {
  return (
    <div>
      <div className={styles.table}>
        <div className={styles.infoWrapper}>
          <div className={styles.tableHeader}>Job Title</div>
          <div className={styles.tableHeader}>Start Date</div>
          <div className={styles.tableHeader}>End Date</div>
        </div>
        {employeeInfo.titleInfo.map((title, index) => {
              return (
                <div key={index} className={styles.infoWrapper}>
                  <div className={styles.tableInfo}>{title.title}</div>
                  <div className={styles.tableInfo}>{title.fromDate}</div>
                  <div className={styles.tableInfo}>{title.toDate}</div>
                </div>
              );
            })
            }
      </div>
    </div>
  );
}

export default InformationRoleHistory;
