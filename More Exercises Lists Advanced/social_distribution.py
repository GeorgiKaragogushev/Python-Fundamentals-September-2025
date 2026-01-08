population = list(map(int,input().split(', ')))
minimum_wealth = int(input())
wealthiest_part_index = population.index(max(population))
for i in range(len(population)):
    wealthiest_part_index = population.index(max(population))
    if population[i] < minimum_wealth:
        needed_wealth = minimum_wealth - population[i]
        population[i] += needed_wealth
        if population[wealthiest_part_index] < max(population):
            wealthiest_part_index = population.index(max(population))
        population[wealthiest_part_index] -= needed_wealth
if any(number < minimum_wealth for number in population):
    print('No equal distribution possible')
else:
    print(population)