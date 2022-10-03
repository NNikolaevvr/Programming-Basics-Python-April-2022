fav_book = input()
book_counter = 0
current_book = input()

while current_book != 'No More Books':

    book_counter += 1

    if fav_book == current_book:
        print(f'You checked {book_counter - 1} books and found it.')

        break

    current_book = input()

if current_book == 'No More Books':

    print(f'The book you search is not here!')
    print(f'You checked {book_counter} books.')


