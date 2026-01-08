def add_stop(destinations,current_command):
    index = int(current_command[1])
    country = current_command[2]
    if index < len(destinations):
        beforre_index = destinations[:index]
        after_index = destinations[index:]
        destinations = beforre_index + country + after_index
    return destinations

def remove_stop(destinations,current_command):
    start_index = int(current_command[1])
    end_index = int(current_command[2])
    if int(start_index) < len(destinations) and len(destinations) > end_index:
        before_start_index = destinations[:start_index]
        after_end_index = destinations[end_index+1:]
        destinations = before_start_index + after_end_index
    return destinations


def switch(destinations,current_command):
    old_string = current_command[1]
    new_string = current_command[2]
    if old_string in destinations:
        destinations = destinations.replace(old_string,new_string)
    return destinations

stops_destinations = input()
command = input()
while command != 'Travel':
    command = command.split(':')

    if command[0] == 'Add Stop':
        stops_destinations = add_stop(stops_destinations,command)
        print(stops_destinations)
    elif command[0] == 'Remove Stop':
        stops_destinations = remove_stop(stops_destinations,command)
        print(stops_destinations)
    elif command[0] == 'Switch':
        stops_destinations = switch(stops_destinations, command)
        print(stops_destinations)

    command = input()

print(f"Ready for world tour! Planned stops: {stops_destinations}")





