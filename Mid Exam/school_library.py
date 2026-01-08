shelf_with_books = input().split('&')

while True:
    command = input()

    if command == 'Done':
        print(', '.join(shelf_with_books))
        break
    command = command.split(' | ')
    current_command = command[0]
    book_name = command[1]

    if current_command == "Add Book":
        if book_name in  shelf_with_books:
            continue
        else:
            shelf_with_books.insert(0,book_name)

    elif current_command == 'Take Book':
        if book_name in shelf_with_books:
            shelf_with_books.remove(book_name)
        else:
            continue
    elif current_command == 'Insert Book':
        if book_name not in shelf_with_books:
            shelf_with_books.append(book_name)
        else:
            continue
    if current_command == 'Swap Books':
        second_book_name = command[2]
        if book_name in  shelf_with_books and  second_book_name in shelf_with_books:
            first_book_index = shelf_with_books.index(book_name)
            second_book_index = shelf_with_books.index(second_book_name)
            [shelf_with_books[first_book_index]],[shelf_with_books[second_book_index]] = [shelf_with_books[second_book_index]],[shelf_with_books[first_book_index]]
        else:
            continue

    elif current_command == 'Check Book':
        index = int(book_name)
        if len(shelf_with_books) < index:
            continue
        else:
            print(shelf_with_books[index])





