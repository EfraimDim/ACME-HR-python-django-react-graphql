from graphene import relay, ObjectType, Boolean
from .login import ColleaguesConnection

class PaginatedColleaguesType(ObjectType):
    hasNextPage = Boolean()
    colleagues = relay.ConnectionField(ColleaguesConnection)
    