def percent_loaded(percents):
    if percents == 100:
        return '100% Complete!\n[%%%%%%%%%%]'
    total_loaded = percents // 10
    total_not_loaded = 10 - total_loaded
    return f"{percents}% [{'%' * total_loaded}{'.' * total_not_loaded}]\nStill loading..."

number = int(input())
print(percent_loaded(number))
