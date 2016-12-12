import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    #retrive data
    c.execute("""SELECT DISTINCT orders.make, orders.model,
            inventory.Quantity FROM orders, inventory WHERE inventory.model = orders.model ORDER by orders.model ASC""")

    rows = c.fetchall()



    for r in rows:
        print  r[0] + " "+ r[1]
        print "Quantity : " + str(r[2])
        c.execute("SELECT count(order_date) FROM orders WHERE make =? and model =?", (r[0],r[1]))
        count_c = c.fetchone()[0]



        print "Order Count: ", count_c
        print
