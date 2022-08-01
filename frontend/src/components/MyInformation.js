import InformationBasic from "./InformationBasic";
import InformationRoleHistory from "./InformationRoleHistory";
import InformationDepartmentHistory from "./InformationDepartmentHistory";
import InformationSalary from "./InformationSalary";
import { useContext, useEffect } from "react";
import { AppContext } from "./AppContext";
import RoleDepartmentToggle from "./RoleDepartmentToggle";
import { useLazyQuery } from "@apollo/client";
import { GET_MY_INFORMATION } from "../graphql/queries";

function MyInformation() {
  const {
    loginInfo,
    setPaginationSalaryArray,
    paginationSalaryArray,
    paginationCountSalary,
    paginationPageSalary,
    setPaginationPageSalary,
    roleDepartmentToggle,
    setPaginationCountSalary,
    setMyInformation,
    myInformationCalledOnce,
    myInformation
  } = useContext(AppContext);

  const [getMyInformation] = useLazyQuery(GET_MY_INFORMATION, {
    onCompleted: (myInformation) => {
      try {
        setPaginationCountSalary(Math.ceil(myInformation.getMyInformation.salaryInfo.length / 10));
        setPaginationSalaryArray(myInformation.getMyInformation.salaryInfo.slice(0, 10));
        const user = loginInfo.user;
        console.log(myInformation)
        setMyInformation({user, ...myInformation.getMyInformation});
      } catch (e) {
        console.log(e);
      }
    },
  });

  useEffect(() => {
    if (myInformationCalledOnce.current) {
      return;
    } else {
      getMyInformation({ variables: { employeeId: loginInfo.user.userInfo.empNo} });
      myInformationCalledOnce.current = true;
    }
  });

  return (
    <>
      {myInformation && (
        <div>
          <InformationBasic employeeInfo={myInformation} />
          <RoleDepartmentToggle />
          {roleDepartmentToggle ? (
            <InformationRoleHistory employeeInfo={myInformation} />
          ) : (
            <InformationDepartmentHistory employeeInfo={myInformation} />
          )}
          <InformationSalary
            arrayToPaginate={myInformation.salaryInfo}
            paginatedArray={paginationSalaryArray}
            setPaginatedArray={setPaginationSalaryArray}
            paginationCount={paginationCountSalary}
            paginationPage={paginationPageSalary}
            setPaginationPage={setPaginationPageSalary}
          />
        </div>
      )}
    </>
  );
}

export default MyInformation;
