from flask import Flask

app = Flask(__name__)

@app.route("/")
def basic():
    return '<h1 style="text-align:center">Hello World'\
            '\n<a href="https://google.com/">Google'

if __name__ =="__main__":
    app.run(debug=True)