from flask import Flask,render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    blog_data = response.json()
    return render_template("blog_post.html",post=blog_data)

if __name__ == "__main__":
    app.run(debug=True)