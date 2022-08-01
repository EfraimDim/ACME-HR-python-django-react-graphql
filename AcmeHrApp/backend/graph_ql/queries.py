import graphene
from graphene import Field, List
from .all_type_defs.login import LoginType
from .all_type_defs.get_my_information import MyInformationType
from .all_type_defs.get_my_departments import MyDepartmentInfoType
from .all_type_defs.get_my_organisation import MyOrganisationType
from .all_type_defs.get_employee_details import EmployeeInformationType
from .all_type_defs.get_paginated_colleagues import PaginatedColleaguesType
from .all_queries.user_queries.login import login_query
from .all_queries.user_queries.get_my_information import get_my_information_query
from .all_queries.hr_manager_queries.get_my_organisation_info import get_my_organisation_info_query
from .all_queries.managers_queries.get_my_department_info import get_my_department_info_query
from .all_queries.managers_queries.get_employee_details import get_employee_details_query
from .all_queries.user_queries.get_next_group_of_colleagues import get_next_group_of_colleagues_query


class Query(graphene.ObjectType):
    login = Field(LoginType, employee_id=graphene.String(
        required=True), password=graphene.String(required=True))
    get_my_information = Field(MyInformationType, employee_id=graphene.Int(
        required=True))
    get_my_department_info = Field(MyDepartmentInfoType, dept_no=graphene.String(
        required=True))
    get_my_organisation_info = Field(MyOrganisationType)
    get_employee_details = Field(EmployeeInformationType, emp_no=graphene.Int(
        required=True), accessibility=graphene.String(
        required=True))
    get_paginated_colleagues = Field(PaginatedColleaguesType, cursor=graphene.Int(
        required=True))

    def resolve_login(root, info, employee_id, password):
        response = login_query(employee_id, password)
        return response

    def resolve_get_my_information(root, info, employee_id):
        response = get_my_information_query(employee_id)
        return response

    def resolve_get_my_department_info(root, info, dept_no):
        response = get_my_department_info_query(dept_no)
        return response

    def resolve_get_my_organisation_info(root, info,):
        dept_with_managers_list = get_my_organisation_info_query()
        return dept_with_managers_list

    def resolve_get_employee_details(root, info, emp_no, accessibility):
        response = get_employee_details_query(emp_no, accessibility)
        return response

    def resolve_get_paginated_colleagues(root, info, cursor):
        response = get_next_group_of_colleagues_query(cursor)
        return response
