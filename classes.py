class user:
    def __init__(self, username, password):
        self.username = username
        self.first_name = ''
        self.last_name = ''
        self.email = ''
        self.password = password
        self.address = ''
        self.city = ''
        self.state = ''
        self.pincode = ''
        self.phone = ''

class book:
    def __init__(self, id, title, author, language, pages, quantity):
        self.id = id
        self.title = title
        self.author = author
        self.language = language
        self.pages = pages
        self.quantity = quantity

class borrowed_books:
    def __init__(self, id, username, title, author, language, date):
        self.id = id
        self.username = username
        self.title = title
        self.author = author
        self.language = language
        self.date = date