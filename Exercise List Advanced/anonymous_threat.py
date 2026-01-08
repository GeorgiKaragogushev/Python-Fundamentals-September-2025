text = input().split()
command = input()

while command != '3:1':
    command = command.split()
    action = command[0]

    if action == 'merge':
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < 0 or start_index >= len(text):
            start_index = 0
        if end_index < 0 or end_index >= len(text):
            end_index = len(text)-1

        if start_index<= end_index:
            new_text = ''.join(text[start_index:end_index+1])
            del text[start_index:end_index+1]
            text.insert(start_index,new_text)

    elif action == 'divide':
        index = int(command[1])
        partition = int(command[2])
        selected_element = text[index]
        text.pop(index)
        result = []
        if len(selected_element) % partition == 0:
            partition_lenght = len(selected_element) // partition

            for i in range(0,len(selected_element),partition_lenght):
                substing = selected_element[i:partition_lenght+i]
                result.append(substing)

        else:
            partition_lenght = int(len(selected_element) // partition)
            current_iteration = 0
            for i in range(0,len(selected_element),partition_lenght):
                current_iteration+=1
                if current_iteration == partition:
                    substing = selected_element[i:]
                    result.append(substing)
                    break
                else:
                    substing = selected_element[i:partition_lenght+i]
                    result.append(substing)

        for element in reversed(result):
            text.insert(index,element)

    command = input()

print(' '.join(text))