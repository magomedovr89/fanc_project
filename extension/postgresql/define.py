from config import table_dict
def create_request(dictionary):
    requests_list = []
    for table_name in dictionary:
        temporary = []
        temporary.append(f'CREATE TABLE {table_name}(')
        for col_name in dictionary[table_name]:
            temporary.append(f'{col_name} {dictionary[table_name][col_name]},')
            req = (('\n\t').join(temporary))
            req = (req[:-1] + ');')
        requests_list.append(req)
    return requests_list





print(create_request(table_dict))