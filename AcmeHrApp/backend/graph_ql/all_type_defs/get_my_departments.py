from graphene import ObjectType, relay,  Field
from .login import ColleaguesConnection
from .get_my_information import DepartmentType

class MyDepartmentInfoType(ObjectType):
    department = Field(DepartmentType)
    departmentEmployees = relay.ConnectionField(ColleaguesConnection)
    