#executemany() method
import csv
import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    c.execute("""CREATE TABLE orders
            (make TEXT, model TEXT, order_date INT)""")

    #open the csv file and assign it to a variable
    inv_cars = csv.reader(open("invent_cars.csv", "rU"))

    #create a new table called employees
    #c.execute("CREATE TABLE inventory(Make TEXT, Model TEXT, Quantity INT)")

    #insert data into table
    c.executemany("INSERT INTO orders(make, model, order_date) VALUES (?,?,?)", inv_cars)
