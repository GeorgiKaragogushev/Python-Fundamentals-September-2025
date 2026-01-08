number_of_pieces = int(input())
pieces = {}


for piece in range(number_of_pieces):
    piece_name,piece_composer,piece_key = input().split("|")
    if piece_name not in pieces:
        pieces[piece_name] = {'Composer':piece_composer,'Piece key': piece_key}
command = input()
while command != 'Stop':
    command = command.split('|')
    action = command[0]
    if action == 'Add':
        piece_name = command[1]
        piece_composer = command[2]
        piece_key = command[3]
        if piece_name in pieces:
            print(f"{piece_name} is already in the collection!")
        else:
            pieces[piece_name] = {'Composer':piece_composer,'Piece key': piece_key}
            print(f"{piece_name} by {piece_composer} in {piece_key} added to the collection!")
    elif action == 'Remove':
        piece_name = command[1]
        if piece_name in pieces:
            del pieces[piece_name]
            print(f'Successfully removed {piece_name}!')
        else:
            print(f"Invalid operation! {piece_name} does not exist in the collection.")
    elif action == 'ChangeKey':
        piece_name = command[1]
        new_piece_key = command[2]
        if piece_name in pieces:
            pieces[piece_name]['Piece key'] = new_piece_key
            print(f"Changed the key of {piece_name} to {new_piece_key}!")
        else:
            print(f"Invalid operation! {piece_name} does not exist in the collection.")
    command = input()

for piece_name,value in pieces.items():
    piece_composer = value['Composer']
    piece_key = value['Piece key']
    print(f"{piece_name} -> Composer: {piece_composer}, Key: {piece_key}")