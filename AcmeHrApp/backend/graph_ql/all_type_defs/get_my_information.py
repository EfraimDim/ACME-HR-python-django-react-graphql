import graphene
from graphene import Int, ObjectType, String, Field
from .login import FullTitleType


class SalaryType(ObjectType):
    salary = String()
    to_date = String()
    from_date = String()
    emp_no = Int()


class DepartmentType(ObjectType):
    dept_name = String()
    dept_no = String()


class DeptEmpType(ObjectType):
    emp_no = Int()
    dept_no = String()
    from_date = String()
    to_date = String()


class DeptInfoType(ObjectType):
    departments = Field(DepartmentType)
    dept_emp = Field(DeptEmpType)


class MyInformationType(ObjectType):
    deptInfo = graphene.List(DeptInfoType)
    salaryInfo = graphene.List(SalaryType)
    titleInfo = graphene.List(FullTitleType)
