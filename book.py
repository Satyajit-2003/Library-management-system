from classes import book, borrowed_book
import sqlite3
import datetime 

conn = sqlite3.connect(r'./databases\main.db', check_same_thread=False)
c = conn.cursor()

def get_home_books():
    c.execute("SELECT * FROM book ORDER BY RANDOM() LIMIT 10;")
    ret_list = []
    res = c.fetchall()
    for i in res:
        ret_list.append(book(i[0], i[1], i[2], i[3], i[4], i[5]))
    return ret_list

def search_book(search_query):
    search_query.replace("'", "''")
    c.execute("SELECT * FROM book WHERE title LIKE '%{}%';".format(search_query))
    res = c.fetchall()
    result = []
    for i in res:
        result.append(book(i[0], i[1], i[2], i[3], i[4], i[5]))
    return result

def borrow_book_func(username, book_id):
    c.execute("SELECT * FROM BORROW WHERE id = {} and username = '{}' and returndate = NULL;".format(book_id, username))
    if len(c.fetchall()) > 0:
        return False
    c.execute("INSERT INTO BORROW VALUES ('{}', '{}', '{}', NULL);".format(
        username, book_id, str( datetime.date.today() ) ))
    c.execute("UPDATE book SET quantity = quantity - 1 WHERE id = {};".format(book_id));
    conn.commit()
    return True

def return_book_func(username, book_id):
    c.execute("UPDATE book SET quantity = quantity + 1 WHERE id = {};".format(book_id))
    c.execute("UPDATE BORROW SET returndate = '{}' WHERE id = {} and username = '{}';".format(
        str( datetime.date.today() ), book_id, username))
    conn.commit()
    return True

def borrowed_books(username):
    result = []
    c.execute("""SELECT b2.id, username, title, author, language, borrowdate, returndate FROM BORROW b1, BOOK b2 
    WHERE b1.id = b2.id AND username = '{}' ORDER BY returndate;""".format(username))
    res = c.fetchall()
    for i in res:
        result.append(borrowed_book(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
    return result