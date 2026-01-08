lines = int(input())
plants_storage = {}

for line in range(lines):
    plant_name,plant_rarity= input().split('<->')
    plants_storage[plant_name] = {'rarety':plant_rarity, 'rating':[] }

command = input()
while command != 'Exhibition':
    current_command,plant_info = command.split(': ')
    if current_command == 'Rate':
        plant, plant_rating_or_rarety = plant_info.split(' - ')
        if plant not in plants_storage:
            print('error')
        else:
            plants_storage[plant]['rating'].append(plant_rating_or_rarety)
    elif current_command == 'Update':
        plant, plant_rating_or_rarety = plant_info.split(' - ')
        if plant not in plants_storage:
            print('error')
        else:
            plants_storage[plant]['rarety'] = plant_rating_or_rarety
    elif current_command == 'Reset':
        plant = plant_info
        if plant not in plants_storage:
            print('error')
        else:
            plants_storage[plant]['rating'] = []
    command = input()

print('Plants for the exhibition:')
for plant_nickname,plant_information in plants_storage.items():

    rarety_for_plant = int(plants_storage[plant_nickname]['rarety'])
    rating_for_plant = plants_storage[plant_nickname]['rating']
    average_rating = 0
    if rating_for_plant:
        average_rating = sum(map(float,rating_for_plant)) / len(rating_for_plant)
    print(f'- {plant_nickname}; Rarity: {rarety_for_plant}; Rating: {average_rating:.2f}')
