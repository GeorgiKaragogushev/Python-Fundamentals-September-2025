number_of_lines = int(input())
special_word = input()

my_list = []
filtered_list = []

for i in range(number_of_lines):
    text = input()

    my_list.append(text)

for sentace in my_list:
    if special_word in sentace:
        filtered_list.append(sentace)


print(my_list)
print(filtered_list)
