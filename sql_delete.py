#import the sqlite3 library
import sqlite3

with sqlite3.connect("new.db") as connection:
    c= connection.cursor()

    c.execute("DELETE FROM orders")

    c.execute("SELECT * FROM orders")

    rows = c.fetchall()

    for r in rows:
        print r[0], [1],[2]

#close the database connection
