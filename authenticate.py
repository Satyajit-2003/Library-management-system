dummy_users = {'admin': 'admin', 'satya': 'satya'}

def login(request_form):
    username = request_form['username']
    password = request_form['password']
    if username in dummy_users and dummy_users[username] == password:
        return True
    else:
        return False

def register(request_form):
    username = request_form['username']
    email = request_form['email']
    password = request_form['password']
    confirm_password = request_form['confirm-password']
    if username in dummy_users:
        return 'User exists'
    if password != confirm_password:
        return 'Passwords do not match'
    else:
        dummy_users[username] = password
        return 'Success'
