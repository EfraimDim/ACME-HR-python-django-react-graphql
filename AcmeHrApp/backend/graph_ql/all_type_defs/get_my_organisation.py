from graphene import ObjectType, String, Field, Int, List
from .login import TitleNameType


class ManagersType(ObjectType):
    emp_no = Int()
    dept_no = String()
    emp_no__first_name = String()
    emp_no__last_name = String()

class DepartmentsType(ObjectType):
    dept_no = String()
    total = Int()
    dept_no__dept_name = String()

class DeptWithManagersListType(ObjectType):
    department = Field(DepartmentsType)
    manager = Field(ManagersType)

class MyOrganisationType(ObjectType):
    deptWithManagersList = List(DeptWithManagersListType)
    titlesList = List(TitleNameType)
