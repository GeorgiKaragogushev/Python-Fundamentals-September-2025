def input_type(word_type:str):
    if word_type == 'int':
        return int(data_number_or_text) * 2
    elif word_type == 'real':
        return f"{float(data_number_or_text) * 1.5:.2f}"
    elif word_type == 'string':
        return f'${data_number_or_text}$'


date_type = input()
data_number_or_text = input()
print(input_type(date_type))