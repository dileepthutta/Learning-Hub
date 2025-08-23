from flask import Flask,render_template
import requests
from datetime import date

# Gender API || Age API ENDPOINTS
GENDER_API_ENDPOINT = "https://api.genderize.io/"
AGE_API_ENDPOINT = "https://api.agify.io/"

# API para's
api_params = {
    "name" : "Jose"
}

# Response of Gender API
response1 = requests.get(
    url= GENDER_API_ENDPOINT,
    params=api_params
)

# Response of Age API
response2 = requests.get(
    url=AGE_API_ENDPOINT,
    params=api_params
)

# Response from API
data = response1.json()
data1 = response2.json()


name = data['name']
gender = data['gender']
age = data1['age']
date = date.today()

# ------------------------------------FLASK Server------------------------------------------------------------
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",name=name,gender=gender,age=age,date=date.year)

if __name__ == "__main__":
    app.run(debug=True)