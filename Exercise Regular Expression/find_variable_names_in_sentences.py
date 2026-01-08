import re

text= input()

pattern = r'\b_([A-Za-z0-9]+)\b'

print(','.join(re.findall(pattern,text)))