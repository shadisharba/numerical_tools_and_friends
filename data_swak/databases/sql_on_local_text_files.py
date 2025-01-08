import os
import tempfile
import sqlite3

# Create a temporary folder
temp_folder = tempfile.mkdtemp()
print(f"Temporary folder: {temp_folder}")

# Generate random text files
file_names = []
for i in range(5):
    file_name = os.path.join(temp_folder, f"file{i}.txt")
    with open(file_name, "w") as file:
        file.write(f"This is file {i+1}")

    file_names.append(file_name)

# Create an in-memory SQLite database
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Create a table to store file data
cursor.execute("CREATE TABLE files (id INTEGER PRIMARY KEY, content TEXT)")

# Insert file data into the table
for i, file_name in enumerate(file_names):
    with open(file_name, "r") as file:
        content = file.read()
        cursor.execute("INSERT INTO files (id, content) VALUES (?, ?)", (i + 1, content))

# Query data from the text files using SQL
cursor.execute("SELECT * FROM files")
rows = cursor.fetchall()

# Print the query results
for row in rows:
    print(row)

# Close the database connection
conn.close()
