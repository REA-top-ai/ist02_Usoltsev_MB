tables ={
    1: ['Jiho', False],
    2: [],
    3: [],
    4: []
}


def assign_table (table_number, name, vip_status=False):
    tables[table_number] = [name, vip_status]


assign_table(6, 'Yoni', False)
assign_table(4, 'Карла')

print(tables)