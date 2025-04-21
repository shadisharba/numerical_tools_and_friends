import sqlite3
from faker import Faker

# connecting to the database
connection = sqlite3.connect("../../data_repo/sqlite.db")

# cursor
crsr = connection.cursor()

# SQL command to create a table in the database
sql_command = """CREATE TABLE IF NOT EXISTS emp ( 
staff_number INTEGER PRIMARY KEY, 
fname VARCHAR(20), 
lname VARCHAR(30), 
gender CHAR(1), 
joining DATE);"""
crsr.execute(sql_command)

# Clear the emp table before inserting new rows. Here's how you can do it:
sql_command = "DELETE FROM emp;"
crsr.execute(sql_command)

# generate and insert 10 rows of data
fake = Faker()
for idx in range(10):
    staff_number = idx + 1
    fname = fake.first_name()
    lname = fake.last_name()
    gender = fake.random_element(elements=("M", "F"))
    joining = fake.date()

    # SQL command to insert data into the table
    sql_insert = f"INSERT INTO emp VALUES ({staff_number}, '{fname}', '{lname}', '{gender}', '{joining}');"

    crsr.execute(sql_insert)

# commit the changes
connection.commit()
crsr.execute(sql_command)
connection.close()

# connect to the database again, fetch all the rows and print them
connection = sqlite3.connect("../../data_repo/sqlite.db")
crsr = connection.cursor()
crsr.execute("SELECT * FROM emp")
rows = crsr.fetchall()
for row in rows:
    print(row)
connection.close()
