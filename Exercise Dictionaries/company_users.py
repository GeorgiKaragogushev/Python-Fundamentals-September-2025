info_storage = {}

command = input()
while command != 'End':
    company,employee_id = command.split(' -> ')

    if company not  in info_storage:
        info_storage[company] = []
    if employee_id not in info_storage[company]:
        info_storage[company].append(employee_id)
    command = input()

for company,id_list in info_storage.items():
    print(company)
    for id_number in id_list:
        print(f'-- {id_number}')

