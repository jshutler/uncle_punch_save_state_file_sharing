
from flask import Flask, render_template, request, url_for
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





