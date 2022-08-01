from ....queries.user_queries.get_all_employees import get_all_employees


def get_next_group_of_colleagues_query(offset):
    new_colleagues = get_all_employees(1000, int(offset))
    hasNextPage = False
    if (len(new_colleagues) == 1000):
        hasNextPage = True
    return {'colleagues': new_colleagues, 'hasNextPage': hasNextPage}
