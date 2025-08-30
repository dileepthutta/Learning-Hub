
# TO unzip the data.

combined = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]

names, scores = zip(*combined)

print("Unzipped Names:")
print(list(names))

print("Unzipped Scores:")
print(list(scores))
