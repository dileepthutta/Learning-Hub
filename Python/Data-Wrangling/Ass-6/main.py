
# Python Script for PPrint.

from pprint import pprint

data = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "Data Analysis", "Machine Learning"],
    "education": {
        "undergraduate": {
            "degree": "BSc",
            "major": "Computer Science"
        },
        "postgraduate": {
            "degree": "MSc",
            "major": "AI and Robotics"
        }
    }
}

print("Pretty Printed Data:")
pprint(data)
