import re
text = input()
while text != 'Done':
    pattern = r'<([A-Z][A-Za-z\s]+)>.*?&&([A-Z]{2}[0-9]{4}[A-Z]{2})&&'
    matches = re.findall(pattern,text)

    if matches:
        for match in matches:
            model= match[0]
            number = match[1]
            print(f"Linked car {model} with number {number}!")
    text = input()

