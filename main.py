from flask import Flask, render_template, request, flash
from authenticate import login, register

app = Flask(__name__)
app.secret_key = "secret key"

@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login_page_function():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if login(request.form):
            return render_template(r"home.html", username=username)
        else:
            return render_template(r"login.html", error="Invalid username or password")
    return render_template(r"login.html")


@app.route("/register" , methods=['GET', 'POST'])
def register_page_function():
    if request.method == 'POST':
        if register(request.form) == 'User exists':
            flash(message="User exists", category="danger")
        elif register(request.form) == 'Passwords do not match':
            flash(message="Passwords do not match", category="danger")
        elif register(request.form) == 'Success':
            flash(message="User registered successfully", category="success")
            return render_template(r"login.html")
    return render_template(r"register.html")

if __name__== "__main__":
    app.run(debug=True)