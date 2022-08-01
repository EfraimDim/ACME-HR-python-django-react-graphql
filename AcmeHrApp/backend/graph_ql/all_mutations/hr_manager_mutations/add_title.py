from ....queries.hr_manager_queries.add_new_title import add_new_title


def add_title_mutation(title_name):
    add_new_title(title_name)
    return 'Title added to the database!'
