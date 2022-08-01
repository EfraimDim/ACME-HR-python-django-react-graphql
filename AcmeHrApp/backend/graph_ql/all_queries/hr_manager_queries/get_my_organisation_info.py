from ....queries.hr_manager_queries.get_department_info_for_hr import get_department_info_for_hr
from ....queries.hr_manager_queries.get_department_manager_info_for_hr import get_department_manager_info_for_hr
from ....queries.hr_manager_queries.get_titles_list import get_titles_list


def get_my_organisation_info_query():
    departments_list = get_department_info_for_hr()
    managers_list = get_department_manager_info_for_hr()
    titles_list = get_titles_list()
    dept_with_managers_list = []
    for i in range(0, len(departments_list)):
        department_with_manager = {
            'department': departments_list[i], 'manager': managers_list[i]}
        dept_with_managers_list.append(department_with_manager)
    return {'deptWithManagersList': dept_with_managers_list, 'titlesList' : titles_list}