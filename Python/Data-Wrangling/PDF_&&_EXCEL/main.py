import pprint
data = {
 "name": "Alice",
 "age": 25,
 "hobbies": ["reading", "cycling", "coding"],
 "skills": {"programming": "advanced", "design": "intermediate"}
}
# Using pprint for readable output
pprint.pprint(data, indent=2, width=40)

#
# This feature is particularly useful for debugging, presenting outputs in a clear
# manner, and inspecting large datasets during development.
# By customizing parameters like indentation, line width, and depth, pprint ensures
# that data is displayed in a way that is easy to interpret and analyze