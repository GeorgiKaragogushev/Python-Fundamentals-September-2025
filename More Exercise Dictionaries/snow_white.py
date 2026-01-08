data = {}

command = input()
while command != 'Once upon a time':
    command = command.split(' <:> ')
    name =  command[0]
    hat_color =  command[1]
    physics = int(command[2])

    if name not in data:
        data[name] = {hat_color:physics}
    elif name in data:
        if hat_color not in data[name]:
            data[name][hat_color] = physics
        elif hat_color in data[name]:
            if data[name][hat_color] < physics:
                data[name][hat_color] = physics

    command = input()
info_list = []
for dwarf_name, info in data.items():
    for color, points in info.items():
       info_list.append((dwarf_name,color,points))

color_list = {}
for dwarf,color,points in info_list:
    color_list[color] = color_list.get(color,0) +1

sorted_info = sorted(info_list,key=lambda x: (-x[2], -color_list[x[1]]))

for dward,color,points in sorted_info:
    print(f'({color}) {dward} <-> {points}')

