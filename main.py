from flask import Flask, render_template, request, flash
from authenticate import login, register

app = Flask(__name__)
app.secret_key = "secret key"

@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login_page_function():
    if request.method == 'POST':
        if not login(request.form):
            flash(message="Invalid username or password", category="danger")
        else:
            return render_template(r"logged_user_home.html", username=(request.form['username']).capitalize())
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

@app.route("/borrow", methods=['GET', 'POST'])
def borrow_book():
    if request.method == 'POST':
        id = request.form['book-id']
        flash(message=f"Borrowed book having id {id} sucessfully", category="success")
    return render_template(r"logged_user_home.html", username=request.form['username'])

@app.route("/request", methods=['GET', 'POST'])
def request_book():
    if request.method == 'POST':
        try:
            title = request.form['title']
            flash(message=f"Requested book {title} sucessfully", category="success")
            return render_template(r"logged_user_home.html", username=request.form['username'])
        except:
            return render_template(r"req_book.html", username=request.form['username'])

if __name__== "__main__":
    app.run(debug=True)