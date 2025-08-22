# Rendering html files using python
# -html files are stored in the templates.
# -Method used to render html files (render_template)

from flask import Flask,render_template

app = Flask(__name__)

#Home route.
@app.route("/")
def home():
    return render_template("deepu.html")

if __name__ =="__main__":
    app.run()