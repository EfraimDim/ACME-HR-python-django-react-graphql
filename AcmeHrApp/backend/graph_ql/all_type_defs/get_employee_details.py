from .get_my_information import DeptInfoType, SalaryType, FullTitleType
from .login import EmployeeType
from graphene import List, ObjectType, Field, String, Int


class UserInfoType(ObjectType):
    userInfo = Field(EmployeeType)


class EmployeeInformationType(ObjectType):
    user = Field(UserInfoType)
    deptInfo = List(DeptInfoType)
    salaryInfo = List(SalaryType)
    titleInfo = List(FullTitleType)
    employeesManager = Field(EmployeeType)
