entry  = input()
phones_dictionary = {}

while '-' in entry :
    name,number = entry .split('-')
    phones_dictionary[name] = number
    entry  = input()

entry = int(entry)

for i in range(entry):
    searched_name = input()
    if searched_name in phones_dictionary.keys():
        print(f'{searched_name} -> {phones_dictionary[searched_name]}')
    else:
        print(f"Contact {searched_name} does not exist.")


