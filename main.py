from flask import Flask, render_template, request, flash
from authenticate import login, register, user_obj, update_user
from book import get_home_books, search_book, borrow_book_func, return_book_func, borrowed_books

app = Flask(__name__)
app.secret_key = "secret key"

@app.route(rule="/admin_login", methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        resp = login(request.form)
        if resp:
            return render_template(r"admin_home.html")
        else:
            flash(message="Invalid password", category="danger")
    return render_template(r"logged_admin_home.html")

@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login_page_function():
    if request.method == 'POST':
        if request.form['username'] == 'admin':
            flash(message="Continue on admin login", category="danger")
            return render_template(r"admin_login.html")
        resp = login(request.form)

        
        if not resp:
            flash(message="Invalid username or password", category="danger")
        else:
            return render_template(r"logged_user_home.html", curr_user = resp, books = get_home_books())
    return render_template(r"login.html")

@app.route("/register" , methods=['GET', 'POST'])
def register_page_function():
    if request.method == 'POST':
        msg = register(request.form)
        if msg != 'Success':
            flash(message=msg, category="danger")
        else:
            flash(message="User registered successfully", category="success")
            return render_template(r"login.html")
    return render_template(r"register.html")

@app.route("/home", methods=['GET', 'POST'])
def ret_home():
    print(request.method)
    if request.method == 'POST':
        try:
            query = request.form['book-search']
            return render_template(r"logged_user_home.html", curr_user = user_obj(request.form['username']), books = search_book(query))
        except:
            return render_template(r"logged_user_home.html", curr_user=user_obj(request.form['username']), books = get_home_books())

@app.route("/borrow", methods=['GET', 'POST'])
def borrow_book():
    if request.method == 'POST':
        id = request.form['book-id']
        username = request.form['username']
        resp = borrow_book_func(username, id)
        if resp:
            flash(message=f"Borrowed book having id {id} sucessfully", category="success")
        else:
            flash(message=f"You already borrowed book having  {id}", category="danger")
    return render_template(r"logged_user_home.html", curr_user = user_obj(request.form['username']), books = get_home_books())

@app.route("/request", methods=['GET', 'POST'])
def request_book():
    if request.method == 'POST':
        try:
            title = request.form['title']
            flash(message=f"Requested book {title} sucessfully", category="success")
            return render_template(r"logged_user_home.html", curr_user = user_obj(request.form['username']), books = get_home_books())
        except:
            print(user_obj(request.form['username']).username)
            return render_template(r"req_book.html", curr_user = user_obj(request.form['username']))

@app.route("/profile", methods=['GET', 'POST'])
def view_profile():
    if request.method == 'POST' :
        try:
            resp = update_user(request.form)
            print(resp)
            if resp == 'password':
                flash(message="Passwords do not match", category="danger")
            elif resp:
                flash(message="Profile updated successfully", category="success")
                return render_template(r"logged_user_home.html", curr_user = user_obj(request.form['username']), books = get_home_books())
            else:
                flash(message="Profile not updated", category="danger")
        except:
            pass
        return render_template(r"edit_profile.html", curr_user = user_obj(request.form['username']))
    # return render_template(r"editprofile.html", curr_user = user_obj(request.form['username']))

@app.route("/borrowed_books", methods=['GET', 'POST'])
def view_borrowed_books():
    if request.method == 'POST':
        return render_template(r"borrowed_book.html", curr_user = user_obj(request.form['username']), books = borrowed_books(request.form['username']))

@app.route("/return_book", methods=['GET', 'POST'])
def return_book():
    if request.method == 'POST':
        id = request.form['book-id']
        username = request.form['username']
        resp = return_book_func(username, id)
        if resp:
            flash(message=f"Returned book having id {id} sucessfully", category="success")
        else:
            flash(message=f"Book having id {id} not borrowed", category="danger")
    return render_template(r"borrowed_book.html", curr_user = user_obj(request.form['username']), books = borrowed_books(request.form['username']))


#Admin methods
@app.route("/edit_book", methods=['GET', 'POST'])
def edit_book():
    if request.method == 'POST':
        id = request.form['book-id']
        flash(message=f"Edited book having id {id} sucessfully", category="success")
    return render_template(r"logged_admin_home.html", curr_user = user_obj(request.form['username']))

if __name__== "__main__":
    app.run(debug=True)