# ------------------------------------Hello World using Flask-------------------------------------------------
from flask import Flask
app = Flask(__name__)

print(__name__)
@app.route("/")
def hello_world():
    return '<h1>Hello,World!</h1>'

# @ is a python decorator used to create route.

@app.route("/deepu")
def deepu():
    return "<h1>Deepu</h1>"

# Hello World server using Flask

# How to run

# set FLASK_APP = FILE_NAME
# flask run [To run the flask server]


# ----------------------------------To Run the Server Directly-----------------------------------------------
if __name__ =="__main__":
    app.run()



