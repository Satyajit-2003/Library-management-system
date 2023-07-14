class user:
    def __init__(self, username, first_name, last_name, email, address, city, state, pincode, phone):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.pincode = pincode
        self.phone = phone


class book:
    def __init__(self, id, title, author, language, pages, quantity):
        self.id = id
        self.title = title
        self.author = author
        self.language = language
        self.pages = pages
        self.quantity = quantity

class borrowed_book:
    def __init__(self, id, username, title, author, language, borrowdate, returndate):
        self.id = id
        self.username = username
        self.title = title
        self.author = author
        self.language = language
        self.borrowdate = borrowdate
        self.returndate = returndate