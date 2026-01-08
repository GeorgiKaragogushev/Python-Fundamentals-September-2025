class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        self.species = species
        if species == 'mammal':
            return f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == 'fish':
            return f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"
        elif species == 'bird':
            return f"Birds in {self.zoo_name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"


name_of_the_zoo = input()
animal = Zoo(name_of_the_zoo)
count = int(input())

for i in range(count):
    animal_info = input().split()
    species, name = animal_info
    animal.add_animal(species, name)
info = input()
print(animal.get_info(info))
