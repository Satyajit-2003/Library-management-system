from classes import book, borrowed_books


book_list = []
book_list.append(book(1, 'To Kill a Mockingbird', 'Harper Lee', 'English', 281, 6))
book_list.append(book(2, 'The Great Gatsby', 'F. Scott Fitzgerald', 'English', 218, 5))
book_list.append(book(3, 'One Hundred Years of Solitude', 'Gabriel García Márquez', 'Spanish', 417, 4))
book_list.append(book(4, 'The Brothers Karamazov', 'Fyodor Dostoevsky', 'Russian', 824, 10))
book_list.append(book(5, 'The Catcher in the Rye', 'J.D. Salinger', 'English', 234, 15))
book_list.append(book(6, 'Pride and Prejudice', 'Jane Austen', 'English', 279, 19))
book_list.append(book(7, 'The Odyssey', 'Homer', 'Greek', 416, 23))
book_list.append(book(8, 'Crime and Punishment', 'Fyodor Dostoevsky', 'Russian', 551, 18))
book_list.append(book(9, 'The Divine Comedy', 'Dante Alighieri', 'Italian', 798, 21))
book_list.append(book(10, 'Beloved', 'Toni Morrison', 'English', 275, 5))

borrowed_books_list = []
borrowed_books_list.append(borrowed_books(1, 'tannu', 'To Kill a Mockingbird', 'Harper Lee', 'English', '2020-01-01'))
borrowed_books_list.append(borrowed_books(2, 'tannu', 'The Great Gatsby', 'F. Scott Fitzgerald', 'English', '2020-01-01'))
borrowed_books_list.append(borrowed_books(3, 'tannu', 'One Hundred Years of Solitude', 'Gabriel García Márquez', 'Spanish', '2020-01-01'))
borrowed_books_list.append(borrowed_books(4, 'tannu', 'The Brothers Karamazov', 'Fyodor Dostoevsky', 'Russian', '2020-01-01'))
borrowed_books_list.append(borrowed_books(5, 'tannu', 'The Catcher in the Rye', 'J.D. Salinger', 'English', '2020-01-01'))
borrowed_books_list.append(borrowed_books(6, 'satya', 'Pride and Prejudice', 'Jane Austen', 'English', '2020-01-01'))
borrowed_books_list.append(borrowed_books(7, 'satya', 'The Odyssey', 'Homer', 'Greek', '2020-01-01'))
borrowed_books_list.append(borrowed_books(8, 'satya', 'Crime and Punishment', 'Fyodor Dostoevsky', 'Russian', '2020-01-01'))
borrowed_books_list.append(borrowed_books(9, 'satya', 'The Divine Comedy', 'Dante Alighieri', 'Italian', '2020-01-01'))
borrowed_books_list.append(borrowed_books(10, 'satya', 'Beloved', 'Toni Morrison', 'English', '2020-01-01'))

def get_home_books():
    return book_list[:8]

def search_book(search_query):
    result = []
    for book in book_list:
        if search_query.lower() in book.title.lower() or search_query.lower() in book.author.lower():
            result.append(book)
    return result

def borrow_book_func(username, book_id):
    # TODO: Add code to borrow book
    # return True if book is borrowed successfully
    return True

def return_book_func(username, book_id):
    # TODO: Add code to return book
    # return True if book is returned successfully
    return True

def borrowed_books(username):
    result = []
    for book in borrowed_books_list:
        if username == book.username:
            result.append(book)
    return result