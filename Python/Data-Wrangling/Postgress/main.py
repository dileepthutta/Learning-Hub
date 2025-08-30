import psycopg2

connection = psycopg2.connect(
    dbname="collegedb",
    user="postgres",
    password="",
    host="localhost",
    port="5432"
)
cursor = connection.cursor()

cursor.execute("Select version()")

version = cursor.fetchone()

print(f"Connected to Postgres SQL {version[0]}")

cursor.close()


