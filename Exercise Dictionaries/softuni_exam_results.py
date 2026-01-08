command = input()
submissions_list = {}
dict_with_submissions = {}

while command != 'exam finished':
    if len(command.split('-')) > 2:
        username, language, points = command.split('-')


        if language not in submissions_list:
            submissions_list[language] = {username: points}
        elif username not in submissions_list[language]:
            submissions_list[language].update({username: points})
        elif username in submissions_list[language]:
            if int(points) > int(submissions_list[language][username]):
                submissions_list[language][username] = points
        if language not in dict_with_submissions:
            dict_with_submissions[language] = 0
        dict_with_submissions[language] +=1
    else:
        command = command.split('-')
        username = command[0]

        for lang in submissions_list.keys():
            if username in submissions_list[lang]:
                del submissions_list[lang][username]

    command = input()

print('Results:')
for lang,info in submissions_list.items():
    for name,points in info.items():
        print(f'{name} | {points}')

print('Submissions:')
for lang,submissions in dict_with_submissions.items():
    print(f'{lang} - {submissions}')
