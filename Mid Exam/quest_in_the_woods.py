days_adventure = int(input())
people_number = int(input())
initial_energy = float(input())
water_per_person = float(input())
food_per_person = float(input())

total_water = days_adventure *(people_number * water_per_person)
total_food = days_adventure *(people_number * food_per_person)


for day in range(1,days_adventure+1):
    daily_energy_loss = float(input())

    if initial_energy <= 0:
        print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
        break

    initial_energy -= daily_energy_loss

    if day % 2 == 0:
        total_water -= total_water * 0.30
        initial_energy += initial_energy * 0.05
    if day % 3 == 0:
        initial_energy += initial_energy * 0.10
        total_food -= total_food / people_number

if initial_energy > 0:
    print(f"You are ready for the quest. You will be left with {initial_energy:.2f} energy!")


