from flask import Flask, render_template
from forms import MyForm


app = Flask(__name__)
app.secret_key = "Apple"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login",methods=["POST","GET"])
def login():
    form=MyForm()
    if form.validate_on_submit():
        user_cri = {
            "email": "admin@email.com",
            "password": "12345678"
        }
        if user_cri['email'] == form.email.data and user_cri['password'] == form.password.data:
            return render_template("success.html")
        else:
            return render_template("denied.html")
        # print(form.email.data) # To print the data.
    return render_template("login.html",form=form)

if __name__ == '__main__':
    app.run(debug=True)
