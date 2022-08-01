from graphene import Field, String, ObjectType, Int
from .all_type_defs.hr_mutation_message import HrMutationType, AddDepartmentType
from .all_mutations.hr_manager_mutations.add_employee import add_employee_mutation
from .all_mutations.hr_manager_mutations.edit_employee import edit_employee_mutation
from .all_mutations.hr_manager_mutations.edit_employee_role import edit_employee_role_mutation
from .all_mutations.hr_manager_mutations.edit_employee_department import edit_employee_department_mutation
from .all_mutations.hr_manager_mutations.edit_employee_salary import edit_employee_salary_mutation
from .all_mutations.hr_manager_mutations.add_department import add_department_mutation
from .all_mutations.hr_manager_mutations.add_title import add_title_mutation


class Mutation(ObjectType):
    add_employee = Field(HrMutationType, first_name=String(
        required=True),
        last_name=String(required=True),
        gender=String(required=True),
        birth_date=String(required=True),
        emp_num=String(required=True),
        role=String(required=True),
        department=String(required=True),
        hire_date=String(required=True),
        salary=String(required=True))
    edit_employee = Field(HrMutationType, first_name=String(
        required=True),
        last_name=String(required=True),
        gender=String(required=True),
        birth_date=String(required=True),
        emp_num=String(required=True),
        original_dept_no=String(required=True),
        original_role=String(required=True),
        role=String(required=True),
        department=String(required=True),
        hire_date=String(required=True),
        current_date=String(required=True))
    edit_employee_role = Field(HrMutationType, emp_num=Int(
        required=True),
        department_no=String(required=True),
        original_role=String(required=True),
        new_role=String(required=True),
        new_role_start_date=String(required=True))
    edit_employee_department = Field(HrMutationType, emp_num=Int(
        required=True),
        new_department_no=String(required=True),
        new_department_start_date=String(required=True))
    edit_employee_salary = Field(HrMutationType, emp_num=Int(
        required=True),
        new_salary=String(required=True),
        new_salary_start_date=String(required=True))
    add_department = Field(AddDepartmentType, dept_no=String(
        required=True),
        dept_name=String(required=True),
        managers_emp_num=String(required=True),
        start_date=String(required=True))
    add_title = Field(HrMutationType, title_name=String(
        required=True))


    def resolve_add_employee(root, info, first_name, last_name, gender, birth_date, emp_num, role, department, hire_date, salary):
        response = add_employee_mutation(
            first_name, last_name, gender, birth_date, emp_num, role, department, hire_date, salary)
        return {'message': response}

    def resolve_edit_employee(root, info, first_name, last_name, gender, birth_date, emp_num, original_dept_no, original_role, role, department, hire_date, current_date):
        response = edit_employee_mutation(first_name, last_name, gender, birth_date, emp_num, role, department, hire_date, original_dept_no, original_role, current_date)
        return {'message': response}
    
    def resolve_edit_employee_role(root, info, emp_num, department_no, original_role, new_role, new_role_start_date):
        response = edit_employee_role_mutation(emp_num, department_no, original_role, new_role, new_role_start_date)
        return {'message': response}

    def resolve_edit_employee_department(root, info, emp_num, new_department_no, new_department_start_date):
        response = edit_employee_department_mutation(emp_num, new_department_no, new_department_start_date)
        return {'message': response}

    def resolve_edit_employee_salary(root, info, emp_num, new_salary, new_salary_start_date):
        response = edit_employee_salary_mutation(emp_num, new_salary, new_salary_start_date)
        return {'message': response}

    def resolve_add_department(root, info, dept_no, dept_name, managers_emp_num, start_date):
        response = add_department_mutation(managers_emp_num, dept_no, dept_name, start_date)
        return response

    def resolve_add_title(root, info, title_name):
        response = add_title_mutation(title_name)
        return {'message': response}
