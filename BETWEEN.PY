from conn import db_connect

conn = db_connect()
cur = conn.cursor()
conn.autocommit= True

# cur.execute(
    # """CREATE DATABASE avto"""
# )
# print("database yaratildi !!!")
# cur.execute(
#     """
#     CREATE TABLE car(
#     id SERIAL PRIMARY KEY,
#     model VARCHAR(800),
#     name VARCHAR(1000),
#     price NUMERIC(1000,2)
    
#     )
#     """
# )
# print("Tayyor ro'yhat")

# cur.execute(
#     "INSERT INTO car(model,name,price) VALUES ('BMW','M3',250000),('AUDI','S9',270000)"
# )
# print("tayyor")

# cur.execute(
#     # "SELECT * FROM car WHERE price BETWEEN 10 AND 3000000000000 "
#     # "SELECT * FROM car WHERE name BETWEEN 'A' AND 'S' "
#     # "SELECT AVG(price) FROM car "
#     # "SELECT COUNT(id) FROM car "
#     "SELECT (id) AS son_royhat"

# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)