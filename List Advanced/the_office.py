numbers = list(map(int,input().split()))
factor = int(input())

multiply_happiness = [number * factor for number in numbers]
total_employers = len(multiply_happiness)
average_hapinnes = sum(multiply_happiness) / total_employers

total_happy_emplyoyers = [employer_hapiness for employer_hapiness in multiply_happiness if employer_hapiness >= average_hapinnes]

if len(total_happy_emplyoyers) < total_employers// 2:
    print(f"Score: {len(total_happy_emplyoyers)}/{total_employers}. Employees are not happy!")
else:
    print(f"Score: {len(total_happy_emplyoyers)}/{total_employers}. Employees are happy!")