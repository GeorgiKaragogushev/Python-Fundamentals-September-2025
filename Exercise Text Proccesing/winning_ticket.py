tickets = [ticket.strip() for ticket in input().split(', ')]
symbols = ['@', '#', '$', '^']

for ticket in tickets:
    is_valid = False
    if len(ticket) != 20:
        print('invalid ticket')
        continue

    left_part = ticket[:10]
    right_part = ticket[10:]

    for symbol in symbols:
        for lenght in range(10,5,-1):
            symbol_repetitions = symbol * lenght
            if symbol_repetitions in left_part and symbol_repetitions in right_part:
                if lenght == 10:
                    is_valid = True
                    print(f'ticket "{ticket}" - {lenght}{symbol} Jackpot!')
                    break
                else:
                    is_valid = True
                    print(f'ticket "{ticket}" - {lenght}{symbol}')
                    break
        if is_valid:
            break
    else:
        print(f'ticket "{ticket}" - no match')













