from classes import user as User
import sqlite3
import hashlib
hash_func = hashlib.sha256()

conn = sqlite3.connect(r'./databases\main.db', check_same_thread=False)
c = conn.cursor()

def login(request_form):
    username = request_form['username']
    password = request_form['password']
    hash_func.update(password.strip().encode('utf-8'))
    c.execute("SELECT username, first_name, last_name, email, address, city, state, pincode, phone FROM user WHERE username = '{}' AND password = '{}';".format(username, password))
    res = c.fetchall()
    print(username, password, hash_func.hexdigest())
    print(res)
    if len(res) > 0:
        return User(res[0][0], res[0][1], res[0][2], res[0][3], res[0][4], res[0][5], res[0][6], res[0][7], res[0][8])
    return False

def register(request_form):
    username = request_form['username']
    email = request_form['email']
    password = request_form['password']
    confirm_password = request_form['confirm-password']
    if password != confirm_password:
        return 'Passwords do not match'
    c.execute("SELECT * FROM user WHERE username = '{}' OR email = '{}';".format(username, email))
    if len(c.fetchall()) > 0:
            return 'Username or email exists'
    else:
        hash_func.update(password.encode('utf-8'))
        c.execute("INSERT INTO USER (username, email, password) VALUES ('{}', '{}', '{}');".format(username, email, password))
        c.execute("Commit;")
        return 'Success'

def update_user(request_form):
    username = request_form['username']
    if request_form['password'] != '' and request_form['confirm'] != '':
        if request_form['password'] != request_form['confirm']:
            return 'password'
    c.execute("SELECT * FROM user WHERE username = '{}';".format(username))
    res = c.fetchall()
    if len(res) == 0:
        return False
    else:
        if request_form['password'] != '' and request_form['confirm'] != '':
            hash_func.update(request_form['password'].encode('utf-8'))
            c.execute("""UPDATE user SET first_name = '{}', last_name = '{}', address = '{}', 
            city = '{}', state = '{}', pincode = '{}', phone = '{}', password = '{}' WHERE username = '{}';""".format(
                request_form['firstname'], request_form['lastname'], request_form['address'], 
                request_form['city'], request_form['state'], request_form['pincode'], request_form['phone'],request_form['password'], username))
        else:
            c.execute("""UPDATE user SET first_name = '{}', last_name = '{}', address = '{}', 
            city = '{}', state = '{}', pincode = '{}', phone = '{}' WHERE username = '{}';""".format(
                request_form['firstname'], request_form['lastname'], request_form['address'], 
                request_form['city'], request_form['state'], request_form['pincode'], request_form['phone'], username))
        c.execute("commit;")
        return True


def user_obj(username):
    c.execute("SELECT username, first_name, last_name, email, address, city, state, pincode, phone FROM user WHERE username = '{}';".format(username))
    res = c.fetchall()
    if len(res) == 0:
        return False
    else:
        return User(res[0][0], res[0][1], res[0][2], res[0][3], res[0][4], res[0][5], res[0][6], res[0][7], res[0][8])