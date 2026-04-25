from mashq.db import db_connect

conn  = db_connect()
cur = conn.cursor()
conn.autocommit = True

# cur.execute(
#     "CREATE DATABASE users"
# )
# print("Yaratildi !!!")

# cur.execute(
#     """
#     CREATE TABLE students(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100)
#     )

#     """
# )
# print("Yaratildi !!!")

# cur.execute(
#     """
#     CREATE TABLE  teacher(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100)
#     )

#     """
# )
# print(" Yaratildi !!! ")

# cur.execute(
#     "INSERT INTO students(name) VALUES('Elbek')"
# )
# print("studentlar qo'shildi !!!")
# cur.execute(
#     "INSERT INTO teacher(name) VALUES('Odilbek')"
# )
# print("teacherlar qo'shildi !!! ")
cur.execute(
   " SELECT name FROM students UNION SELECT name FROM teacher;" 
)

rows = cur.fetchall()
for row in rows:
    print(row)

