import mysql.connector

def connect_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='DataBase_Name',
            user="root",
            password="YOUR_PASSWORD"
        )
        if connection.is_connected():
            print("Successfully Connected to MYSQL.")

            cursor = connection.cursor()

            query = "Select *from student_table where id>5 and marks >80"

            cursor.execute(query)

            #To fetch all the rows.
            rows = cursor.fetchall()

            #Print all the data
            for row in rows:
                print(row)


    except mysql.connector.Error as e:
        print(f"Error {e}")

    finally:
        try:
            if connection.is_connected():
                connection.close()
        except NameError:
            pass


#To insert the data into the database.
def add_data(id,name,age,sports,marks):

    try:
        connection = mysql.connector.connect(
            host='localhost',
            database="DataBase_Name",
            user="root",
            password="Password"
        )
        if connection.is_connected():
            cursor = connection.cursor()

            query = "INSERT INTO raghu (id,name,age,sports,marks) VALUES (%s, %s, %s, %s, %s)"

            values = (id,name,age,sports,marks)

            cursor.execute(query,values)

            connection.commit()

            print("Student Data inserted successfully!")

    except mysql.connector.Error as e:
        print(f"Error {e}")

    finally:
        try:
            if connection.is_connected():
                connection.close()
        except NameError:
            pass

add_data(id="11",name="student11",age="18",sports="Cricket",marks="57")


