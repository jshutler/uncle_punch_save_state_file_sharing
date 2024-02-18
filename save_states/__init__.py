
from flask import Flask, render_template, redirect, request, session, url_for, make_response, abort
from werkzeug.utils import secure_filename
from markupsafe import escape
app = Flask(__name__)
test_env = True

if test_env:
    app.secret_key = 'testing_key'
    print(f'Using testing enviornment')

app.url_map.strict_slashes = False 

users = [
    {"id": 1, "name": "Benjamin"},
    {"id": 2, "name": "John"},
    {"id": 3, "name": "George"}
]

app.secret_key = "poop"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.permanent = True
        session["username"] = request.form["username"]
        return redirect(url_for("index"))
    return render_template("login.html")

@app.route("/index")
def index():
    print(session["username"])
    return render_template("index.html", logged_in="username" in session)


@app.route("/file_uploader", methods=["GET", "POST"])
def file_uploader():
    upload_success = False
    if request.method == "POST":
        file = request.files["uploadedFile"]
        file.save(secure_filename(file.filename))
        upload_success = True
    
    return render_template("file_uploader.html", upload_success=upload_success)


@app.route("/")
def home():
    print(url_for('test'))
    return  render_template("index.html")

@app.route("/my/test/route")
def test():
    return "Test"

@app.route("/set_cookie/<username>")
def set_cookie(username):
    res = make_response("Hello!")
    res.headers['my-header'] = "This is my header"

    res.set_cookie("username", 
        value=username,
        max_age=60,
        expires=None,
        path='/',
        secure=True,
        httponly=True, # lets javascript access cookies
        samesite="None")
    return res

@app.route("/whoami")
def whoami():
    # how to access cookies
    username = request.cookies.get("username", 'no cookie')

    return username

@app.route('/logout')
def logout():
    # remove session variable
    session.pop("username", None)
    res = make_response("Goodbye")
    # remove cookie
    res.set_cookie("username", value="")
    return redirect(url_for("index"))
    # return res
# this gives us a custom error page for a given type of error
# meant primarily for client side 400 errors
@app.errorhandler(404) 
def not_found_error(e):
    print(e)
    return render_template("404.html"), 404



@app.route('/admin')
def admin():
    abort(401) # for when we know what we want

    print("This will never execute")
    return "", 401
# @app.route("/sign_up")
# def form():
    # return render_template("form.html")

# @app.route("/search")
# def search():
#     return render_template('search.html')

# @app.route("/completed", methods=["POST", "GET"])
# def sign_up_completed():
#     if request.method == "POST":
#         if request.form["username"] == 'jack' and request.form['password'] == 'pass':
#             return "Login Successful"
    
#     return "Not Successful"

# @app.route("/")
# def hello():
#     return "<h1> Hello World</h1>"

# @app.route("/<string:name>")
# def hi_name(name):
#     return render_template("index.html", name=name)

# @app.route("/user/<int:id>")
# def foo(id):
#     print(type(id))

#     for user in users:
#         if user.get('id') == id:
#             return user["name"]
        
#     return f"<h1>User Not found!</h1>"





