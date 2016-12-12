import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    #update data
    #c.execute("UPDATE inventory SET Quantity = 77 WHERE model ='Focus'")
    #c.execute("UPDATE inventory SET Quantity = 13 WHERE model ='Acura'")
    #delete data
    #c.execute("DELETE FROM population WHERE city='Boston'")

    print "\nNEW DATA:\n"

    c.execute("SELECT *  FROM inventory WHERE Make = 'Ford'")


    #fetchall() retrieves all records from the query
    rows = c.fetchall()

    for r in rows:
        print r[0], r[1], r[2]
