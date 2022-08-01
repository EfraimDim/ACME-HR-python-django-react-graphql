import graphene
from graphene import Int, relay, ObjectType, String, Field


class FullTitleType(ObjectType):
    title = String()
    to_date = String()
    from_date = String()
    emp_no = Int()


class TitleNameType(ObjectType):
    title = graphene.String()


class ColleaguesType(ObjectType):
    title = Field(FullTitleType)
    birth_date = String()
    emp_no = Int()
    first_name = String()
    last_name = String()
    gender = String()
    hire_date = String()

    class Meta:
        interfaces = (relay.Node,)  # make sure you add this
        fields = "__all__"


class ColleaguesConnection(relay.Connection):
    class Meta:
        node = ColleaguesType


class EmployeeType(ObjectType):
    birth_date = graphene.String()
    emp_no = Int()
    first_name = graphene.String()
    last_name = graphene.String()
    gender = graphene.String()
    hire_date = graphene.String()


class UserType(ObjectType):
    accessibility = String()
    dept_no = String()
    userInfo = Field(EmployeeType)


class LoginType(ObjectType):
    colleagues = relay.ConnectionField(ColleaguesConnection)
    totalEmployeeCount = graphene.Int()
    user = graphene.Field(UserType)
