sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0

# Подсчет суммы через вложенные циклы
for location in sales_data:
    for item in location:
        scoops_sold += item

print(scoops_sold)