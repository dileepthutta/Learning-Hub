from flask import Flask,render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField
from form import MyForm

app = Flask(__name__)
app.secret_key = "heyy"

@app.route("/")
def home():
    form = MyForm()
    return render_template("index.html",form=form)

@app.route("/response",methods=["POST","GET"])
def response():
    if request.method == "POST":
        return "<h1>Registration Done</h1>"
    else:
        return ""

if __name__ =="__main__":
    app.run(debug=True)