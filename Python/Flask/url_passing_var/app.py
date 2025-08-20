# ---------------------------To add multiple html Tags in same route and run in server live---------------------------
from flask import Flask

app = Flask(__name__)

@app.route("/")
def greet():
    return '<h1>Hello World</h1>'\
            '<h2>Hello World</h2>'


# if __name__ == "__main__":
#     app.run(debug=True) #To change the server side code live.

# ---------------------------Passing variable in URL---------------------------

#To get the passed data in the URL

@app.route("/username/<name>")
def username(name):
    return f"Heyy {name}.✌️"

# To make entire part as the text.

@app.route("/uname/<path:user>")
def uname(user):
    return (f"Heyy there its's just a text no routes accepted from here ! /"
            f"{user}😈")

# To pass multiple datatype data in the url path

@app.route("/details/<name>/<int:age>/<float:salary>")
def details(name,age,salary):
    return f'Hello {name}👋'\
           f'Your age is {age}✌️'\
           f'Your salary is {salary}💸'

if __name__ == "__main__":
    app.run(debug=True) #To change the server side code live.