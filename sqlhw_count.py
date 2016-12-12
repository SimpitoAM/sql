import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    #create a dictionary of sql queries
    sql = { 'Ford Ranger Orders: ': "SELECT count(model) FROM orders WHERE model ='Ranger'",
            'Ford Focus Orders: ': "SELECT count(model) FROM orders WHERE model ='Focus'",
            'Ford Aplus Orders: ': "SELECT count(model) FROM orders WHERE model ='Aplus'",
            'Honda CRV Orders: ': "SELECT count(model) FROM orders WHERE model ='CRV'",
            'Honda Acura Orders: ': "SELECT count(model) FROM orders WHERE model ='Acura'"

            }

    #run each sql query item in the dictionary
    for keys, values in sql.iteritems():

        # run sql
        c.execute(values)

        # fetchone() retrieves one record from the query
        result = c.fetchone()

        #output the result to screen
        print keys + ":", result[0]
