from flask import Flask, render_template,request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
# To print the form data after the user submitted the form.
def revive_data():
    if request.method == "POST":
        user_name = request.form.get('username')
        password = request.form.get('password')
        return f"<h1>Username: {user_name} Password: {password}</h1>"
    else:
        return ""

if __name__ == "__main__":
    app.run(debug=True)
