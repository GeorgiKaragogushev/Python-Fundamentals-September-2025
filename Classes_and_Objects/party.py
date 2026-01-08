class Party:
    def __init__(self):
        self.people = []

    def going_party(self):
        return f"Going: {', '.join(self.people)}"

    def total_going(self):
        return f"Total: {len(self.people)}"


party = Party()

while True:
    command = input()

    if command == 'End':
        break
    name = command

    party.people.append(name)

print(party.going_party())
print(party.total_going())
