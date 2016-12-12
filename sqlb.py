#import the sqlite3 library
import sqlite3

#create database if database doesn't already exist
conn = sqlite3.connect("new.db")

#get a  cursor object used to execute SQL commands
cursor = conn.cursor()

try:
    #insert data
    cursor.execute("INSERT INTO populations VALUES('New York City', \
    'NY', 8200000)")
    cursor.execute("INSERT INTO populations VALUES('Lusaka', \
    'LSK', 3000000)")

    #commit the changes
    conn.commit()
except sqlite3.OperationalError:
    print "Ooops! Something went wrong. Try again..."

#close the database connection
conn.close()
