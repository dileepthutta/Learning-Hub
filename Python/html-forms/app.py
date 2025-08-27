from flask import Flask, render_template,request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        return f"<h1>Success form submitted! <h1>"
    else:
        return ""
if __name__ == "__main__":
    app.run(debug=True)
