# We use multiline statements like if statement or for loop we use this type of multiline statements

from flask import Flask,render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    posts = response.json()
    return render_template("index.html",data=posts)

if __name__ == "__main__":
    app.run(debug=True)
