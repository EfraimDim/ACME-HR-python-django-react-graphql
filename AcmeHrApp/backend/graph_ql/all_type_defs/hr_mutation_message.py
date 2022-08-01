from graphene import ObjectType, String, Field

class HrMutationType(ObjectType):
    message = String()

class ManagerNameType(ObjectType):
    first_name = String()
    last_name = String()

class AddDepartmentType(ObjectType):
    message = String()
    newManager = Field(ManagerNameType)
