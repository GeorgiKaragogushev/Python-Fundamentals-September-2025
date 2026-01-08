list_of_deck = input().split()
number_of_shuffle = int(input())

for shuffle in range(number_of_shuffle):
    middle_part_of_the_dec = len(list_of_deck) // 2

    left_part = list_of_deck[:middle_part_of_the_dec]
    right_part = list_of_deck[middle_part_of_the_dec:]
    deck_after_shuffling = []
    for index in range(middle_part_of_the_dec):
        deck_after_shuffling.append(left_part[index])
        deck_after_shuffling.append(right_part[index])

    list_of_deck = deck_after_shuffling.copy()

print(list_of_deck)
