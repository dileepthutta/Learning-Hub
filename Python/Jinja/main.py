from flask import Flask,render_template
import random
import datetime

#  Jinja is templating language for python to send Python script into the HTML.
#  {{ Python Script}}

app = Flask(__name__)

@app.route("/")
def home():
    rand_num = random.randint(1,10)
    today = datetime.date.today()
    return render_template("index.html",num=rand_num,var=today.year)

if __name__ == "__main__":
    app.run(debug=True)
